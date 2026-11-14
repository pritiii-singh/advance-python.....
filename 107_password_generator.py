"""
Project 107: Secure Password Generator & Strength Checker
Concepts: string module, random.SystemRandom, character sets, entropy calculation.
"""
import string
import secrets
import math

def calculate_entropy(pwd):
    charset = 0
    if any(c in string.ascii_lowercase for c in pwd): charset += 26
    if any(c in string.ascii_uppercase for c in pwd): charset += 26
    if any(c in string.digits for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += len(string.punctuation)
    if charset == 0: return 0
    return len(pwd) * math.log2(charset)

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    req = [secrets.choice(string.ascii_lowercase)]
    if use_upper:
        chars += string.ascii_uppercase
        req.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        req.append(secrets.choice(string.digits))
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        req.append(secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))

    remaining = length - len(req)
    if remaining > 0:
        req.extend(secrets.choice(chars) for _ in range(remaining))
    secrets.SystemRandom().shuffle(req)
    return "".join(req)

def main():
    print("=== PASSWORD GENERATOR & STRENGTH CHECKER ===")
    length = int(input("Enter password length (minimum 6, default 16): ") or 16)
    use_upper = input("Include uppercase? (y/n, default y): ").strip().lower() != 'n'
    use_digits = input("Include digits? (y/n, default y): ").strip().lower() != 'n'
    use_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != 'n'

    password = generate_password(max(6, length), use_upper, use_digits, use_symbols)
    entropy = calculate_entropy(password)

    strength = "Weak"
    if entropy >= 65: strength = "Very Strong"
    elif entropy >= 50: strength = "Strong"
    elif entropy >= 36: strength = "Moderate"

    print(f"\nGenerated Password: {password}")
    print(f"Entropy: {entropy:.1f} bits | Rating: {strength}")

if __name__ == "__main__":
    main()
