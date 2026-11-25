"""
Project 127: Trivia Quiz Bowl
Concepts: list of nested dictionaries, enumeration, scoring metrics, grade calculation.
"""
QUESTIONS = [
    {
        "q": "What is the capital of Japan?",
        "options": ["Kyoto", "Tokyo", "Osaka", "Hiroshima"],
        "answer": 2
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": 2
    },
    {
        "q": "Who developed the Python programming language?",
        "options": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"],
        "answer": 1
    },
    {
        "q": "What is the powerhouse of the cell?",
        "options": ["Ribosome", "Nucleus", "Mitochondria", "Golgi apparatus"],
        "answer": 3
    },
    {
        "q": "What is the boiling point of water at standard sea level in Celsius?",
        "options": ["90°C", "95°C", "100°C", "110°C"],
        "answer": 3
    }
]

def main():
    print("=== WELCOME TO TRIVIA QUIZ BOWL ===")
    score = 0
    for idx, item in enumerate(QUESTIONS, 1):
        print(f"\nQuestion {idx}: {item['q']}")
        for opt_idx, opt in enumerate(item['options'], 1):
            print(f"  {opt_idx}. {opt}")
        ans = input("Your answer (1-4): ").strip()
        if ans.isdigit() and int(ans) == item["answer"]:
            print("[OK] Correct!")
            score += 1
        else:
            correct_opt = item['options'][item['answer'] - 1]
            print(f"[X] Wrong! Correct answer was: {correct_opt}")

    total = len(QUESTIONS)
    pct = (score / total) * 100
    print(f"\nFinal Score: {score}/{total} ({pct:.1f}%)")
    if pct >= 80: print("Rating: Outstanding!")
    elif pct >= 60: print("Rating: Good Job!")
    else: print("Rating: Keep practicing!")

if __name__ == "__main__":
    main()
