var Game = function() {
    var choices = ["rock", "scissors", "paper"];

    this.draw = function() {
        var randomIndex = Math.floor(Math.random() * 3);
        console.log(choices[randomIndex]);
        return choices[randomIndex];
    }

    this.playerDraw = function(input) {
        if (choices.indexOf(input) < 0) {
            throw("not a valid choice");
        }
        return true;
    }
}
