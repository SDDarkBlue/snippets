function addls(mymap) {
    alert("testf called with argument: " + mymap);
    mymap.addLayer('countries');
    alert('layer countries added');
}

$(document).ready(function () {
    alert('were going live');
    var map = Kartograph.map('#map', 400, 600);
    alert('map object created');
    map.loadMap('localhost/~bart_aelterman/kartograph-test/world.svg', function() {
        map.addLayer('countries');
    })
    alert('map loaded');
    //map.loadMap('/Users/bart_aelterman/test/kartograph/test-1/world.svg', function() {
     //   alert("function called");
      //  map.addLayer('countries');
    //});
});
