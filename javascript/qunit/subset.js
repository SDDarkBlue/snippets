function subset (array, subsKeys) {
    outArr = new Array();
    for (var i = 0; i < subsKeys.length ; i++) {
	key = subsKeys[i];
	console.log("key: " + key);
	for (var k = 0; k < array.length; k++) {
	    obj = array[k];
	    objKey = obj["key"];
	    if (objKey === key) {
		outArr.push(obj);
	    }
	}
    }
    console.log("out array: " + outArr);
    return outArr;
}
