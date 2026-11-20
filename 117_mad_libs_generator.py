"""
Project 117: Mad Libs Story Generator
Concepts: string template replacement, user input collection, interactive narrative.
"""
import random

STORIES = [
    {
        "title": "Space Odyssey",
        "template": "Captain {name} launched the spaceship towards planet {planet}. Suddenly, a huge {creature} began {verb_ing} outside the ship! The crew used a {adjective} laser to defend themselves and ate {food} to celebrate.",
        "prompts": ["name", "planet", "creature", "verb_ing", "adjective", "food"]
    },
    {
        "title": "A Day at the Coding Bootcamp",
        "template": "Yesterday, {name} decided to learn {programming_language}. After drinking {number} cups of {beverage}, they discovered a {adjective} bug in their loop. In the end, they pushed code to {place} and shouted '{exclamation}'!",
        "prompts": ["name", "programming_language", "number", "beverage", "adjective", "place", "exclamation"]
    }
]

def main():
    print("=== MAD LIBS STORY GENERATOR ===")
    story = random.choice(STORIES)
    print(f"Theme: {story['title']}\nFill in the blanks:")

    answers = {}
    for p in story["prompts"]:
        label = p.replace("_", " ").capitalize()
        answers[p] = input(f"Enter a {label}: ").strip() or "something"

    completed = story["template"].format(**answers)
    print("\n" + "=" * 50)
    print(f"      {story['title'].upper()}      ")
    print("=" * 50)
    print(completed)
    print("=" * 50)

if __name__ == "__main__":
    main()
