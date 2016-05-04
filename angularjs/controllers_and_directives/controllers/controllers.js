angular.module('myApp').controller('customersController', ['$scope', function($scope) {
    $scope.customers = [
	{ name: 'Naomi', address: '1600 Amphitheatre' },
	{ name: 'Igor', address: '123 Somewhere' }
    ]

    $scope.customAdd = function(x, y) {
	return x + y;
    };
}]);
