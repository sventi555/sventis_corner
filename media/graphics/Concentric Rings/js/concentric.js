var sides = 20;
var connections = 5;
var circles = [];
var numCircs = 3;
var numPolygons = 15;

function windowResized() {
    resizeCanvas(document.getElementById('frame').offsetWidth, document.getElementById('frame').offsetHeight);
}

function setup() {
    canvas = createCanvas(document.getElementById('frame').offsetWidth, document.getElementById('frame').offsetHeight);
    canvas.parent('frame');
    colorMode(HSB, 255, 100, 100, 100);
    background(20);
    noStroke();
    for (var i = 0; i < numCircs; i++) {
        circles.push([]);
    }
    for (var i = 0; i < numCircs; i++) {
        for (var j = 0; j < numPolygons; j++) {
            circles[i].push(new Polygon(j, width / 5 - i * width / 15, i * 2 * PI / numCircs))
        }
    }
}

function draw() {
    background(20);
    translate(width / 2, height / 2);
    for (var i = 0; i < numCircs; i++) {
        for (var j = 0; j < numPolygons; j++) {
            circles[i][j].turn();
            circles[i][j].show();
        }
    }
}

function Polygon(layer_, radius_, rotation_) {
    this.layer = layer_;
    this.radius = radius_;
    this.colour = color((this.layer * 50) % 255, (this.layer * 8 + 50) % 100, 80, 20);
    this.rotation = rotation_;

    this.show = function () {
        fill(this.colour);
        push();
        rotate(this.rotation);
        beginShape();
        for (var i = 0; i < connections; i++) {
            vertex(this.radius * cos(i * 2 * PI / sides), this.radius * sin(i * 2 * PI / sides));
        }
        endShape(CLOSE);
        pop();
    }

    this.turn = function () {
        this.rotation += pow(-1, this.layer) * (0.001 * this.layer);
        if (this.rotation > 2 * PI) {
            this.rotation -= 2 * PI;
        }
    }
}
