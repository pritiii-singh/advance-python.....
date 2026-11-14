"""
Project 108: Text-Based Dungeon Adventure
Concepts: object state, functions, while loops, inventory management, combat mechanics.
"""
import random

def play_game():
    player = {"health": 100, "attack": 15, "inventory": ["torch", "small health potion"]}
    print("=== THE FORGOTTEN CATACOMBS ===")
    print("You enter a dark dungeon with stone corridors.")

    step = 0
    while player["health"] > 0 and step < 5:
        step += 1
        print(f"\n[Chamber {step}/5] Player HP: {player['health']} | Inventory: {', '.join(player['inventory'])}")
        action = input("Do you want to (1) Proceed forward, (2) Search room, (3) Use potion?: ").strip()

        if action == "3":
            if "small health potion" in player["inventory"]:
                player["health"] = min(100, player["health"] + 30)
                player["inventory"].remove("small health potion")
                print(f"You drank the potion! Health restored to {player['health']}.")
            else:
                print("No potions in inventory.")
            continue

        if action == "2":
            loot = random.choice(["gold coins", "small health potion", "iron dagger", None])
            if loot:
                print(f"[FIND] You found a {loot}!")
                player["inventory"].append(loot)
                if loot == "iron dagger": player["attack"] += 10
            else:
                print("You found nothing but cobwebs.")

        # Encounter
        if random.random() < 0.65:
            monster_name = "Goblin" if step < 3 else "Orc Brute"
            monster_hp = 30 if monster_name == "Goblin" else 55
            monster_atk = 10 if monster_name == "Goblin" else 18
            print(f"[BATTLE] An aggressive {monster_name} appears! (HP: {monster_hp})")

            while monster_hp > 0 and player["health"] > 0:
                choice = input("(A)ttack or (F)lee?: ").strip().lower()
                if choice == "f":
                    dmg = random.randint(5, 10)
                    player["health"] -= dmg
                    print(f"You fled but took {dmg} damage in escape!")
                    break
                else:
                    dmg = player["attack"] + random.randint(-3, 3)
                    monster_hp -= dmg
                    print(f"You struck {monster_name} for {dmg} damage!")
                    if monster_hp <= 0:
                        print(f"You defeated the {monster_name}!")
                        break
                    m_dmg = monster_atk + random.randint(-2, 2)
                    player["health"] -= m_dmg
                    print(f"{monster_name} hit you for {m_dmg} damage! (Your HP: {player['health']})")

    if player["health"] > 0:
        print("\n[WINNER] YOU SURVIVED AND ESCAPED WITH GLORY & LOOT!")
    else:
        print("\n[GAME OVER] You succumbed to the darkness of the catacombs.")

if __name__ == "__main__":
    play_game()
