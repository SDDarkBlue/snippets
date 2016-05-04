angular.module('myApp').directive('myCustomers', function() {
    return {
	controller: 'customersController',
	restrict: 'E',
	templateUrl: 'directives/templates/my-customer.html'
    };
});
