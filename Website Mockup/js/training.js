let images = ['img/SW4L.png', 'img/AC6.png'];
let buttons = ['img/button.png', 'img/button_clicked.png']

let index = 0;
let button_state = 0;

const imgElement = document.getElementById("bottomPicture");
const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");


class Timer {
    constructor(fn, t) {
        var timerObj = setInterval(fn, t);

        this.stop = function () {
            if (timerObj) {
                clearInterval(timerObj);
                timerObj = null;
            }
            return this;
        };

        this.start = function () {
            if (!timerObj) {
                this.stop();
                timerObj = setInterval(fn, t);
            }
            return this;
        };

        this.reset = function (newT = t) {
            t = newT;
            return this.stop().start();
        };
    }
}

function change() {
    imgElement.src = images[index];
    index == 1 ? index = 0 : index = 1;
    button_state == 1 ? button_state = 0 : button_state = 1;
    button_state == 0 ? button1.src = buttons[1] : button1.src = buttons[0];
    button_state == 0 ? button2.src = buttons[0] : button2.src = buttons[1];
}

var timer = new Timer(function() {change()}, 5000);

function switch1() {
    imgElement.src = 'img/SW4L.png';
    button_state = 0;
    button1.src = buttons[1];
    button2.src = buttons[0];
    index == 1 ? index = 0 : index = 1;
    timer.reset(5000);
}

function switch2() {
    imgElement.src = 'img/AC6.png';
    button_state = 1;
    button1.src = buttons[0];
    button2.src = buttons[1];
    index == 1 ? index = 0 : index = 1;
    timer.reset(5000);
}