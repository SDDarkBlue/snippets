// The first pattern is to implement your app as a
// self invoking function. This keeps everything hidden
// from the global scope, but the lack of a public
// API makes it impossible to test the app.
var appAsSelfInvokingFunction = function () {
    console.log("app as self invoking function is running");
}();


// The second pattern uses the module design pattern.
// Here, the app itself becomes a kind of factory
// that creates an object and returns it. The properties
// of this object are accessible from the public scope
// so this pattern allows you to expose parts of your
// app and hence create a public API which can be
// tested.
var appAsModule = function () {
    console.log("app as a module is running");
    var sayHi = function () {
        return "Hello World!";
    };

    var a = {
        sayHi: sayHi
    };

    return a;
}();
