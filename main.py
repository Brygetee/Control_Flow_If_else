"""
4. Control Flow (if/else, comparisons, logical operators)
What you should know: Make decisions in code using conditions.
 Practice Prompt: Ask the user if their fabric is stretchy or
 non-stretchy. If stretchy, suggest “Make leggings,” otherwise suggest
 “Make a tote bag.”

"""
def sewing_project():
    fabric = input("Is your fabric stretchy or non-stretch?(Type 'stretch' or 'non')\n").lower()
    if fabric == "stretch":
        print("Make leggings.")
    elif fabric == 'non':
        print("Make a tote bag")
    else:
        print("Please input a valid response")
        sewing_project()

sewing_project()
"""How to improve this code:
-create a while loop because recursion may cause stack overflow
Recursion: When a function calls itself.
stack overflow: An error that happens when too many function calls pile up in memory.
.strip() removes any extra spaces (or other whitespace) from the start and end of a string, w o this
may return as false
"""
while True:
    fabric = input("Is your fabric stretchy or non-stretchy?\n").strip().lower()

    if fabric == "stretchy":
        print("Make leggings.")
        break
    elif fabric == "non-stretchy":
        print("Make a tote bag.")
        break
    else:
        print("Invalid input. Please type 'stretchy' or 'non-stretchy'.")