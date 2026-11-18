"""
Project 113: CLI Calculator with Calculation History
Concepts: arithmetic parsing, try/except error catching, list logs, user REPL.
"""
import math

def calculate(expr):
    allowed_names = {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "pi": math.pi, "pow": pow}
    # Secure evaluation using restricted namespace
    return eval(expr, {"__builtins__": {}}, allowed_names)

def main():
    history = []
    print("=== REPL CALCULATOR WITH HISTORY ===")
    print("Supports standard math (+, -, *, /, %, **) and funcs: sqrt(), sin(), cos()")
    print("Type 'history' to review, 'clear' to reset, 'quit' to exit.\n")

    while True:
        expr = input("calc > ").strip()
        if not expr:
            continue
        if expr.lower() == "quit":
            break
        if expr.lower() == "history":
            print("\n--- Calculation History ---")
            for idx, item in enumerate(history, 1):
                print(f"{idx}: {item}")
            print("---------------------------")
            continue
        if expr.lower() == "clear":
            history.clear()
            print("History cleared.")
            continue

        try:
            val = calculate(expr)
            record = f"{expr} = {val}"
            history.append(record)
            print(f"=> {val}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
