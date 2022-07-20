"""
Comment
"""
def run():
    print("This function runs the program")
    phrase = "This is a phrase as a string"
    phrase = phrase.upper().lower().capitalize()
    #phrase = phrase.replace("","=)")
    phrase = phrase[:: -1]
    print(phrase)

if __name__ == "__main__":
    run()