function show_mood() {
    for (var i = 0; i < my_mood; i += 1) {
	(function (i) {
	    setTimeout(function () {
		paper.circle(250, 250, 20).attr({
		    stroke: 'none';
		    fill: colors[my_mood - 1]
		}).animate({translation: '0' + (-42 * (i+1))}, 2000, 'bounce').toBack();
	    }, 50*i)
	})(i);
    }
    paper.text(250, 300, moods[my_mood - 1]).attr({fill: colors[my_mood - 1]});

    mood_text.node.onclick = function () {
	return false;
    };
    circ.node.onclick = function () {
	return false;
    };
}

mood_meter = function () {
    var paper = new Raphael(document.getElementById('canvas_container'), 500, 500);
    var circ = paper.circle(250, 250, 20).attr({fill: '#000'});
    var mood_text = paper.text(250, 250, 'My\nmood').attr({fill: '#fff'});
    moods = ['Rubbish', 'Not ok', 'OK', 'Smiley', 'Positively manic'];
    colors = ['#cc0000', '#a97e22', '#9f9136', '#7c9a2d', '#3a9a2d'];
    var my_mood = 1;
    circ.node.onclick = show_mood;
    mood_text.node.onclick = show_mood;
}

window.onload = mood_meter
