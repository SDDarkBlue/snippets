describe("A suite", function() {
    it("contains spec with an expectation", function() {
        expect(true).toBe(true);
    });
});

describe("Hello World", function() {
    it("should return a string", function() {
        expect(HelloWorld()).toBe("Hello World!");
    });
});
