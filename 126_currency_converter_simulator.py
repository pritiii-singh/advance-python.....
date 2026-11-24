"""
Project 126: Currency Converter Simulator
Concepts: dictionaries, math calculations, formatting currencies, user selection.
"""
RATES_TO_USD = {
    "USD": 1.0,
    "EUR": 1.08,
    "GBP": 1.27,
    "JPY": 0.0065,
    "CAD": 0.74,
    "AUD": 0.65,
    "INR": 0.012
}

def convert(amount, from_curr, to_curr, fee_pct=0.5):
    usd_val = amount * RATES_TO_USD[from_curr]
    dest_val = usd_val / RATES_TO_USD[to_curr]
    fee = dest_val * (fee_pct / 100.0)
    final_amt = dest_val - fee
    return dest_val, fee, final_amt

def main():
    print("=== CURRENCY CONVERTER SIMULATOR ===")
    print("Available currencies: " + ", ".join(RATES_TO_USD.keys()))
    
    while True:
        from_c = input("\nConvert FROM currency (or 'q' to quit): ").strip().upper()
        if from_c == 'Q': break
        to_c = input("Convert TO currency: ").strip().upper()
        if from_c not in RATES_TO_USD or to_c not in RATES_TO_USD:
            print("Unsupported currency code.")
            continue
            
        amt = float(input(f"Enter amount in {from_c}: "))
        gross, fee, net = convert(amt, from_c, to_c)
        print(f"\n[EXCHANGE] {amt:.2f} {from_c} = {gross:.2f} {to_c}")
        print(f"Fee (0.5% spread): {fee:.2f} {to_c}")
        print(f"Net Received: {net:.2f} {to_c}")

if __name__ == "__main__":
    main()
