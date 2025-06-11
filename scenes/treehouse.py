from utils.colours import colour_text

def scene():
    print(colour_text(
        "\nYou climb into the Puzzle Treehouse.\n"
        "A cheeky monkey drops a leaf with a scrambled word:\n\n"
        "   c s a e t l\n\n"
        "\"Can you unscramble it to form a land’s name?\" Bunny winks.\n",
        "yellow"
    ))

    answer = input(colour_text("Your answer: ", "green")).strip().lower()
    if answer == "castle":
        print(colour_text("Brilliant! That spells 'castle'.", "blue"))
        return None   # end this demo scene
    else:
        print(colour_text("Not quite—remember, no extra letters or reversals.", "red"))
        return "treehouse_start"
