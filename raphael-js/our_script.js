test_func = function () {
    var paper = new Raphael(document.getElementById('canvas_container'), 500, 500);
    for (var i = 0; i < 5 ; i+=1) {
	var multiplier = i*5;
	paper.circle(250 + (2*multiplier), 100 + multiplier, 50 - multiplier);
    }
    var tetronimo = paper.path("M 250 250 l 0 -50 l -50 0 l 0 -50 l -50 0 l 0 50 l -50 0 l 0 50 z");
    tetronimo.animate({transform:'r25,0,0'}, 1000);
    tetronimo.animate({  path: "M 250 250 l 0 -50 l -50 0 l 0 -50 l -100 0 l 0 50 l 50 0 l 0 50 z"  }, 2000, 'elastic');
    //tetronimo.attr(
     //   {
//	    'gradient': '90-#526c7a-#64a0c1',
//	    'stroke': '#3b44449',
//	    'stroke-width': 20,
//	    'stroke-linejoin': 'round',
//	    'rotation': -90
//	}
//    );
    var circ = paper.circle(250, 250, 40);  
    circ.attr({fill: '#000', stroke: 'none'}); 
    var text = paper.text(250, 250, 'Bye Bye Circle!')  
    text.attr({opacity: 0, 'font-size': 12}).toBack(); 
    circ.node.onmouseover = function() {  
	    this.style.cursor = 'pointer';  
    }
    circ.node.onclick = function() {  
	text.animate({opacity: 1}, 2000);  
	circ.animate({opacity: 0}, 2000, function() {  
	    this.remove();  
	});  
    }  

}


window.onload = test_func
