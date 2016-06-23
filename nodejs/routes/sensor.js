var express = require('express');
var http = require('http');
var router = express.Router();
var SensorTag = require('sensortag');

SensorTag.discoverById(id, callback(sensorTag));

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', { title: 'Api documentation' });
});

var ADDRESS = "b0:b4:48:c9:74:80";
var connected = new Promise(function(resolve, reject) {
        SensorTag.discoverByAddress(ADDRESS, function(tag) {
            resolve(tag);
        });
    }
    ).then(function(tag) {
    new Promise(function(resolve, reject) {
        tag.connectAndSetup(function() {
            resolve(tag);
        });
    });
});

//==============================================================================
// Step 2: Enable the sensors you need.
//------------------------------------------------------------------------------
// For a list of available sensors, and other functions,
// see https://github.com/sandeepmistry/node-sensortag.
// For each sensor enable it and activate notifications.
// Remember that the tag object must be returned to be able to call then on the
// sensor and register listeners.
var sensor = connected.then(function(tag) {
    log("connected");

    tag.enableIrTemperature(log);
    tag.notifyIrTemperature(log);

    tag.enableHumidity(log);
    tag.notifyHumidity(log);

    tag.enableGyroscope(log);
    tag.notifyGyroscope(log);
    return tag;
});

//==============================================================================
// Step 3: Register listeners on the sensor.
//------------------------------------------------------------------------------
// You can register multiple listeners per sensor.
//

// A simple example of an act on the humidity sensor.
var prev = 0;
sensor.then(function(tag) {
    tag.on("humidityChange", function(temp, humidity){
        if(prev < 35 && humidity > 35) {
            log("Don't slobber all over the SensorTag please...");
        }
        prev = humidity;
    });
});

// A simple example of an act on the irTemperature sensor.
sensor.then(function(tag) {
    tag.on("irTemperatureChange", function(objectTemp, ambientTemp) {
        if(objectTemp > 25) {
            log("You're so hot");
        }
    });
});

//==============================================================================
// Step 4 (optional): Configure periods for sensor reads.
//------------------------------------------------------------------------------
// The registered listeners will be invoked with the specified interval.
sensor.then(function(tag) {
    tag.setIrTemperaturePeriod(3000, log);
});

module.exports = router;
