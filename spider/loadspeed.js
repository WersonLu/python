var page = require('webpage').create(),
    system = require('system'),
    t, address;
if (system.args.length === 1) {
    console.log('Usage:loadspeed.js<some URL>');
    phantom.exit();
}
t = Date.now()
address = system.args[1];
page.open(address, function (status) {
    if (status !== 'success') {
        console.log("加载失败");

    } else {
        t = Date.now() - t;

        console.log('加载中' + system.args[1]);
        console.log('加载时间' + t + 'msec')
    }
    phantom.exit();

})