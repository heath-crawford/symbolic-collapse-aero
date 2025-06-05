
import argparse
from sympy import symbols, simplify
from mpmath import mp

def calculate_ap(a, b, p):
    total = 0
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        is_quadratic_residue = pow(rhs, (p - 1) // 2, p) == 1 if rhs != 0 else False
        if rhs == 0 or is_quadratic_residue:
            total += 1
    return p + 1 - total

def L_function(a, b, s_val, num_terms=100):
    total = 1.0
    for p in range(2, 2 + num_terms):
        if all(p % d != 0 for d in range(2, int(p**0.5)+1)):
            ap = calculate_ap(a, b, p)
            term = 1 - ap * p**(-s_val) + p**(1 - 2 * s_val)
            if term == 0:
                continue
            total *= 1 / term
    return total

def main(a, b):
    print("Estimating L(E, s) near s = 1...")
    mp.dps = 25
    s_values = [1 - 10**-i for i in range(1, 6)]
    for s in s_values:
        value = L_function(a, b, s)
        print(f"L(E, s) at s = {s:.5f} ≈ {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BSD Curve Tester CLI")
    parser.add_argument("--a", type=int, required=True, help="Coefficient a")
    parser.add_argument("--b", type=int, required=True, help="Coefficient b")
    args = parser.parse_args()

    main(args.a, args.b)
