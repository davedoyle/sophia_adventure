from utils.colours import colour_text

def scene():
    print(colour_text(
        "\nYou wake up in a misty field. Bunny is by your side, twitching his nose.\n"
        "In the grass you spot a shiny silver compass.\n\n"
        "\"Sophia,\" Bunny says. \"Which land shall we visit first?\"\n\n"
        "1) The Puzzle Treehouse  (spelling fun)\n"
        "2) Timehill Valley       (time puzzles)\n",
        "yellow"
    ))

    choice = input(colour_text("Your choice [1–2]: ", "green")).strip()
    if choice == "1":
        return "treehouse_start"
    elif choice == "2":
        return "timehill_start"
    else:
        print(colour_text("Oops—that’s not 1 or 2. Try again.", "red"))
        return "intro"
