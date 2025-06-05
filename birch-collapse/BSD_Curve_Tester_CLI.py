
import sympy as sp
import matplotlib.pyplot as plt

def bsd_rank_test(curve_name="y^2 = x^3 - x", x_vals=None):
    print(f"Running BSD test for curve: {curve_name}")
    if x_vals is None:
        x_vals = list(range(-10, 11))

    x = sp.Symbol('x')
    expr = sp.sympify(curve_name.split('=')[1].strip())
    y_vals = []

    for val in x_vals:
        try:
            rhs = expr.subs(x, val)
            if rhs >= 0:
                y_val = sp.sqrt(rhs)
                y_vals.append(float(y_val))
            else:
                y_vals.append(None)
        except Exception as e:
            y_vals.append(None)

    valid_points = [(xv, y) for xv, y in zip(x_vals, y_vals) if y is not None]
    rank_estimate = len(valid_points)

    print(f"Estimated BSD rank (approximate): {rank_estimate}")
    print("Valid points on curve:", valid_points)

    if valid_points:
        x_plot, y_plot = zip(*valid_points)
        plt.scatter(x_plot, y_plot)
        plt.title(f"BSD Curve Test: {curve_name}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()

def menu():
    print("BSD Rank Tester - Symbolic Curve Tool")
    while True:
        print("\nOptions:")
        print("1. Run default BSD curve test")
        print("2. Input your own curve")
        print("3. Quit")

        choice = input("Select an option (1-3): ")
        if choice == '1':
            bsd_rank_test()
        elif choice == '2':
            user_curve = input("Enter curve in the form 'y^2 = ...': ")
            bsd_rank_test(curve_name=user_curve)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    menu()
