#!/usr/bin/python

# ARGS

"""
use the `*args` syntax in a function definition. It means you can
provide this function with an undefined number of arguments.
These arguments will be stored in the list `args`.
"""
def hello(name, *args):
    other_names = ', '.join(args)
    print 'Hello {0} and {1}'.format(name, other_names)

"""
'tony' will match `name` while the other arguments will be saved
in the args list
"""
hello('tony', 'helly', 'belly', 'merry')

# KWARGS
"""
kwargs works the same, but these are keyword arguments and a
slightly different syntax.
"""
def hello_kw(name, **kwargs):
    print 'Hello {0}'.format(name)
    print 'You have the following parameters:'
    for key, value in kwargs.iteritems():
        print '{0}: {1}'.format(key, value)

hello_kw('tony', length=184, weight=78, age=35)
