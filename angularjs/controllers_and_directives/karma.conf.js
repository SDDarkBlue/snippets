module.exports = function(config) {
    config.set({
	basePath: '.',
	frameworks: ['jasmine'],
	files: [
	    'bower_components/angular/angular.js',
            'app.js',
            'controllers/controllers.js',
            'tests/example_test.js'
	]
    })
}
