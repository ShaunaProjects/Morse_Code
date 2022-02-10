from art import logo

MORSE_DICT = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
              "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
              "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "&": ".-...", "'": ".----.",
              "@": ".--.-.", ")": "-.--.-", "(": "-.--.", ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--",
              ".": ".-.-.-", "-": "-....-", "×": "-..-", "%": "------..-.-----", "+": ".-.-.", "?": "..--..",
              "/": "..-.", " ": " "
              }

def morse_convert():
    message = input("Please type in the message you would like to convert to Morse code: ").upper()
    morse = [MORSE_DICT[char] for char in message]
    print(" ".join(morse))

run_program = True
print(logo)
print("Welcome to the Morse Code Generator!")
morse_convert()
while run_program:
    continue_program = input("Would you like to convert another message? Type Y or N: ").upper()
    if continue_program == "Y":
        morse_convert()
    elif continue_program == "N":
        print("Thank you for using the Morse Code Generator! Have a nice day.")
        run_program = False
    else:
        print("Sorry, that's not a valid input. Please try again.")
