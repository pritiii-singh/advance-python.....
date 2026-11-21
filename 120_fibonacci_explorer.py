"""
Project 120: Fibonacci Sequence & Golden Ratio Explorer
Concepts: recursion vs iteration, generator functions, golden ratio convergence.
"""
def fibonacci_iterative(n):
    seq = [0, 1]
    if n <= 0: return []
    if n == 1: return [0]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def main():
    print("=== FIBONACCI & GOLDEN RATIO EXPLORER ===")
    while True:
        print("\n1. Generate first N Fibonacci numbers")
        print("2. Explore Golden Ratio (Phi) approximation")
        print("3. Exit")
        c = input("Choice (1-3): ").strip()

        if c == "1":
            n = int(input("How many terms? (e.g., 15): "))
            seq = fibonacci_iterative(n)
            print(f"Sequence: {seq}")
        elif c == "2":
            n = int(input("Evaluate convergence up to term N (min 5): ") or 10)
            seq = fibonacci_iterative(max(5, n))
            print(f"\n{'Pair (F_n / F_{n-1})':<25} | {'Ratio':<10} | {'Error from Phi (1.6180339887)'}")
            print("-" * 65)
            phi = (1 + 5 ** 0.5) / 2
            for i in range(2, len(seq)):
                ratio = seq[i] / seq[i-1]
                err = abs(ratio - phi)
                print(f"{seq[i]} / {seq[i-1]:<15} | {ratio:.6f}   | {err:.8f}")
        elif c == "3":
            break

if __name__ == "__main__":
    main()
