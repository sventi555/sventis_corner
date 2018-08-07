let canvas;
let words;
let ship;
let enemies = [];
let currentEnemy;
let active = false;
let orang;
let space;


function preload() {
    words = loadStrings('words.txt');
    orang = loadImage('orang.png');
    space = loadImage('space.jpg');
}


function windowResized() {
    resizeCanvas(document.getElementById('frame').offsetWidth,
                 document.getElementById('frame').offsetHeight);
}


function setup() {
    canvas = createCanvas(document.getElementById('frame').offsetWidth,
                          document.getElementById('frame').offsetHeight);
    canvas.parent('frame');
    ship = new Ship();
}


function draw() {
    imageMode(CORNER);
    image(space, 0, 0, width, height);
    fill(255);
    ship.show();
    if (frameCount % 90 === 0) {
        enemies.push(new Enemy());
    }
    updateEnemies();
}


function keyTyped() {
    shoot();
}
