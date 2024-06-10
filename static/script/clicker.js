document.getElementById('coin').addEventListener('click', function() {
    increaseScore();
});

let score = 0;

function increaseScore() {
    score += 1;
    document.getElementById('score').textContent = 'Score: ' + score;
}
