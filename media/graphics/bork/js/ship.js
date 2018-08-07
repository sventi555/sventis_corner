function Ship() {
    this.x = 50;
    this.y = height/2;

    this.show = function() {
        imageMode(CENTER, CENTER);
        image(orang, 50, height/2, 80, 80);
    }
}

function shoot() {
    if (!active) {
        for (let i = 0; i < enemies.length; i++) {
            enemy = enemies[i];
            word = enemy.word
            if (key === word[0]) {
                active = true;
                currentEnemy = i;
                enemy.word = word.substring(1, word.length);
                if (enemy.word.length === 0) {
                    active = false;
                    enemies.splice(currentEnemy, 1);
                    currentEnemy = null;
                }
                break;
            }
        }
    } else if (active) {
        enemy = enemies[currentEnemy];
        word = enemy.word;
        if (key === word[0]) {
            enemy.word = word.substring(1, word.length);
            if (enemy.word.length === 0) {
                active = false;
                enemies.splice(currentEnemy, 1);
                currentEnemy = null;
            }
        }
    }
}
