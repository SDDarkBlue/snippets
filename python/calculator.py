import re
expression = '(3 * (1 + 4) - 9) * (5 + (3 * (2 - 1)))'

def resolve_expr_without_brackets(expr):
    """ Resolve an expression that contains no brackets """
    return 'Hi!'

inner_brackets_found = True

while inner_brackets_found:
    m = re.search('\([^\(\)]+\)', expression)
    if m != None:
	# fetch a resolvable expression, and immediately drop its outer brackets
	expr_with_brackets = expression[m.start():m.end()]
	expr = expr_with_brackets[1:-2]
	result = resolve_expr_without_brackets(expr)
	expression = expression.replace(expr_with_brackets, result)
        print expression
    else:
	inner_brackets_found = False
	total_result = resolve_expr_without_brackets(expression)

print total_result
