describe("The rock scissors paper game", function() {
    it("has a game object", function() {
        g = new Game();
        expect(g).toBeDefined();
    });

    it("can draw rock, scissors or paper", function() {
        g = new Game();
        var draw = g.draw();
        var options = ["rock", "scissors", "paper"];
        expect(options.indexOf(draw)).toBeGreaterThan(-1);
    });

    it("lets you draw rock, scissors or paper", function() {
        g = new Game();
        expect(g.playerDraw("rock")).toBe(true);
        expect(g.playerDraw("scissors")).toBe(true);
        expect(g.playerDraw("paper")).toBe(true);
    });

    it("throws an error if you draw something else", function() {
        var errfunc = function() {
            g.playerDraw("knife");
        }
        expect(errfunc).toThrow("not a valid choice");
    });

});
