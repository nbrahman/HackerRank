'''
We now understand the definition of functions.

If f(x)=y, where x in X and y in Y then y is called an image of x, and x is called the preimage of y.

Given x<1>,x<2> in X and y<1>,y<2> in Y,
f(x<1>)=y<1> and f(x<2>)=y<2>

We call the function f: X -> Y as 1-1(one-to-one) if:
f(x<1>)=f(x<2>) =>x<1>=x<2>

Let us define a particular one-to-one function as f2:X-> X, such that f2(x)=x^2
where X={1, 2, 3, 4,...}.

The function defined in the previous challenge is not one-to-one because:
f1(0)=f1(11)=0,0!=11
Your task is to complete the function that takes x as the input and return x^2.

Constraints
1<=x<=1000
'''

# Complete the function below.


def  function( x):
    return x**2
