// The self invoking function does not exist. Nothing can be tested
test("try to access the app as self invoking function", function(assert) {
    assert.ok(typeof(appAsSelfInvokingFunction), "undefined");
});


// The module exposes some functions. These can be tested, others cannot
test("test run app", function(assert) {
    assert.ok(typeof(appAsModule), "object");
});

// Publicly exposed functions can be tested
test("test an exposed function", function(assert) {
    assert.ok(appAsModule.sayHi(), "Hello World!");
});

// Functions that are not exposed, cannot be tested
test("test an unexposed function will fail", function(assert) {
    assert.throws(appAsModule.foo);
});
