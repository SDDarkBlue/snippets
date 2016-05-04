angular.module('sphere1', [])
    .controller('SphereController', function() {
        this.radius;
        this.currentCircle = 1;

        this.circles = circles;

        this.setCurrent = function(val) {
            this.currentCircle = val;
            console.log(val);
        }

        this.isCurrent = function(val) {
            return val == this.currentCircle;
        }

        this.getradius = function() {
            return this.radius;
        }

        this.drawCircles = function() {
            var svg = d3.select("svg");
            dataarr = this.circles.map(function(x) {return x.radius})
            var circle = svg.selectAll("circle").data(dataarr);
            circle.enter().append("circle");
            circle.attr("cy", 60);
            circle.attr("cx", function(d, i) {return i * 100 + 30; });
            circle.attr("r", function(d) {return d;});
        };
    });

var circles = [
{
    "radius": 10,
    "nr": 1
},
{
    "radius": 16,
    "nr": 2
},
{
    "radius": 5,
    "nr": 3
}
];
