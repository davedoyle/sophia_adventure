# scenes/timehill.py

import re
from utils.colours import colour_text

ASCII_CLOCK = r"""  
                    `.
                _.'_____`._           
              .'.-'  12 `-.`.           
             /,' 11  .   1 `.\           
            // 10    |     2 \\          
           ::        |        ::         
           || 9      O---   3 ||         
           ::                 ;;         
            \\ 8           4 //          
             \`. 7       5 ,'/           
              '.`-.__6__.-'.'            
               ((-._____.-))             
               _))       ((_             
              '--'       '--' 
"""

# Pre-compute the normalized “correct” answers
_valid_norms = {
    re.sub(r'[^a-z0-9]', '', ans): True
    for ans in [
        "3 o'clock", "3 o clock", "3oclock",
        "three o'clock", "three o clock", "threeoclock"
    ]
}

def scene():
    print(colour_text(
        "\nYou arrive in Timehill Valley. A giant stone clock stands before you:\n",
        "yellow"
    ))
    print(colour_text(ASCII_CLOCK, "blue"))
    print(colour_text(
        "\nBunny asks: \"What time does this show?\"\n"
        "You may answer:\n"
        "- 3 o'clock (or whatever variant you like)\n",
        "yellow"
    ))

    user_raw = input(colour_text("Your answer: ", "green")).strip().lower()
    # normalize: strip out anything that's not a letter or digit
    user_norm = re.sub(r'[^a-z0-9]', '', user_raw)

    if _valid_norms.get(user_norm):
        print(colour_text("Spot on—well done!", "blue"))
        return None  # demo end
    else:
        print(colour_text(
            "Hmm, that doesn't match. Try again (no need for apostrophes or exact spacing).",
            "red"
        ))
        return "timehill_start"
