function Enemy() {
    this.x = width;
    this.y = random(height);
    this.word = words[floor(random(words.length))];

    this.move = function() {
        dx = ship.x - this.x;
        dy = ship.y - this.y;
        dist = sqrt(pow(dx, 2), pow(dy, 2));
        this.x += dx*1.5/dist;
        this.y += dy*1.5/dist;
    }

    this.show = function() {
        fill(80);
        stroke('white');
        ellipse(this.x, this.y, textWidth(this.word)*1.5, 30);
        textAlign(CENTER, CENTER);
        textSize(18);
        fill(255);
        noStroke();
        text(this.word, this.x, this.y);
    }
}

function updateEnemies() {
    for (let enemy of enemies) {
        if ((abs(enemy.x - ship.x) < textWidth(enemy.word)/2 + 25) && (abs(enemy.y - ship.y) < 10)) {
            textSize(40);
            fill(255);
            noStroke();
            text("GAME OVER", width/2, height/2);
            noLoop();
            break;
        }
        enemy.move();
        enemy.show();
    }
}
