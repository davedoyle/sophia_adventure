# scenes/forest.py

import re
from utils.colours import colour_text

def scene():
    # 1) Opening narrative
    print(colour_text(
        "\nSophia hops out of bed, Bunny tucked under her arm.\n"
        "She’s brave as she walks across the field, stepping through giant daisies\n"
        "that smile and wave at her. The sun is bright and warm on her face.\n"
        "Soon, she reaches Forest Land, where the old wooden bridge awaits...\n",
        "yellow"
    ))

    # 2) Bridge Troll puzzle
    print(colour_text(
        "\nYou arrive at the old wooden bridge. The Bridge Troll blocks the way.\n"
        "He grumbles: \"If you want to pass, you must pay me exactly €1—no more, no less!\"\n",
        "yellow"
    ))
    print(colour_text(
        "\nYou have: 6×50c, 5×20c, 10×10c, and 20×5c coins.\n"
        "Which coins will you give the troll to make exactly €1?",
        "blue"
    ))

    # Get Sophia's answer
    user_raw = input(colour_text("\nYour coins: ", "green")).strip().lower()
    cents = re.findall(r'(\d+)\s*c', user_raw)
    total = sum(int(c) for c in cents)

    if total != 100:
        print(colour_text(f"\nYou gave {total}c, which is not €1. Try again!", "red"))
        return "forest_start"

    print(colour_text("\nCorrect! The troll grumbles and steps aside...", "blue"))

       # 3) Fairy encounter & name prompt
    print(colour_text(
        "\nAs you step onto the bridge, a giggle rings out like little bells.\n"
        "Sophia looks around—small birds flutter overhead, then a tiny fairy lands on a leaf.\n"
        "\"Waaaaaaa!\" Sophia startles.\n"
        "\"Who—who are you?\" she stammers.\n"
        "\"I am a fairy,\" the sprite replies. \"Nali is my name. What’s yours?\"\n",
        "yellow"
    ))
    name = input(colour_text("Your name: ", "green")).strip().title()
    print(colour_text(f"\n\"Wow, {name}, that’s a pretty name for a pretty girl,\" Nali beams.", "blue"))

    # 4) Teddy discovery & crossings reminder
    print(colour_text(
        "\nNali waves her wand—and suddenly a little teddy appears at Sophia’s feet!\n"
        "\"That’s mine!!\" Sophia cries.\n"
        "\"Really???\" Nali asks with a twinkle.\n"
        "\"I will give him back, but first will you help me?\"\n"
        "Nali explains: “We must cross the bridge four times, paying €1 each time.”\n",
        "yellow"
    ))

    # 5) Prepare inventory for four crossings
    inventory = {50: 4, 20: 5, 10: 10, 5: 20}
    crossings = 4


    # 6) Four crossings coin puzzle
    for i in range(1, crossings + 1):
        while True:
            raw = input(colour_text(f"\nCrossing {i} — your coins: ", "green")).lower()
            picked = [int(c) for c in re.findall(r"(\d+)\s*c", raw)]
            total = sum(picked)

            if total != 100:
                print(colour_text(f"You gave {total}c—not €1. Try again.", "red"))
                continue

            counts = {}
            for coin in picked:
                counts[coin] = counts.get(coin, 0) + 1

            too_many = [c for c, cnt in counts.items() if cnt > inventory.get(c, 0)]
            if too_many:
                cm = ", ".join(f"{counts[c]}×{c}c" for c in too_many)
                print(colour_text(f"You tried to use {cm}, but don’t have enough. Try again.", "red"))
                continue

            for c, cnt in counts.items():
                inventory[c] -= cnt

            print(colour_text(f"Correct for crossing {i}! The troll grumbles and steps aside...", "blue"))
            break

    # 7) Finish forest scene
    print(colour_text(
        "\nYou’ve paid the troll 4 times and rescued the little teddy!\n"
        "The bridge creaks open and you step through with Bunny by your side...",
        "blue"
    ))
    return "castle_start"
