'''
Before we jump into security concepts, let us familiarize ourselves with the mathematical background required for it.

Set X is a collection of elements. Here, X={1, 2, 3} is one such example. A collection of integers is also a set.

Given two sets, X and Y, we define a function f that maps every element in X to precisely element in Y.

If X={1, 2, 3} and Y={a, b, c}, the function f will return:

f(1)=a, f(2)=b and f(3)=c.

Let us define a function f1(x)=x<r>, where x in X and x<r> in Y.
Here, x<r> is defined as the remainder of x when divided by 11.

Your task is to complete the function that takes the input x and returns x<r>

Constraints
1<=x<=1000
'''

# Complete the function below.


def  function( x):
    return x%11
