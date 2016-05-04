$.fn.horizontalAccordeon = function (speed) {
    return this.each(function () {
	var $accordeonHeaders = $(this).find('h3'),
	    $open = $accordeonHeaders.next().filter(':first'),
	    width = $open.outerWidth();

	// initialize the display
	$accordeonHeaders.next().filter(':not(:first)').css({ display : 'none', width : 0 });
	$accordeonHeaders.click(function () {
	    if ($open.prev().get(0) == this) {
		return;
	    }
	    $open.animate({ width: 0}, { duration : speed });
	    $open = $(this).next().animate({ width: width }, {duration : speed });
	});
    });
};

$(document).ready(function () {
    $('#accordeonWrapper').horizontalAccordeon(200);
});
