"""CLI interface for newton_raphson_zero project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import sympy as sp

def newtonsMethod(x_guess, func, func_derivative, max_iter = 100, tol = 1e-4):
    x = x_guess
    print("n\tXn\t\t\t\tf(Xn)\t\t\t\tf'(Xn)\t\t\t\tf(Xn)/f'(Xn)\t\t\t\tXn - f(Xn)/f'(Xn)")
    for i in range(1, max_iter + 1):
        f = func.subs('x', x)
        f_prime = func_derivative.subs('x', x)
        m = f/f_prime
        x_new = x - m
        if abs(x_new - x) < tol: # y=0 is the accurate answer; if output of func is within tol, that means we get the correct answer
            return x, i - 1
        print(f"{i}\t{x}\t\t{f}\t\t{f_prime}\t\t{m}\t\t\t{x_new}")
        x = x_new
    return None, max_iter

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return sp.sympify(user_input)
        except sp.SympifyError:
            print("Invalid input. Please try again.")

def main():
    # Convert the string to a SymPy expression
    func = get_valid_input("f(x): ")
    func_derivative = get_valid_input("f'(x): ")
    x_guess = float(input("Initial guess of x: "))
    result, num_iter = newtonsMethod(x_guess=x_guess, func=func, func_derivative=func_derivative)
    print(f"Get the result: {result} in {num_iter} iterations.")
