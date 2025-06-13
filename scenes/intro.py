# scenes/intro.py

from utils.colours import colour_text

# valid keywords for each comprehension question
_WAKE_KEYWORDS   = ("field", "grass", "flower")
_TEDDIES        = {"snowy", "trunkles", "binky", "teddy"}
_LANDS_KEYWORDS = ("forest", "castle", "snow", "time")

def scene():
    # 1) Story
    print(colour_text(
        "\nYou were asleep when a loud POP echoed in your bedroom…\n"
        "You open your eyes and see your bed sitting in a field of green grass and flowers.\n"
        "Bunny is beside you, blinking.\n"
        "“Where are my teddies?!” you shout.\n\n"
        "Suddenly, Bunny’s ears perk up:\n"
        "“I know this world, Sophia. It’s the Land of Four Lands:\n"
        "  • Forest Land\n"
        "  • Castle Land\n"
        "  • Snow Land\n"
        "  • Time Land\n\n"
        "But your four teddies—Snowy the dog, Trunkles the elephant,\n"
        "Binky the penguin, and Teddy—are missing!\n"
        "You must be brave and clever to rescue them.”\n",
        "yellow"
    ))

    # 2) Q1: Where did Sophia wake up?
    ans1 = input(colour_text("1) Where did Sophia wake up? ", "green")).strip().lower()
    if not any(k in ans1 for k in _WAKE_KEYWORDS):
        print(colour_text(
            "Oops—that’s not right. Remember, she woke up in a field of green grass and flowers.",
            "red"
        ))
        return "intro"

    # 3) Q2: What teddy was missing? (name one)
    ans2 = input(colour_text("2) Name one of the missing teddies: ", "green")).strip().lower()
    if ans2 not in _TEDDIES:
        print(colour_text(
            f"Nope—that’s not one of them. Try again! (Snowy, Trunkles, Binky, or Teddy.)",
            "red"
        ))
        return "intro"

    # 4) Q3: Name one of the four lands
    ans3 = input(colour_text("3) Name one of the four lands Bunny mentioned: ", "green")).strip().lower()
    if not any(k in ans3 for k in _LANDS_KEYWORDS):
        print(colour_text(
            "That doesn’t match any of the lands. (Forest, Castle, Snow, or Time.)",
            "red"
        ))
        return "intro"

    # 5) Success! Let her choose which land to visit
    print(colour_text("\nBrilliant—let’s go rescue your teddies!", "blue"))
    print(colour_text(
        "\nWhich land will you explore first?\n"
        "1) Forest Land   (the Bridge Troll’s coin puzzle)\n"
        "2) Castle Land   (the Stone Wall’s number lock)\n"
        "3) Snow Land     (the Skeleton’s hangman trap)\n"
        "4) Time Land     (Captain Clockhand’s clock puzzles)\n",
        "yellow"
    ))

    choice = input(colour_text("Your choice [1–4]: ", "green")).strip()
    if choice == "1":
        return "forest_start"
    if choice == "2":
        return "castle_start"
    if choice == "3":
        return "snow_start"
    if choice == "4":
        return "timehill_start"

    print(colour_text("Please enter 1, 2, 3, or 4.", "red"))
    return "intro"
