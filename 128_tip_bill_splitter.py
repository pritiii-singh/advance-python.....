"""
Project 128: Tip & Bill Splitter with Receipt
Concepts: formatted strings, monetary arithmetic, user prompts, receipt generation.
"""
def main():
    print("=== RESTAURANT BILL & TIP SPLITTER ===")
    bill_subtotal = float(input("Enter bill subtotal ($): "))
    tax_percent = float(input("Enter tax percentage (e.g., 8.5): ") or 0)
    tip_percent = float(input("Enter tip percentage (e.g., 15, 18, 20): ") or 15)
    num_people = int(input("Number of people splitting the bill: ") or 1)

    tax_amount = bill_subtotal * (tax_percent / 100.0)
    tip_amount = bill_subtotal * (tip_percent / 100.0)
    total_bill = bill_subtotal + tax_amount + tip_amount
    per_person = total_bill / max(1, num_people)

    print("\n" + "=" * 40)
    print("             ITEMIZED RECEIPT           ")
    print("=" * 40)
    print(f"Subtotal:                 ${bill_subtotal:>8.2f}")
    print(f"Tax ({tax_percent:>4.1f}%):              ${tax_amount:>8.2f}")
    print(f"Tip ({tip_percent:>4.1f}%):              ${tip_amount:>8.2f}")
    print("-" * 40)
    print(f"Total Amount:             ${total_bill:>8.2f}")
    print(f"People Sharing:           {num_people:>8d}")
    print(f"Amount Per Person:        ${per_person:>8.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
