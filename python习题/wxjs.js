console.show();
log("等待6秒")
sleep(600)
log("开始")

var x;
var y;
events.onTouch(function (p) {
    if (i==1){
        i++;
        x=p.x;
        y=p.y;
        log("起点"+p.x+""+p.y);

    }
    else {
        i--;
        log("终点"+p.x+""+p.y);
        var lengh=Math.pow((p.x-x)*(p.x-x)+(p.y-y)*(p.y-y));
        log("跳跃距离"+lengh)
        var time=Math.round(lengh);
        w.setSize(1,1);
        sleep(300);

    }
})


