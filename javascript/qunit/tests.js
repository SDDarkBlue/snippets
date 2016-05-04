test("hello test", function() {
    ok( 1 == "1", "Passed!");
});
test("subset", function() {
    array = [{"key": "one", "value": 1}, {"key": "two", "value": 2}, {"key": "three", "value": 3}],
    subs_keys = ["one", "three"]
    subs_array = [{"key": "one", "value": 1}, {"key": "three", "value": 3}],
    deepEqual(subset(array, subs_keys), subs_array);
});
