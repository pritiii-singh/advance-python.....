"""
Project 103: All-in-One Unit Converter
Concepts: dictionary dispatch, numeric operations, float formatting, user menus.
"""
def convert_length(val, from_u, to_u):
    to_meters = {"m": 1.0, "km": 1000.0, "mi": 1609.344, "ft": 0.3048, "in": 0.0254}
    return (val * to_meters[from_u]) / to_meters[to_u]

def convert_weight(val, from_u, to_u):
    to_grams = {"g": 1.0, "kg": 1000.0, "lb": 453.59237, "oz": 28.3495}
    return (val * to_grams[from_u]) / to_grams[to_u]

def convert_temp(val, from_u, to_u):
    if from_u == "c": c = val
    elif from_u == "f": c = (val - 32.0) * (5.0 / 9.0)
    elif from_u == "k": c = val - 273.15
    else: return None
        
    if to_u == "c": return c
    elif to_u == "f": return (c * 9.0 / 5.0) + 32.0
    elif to_u == "k": return c + 273.15

def main():
    while True:
        print("\n" + "=" * 40)
        print("         ALL-IN-ONE UNIT CONVERTER      ")
        print("=" * 40)
        print("1. Length (m, km, mi, ft, in)")
        print("2. Weight (g, kg, lb, oz)")
        print("3. Temperature (C, F, K)")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "4":
            print("Goodbye!")
            break
            
        val_str = input("Enter value to convert: ").strip()
        try:
            val = float(val_str)
        except ValueError:
            print("Invalid numeric value.")
            continue
            
        if choice == "1":
            units = ["m", "km", "mi", "ft", "in"]
            from_u = input(f"From unit ({', '.join(units)}): ").strip().lower()
            to_u = input(f"To unit ({', '.join(units)}): ").strip().lower()
            if from_u in units and to_u in units:
                res = convert_length(val, from_u, to_u)
                print(f"-> {val} {from_u} = {res:.4f} {to_u}")
            else:
                print("Invalid unit selection.")
        elif choice == "2":
            units = ["g", "kg", "lb", "oz"]
            from_u = input(f"From unit ({', '.join(units)}): ").strip().lower()
            to_u = input(f"To unit ({', '.join(units)}): ").strip().lower()
            if from_u in units and to_u in units:
                res = convert_weight(val, from_u, to_u)
                print(f"-> {val} {from_u} = {res:.4f} {to_u}")
            else:
                print("Invalid unit selection.")
        elif choice == "3":
            units = ["c", "f", "k"]
            from_u = input(f"From unit (C, F, K): ").strip().lower()
            to_u = input(f"To unit (C, F, K): ").strip().lower()
            if from_u in units and to_u in units:
                res = convert_temp(val, from_u, to_u)
                print(f"-> {val} {from_u.upper()} = {res:.2f} {to_u.upper()}")
            else:
                print("Invalid unit selection.")

if __name__ == "__main__":
    main()
