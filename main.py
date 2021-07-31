import os, sys, random
from datetime import datetime
platforms = {
    "darwin": "MacOS",
    "win32": "Windows32",
    "win64": "Windows64",
    "linux": "Linux",
}


def run_tool():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        command = input(f"[{current_time}] > ")
        if command == "os":
            print(f"Detected operating system: {platforms.get(sys.platform, 'Unknown OS')}")

        
        elif command == "clear":
            os.system("clear")
        
        elif "+" in command:
            nums = command.split("+")
            result = 0
            for x in nums:
                result += int(x)
            print(result)
        
        elif command == "games":
            print("""1. Guess the word
                     2. Rock paper scissor
                     3. Mad libs generator""")
            which = input("\nWhich game would you like to play? ")
            if which == "1":
                try:
                    with open("words.txt", "r") as file:
                        words = [word.strip() for word in file]
                    word_to_guess = random.choice(words)
                    guess = input(f"What word has a length of {len(word_to_guess)} characters, starts with {word_to_guess[0]} and ends with {word_to_guess[-1]}? ")
                    if guess != word_to_guess:
                        print(f"Incorrect. The word was {word_to_guess}.")
                    
                    else:
                        print("Correct!")

                except FileNotFoundError:
                    print("Can't find words.txt. Make sure it's in the same directory and not named something else.")

            elif which == "2":
                choices = ["rock", "paper", "scissor"]
                user_choice = input("Enter your choice: ").lower()
                computer_choice = random.choice(choices)
                if user_choice == computer_choice:
                    print("Tie.")
                elif user_choice == "rock" and computer_choice == "scissor":
                    print("Rock beats scissor. You win!")
                
                elif user_choice == "rock" and computer_choice == "paper":
                    print("Paper beats rock. Computer wins!")
                
                elif user_choice == "scissor" and computer_choice == "rock":
                    print("Rock beats scissor. Computer wins!")
                
                elif user_choice == "scissor" and computer_choice == "paper":
                    print("Scissor beats paper. You win!")
                
                elif user_choice == "paper" and computer_choice == "scissor":
                    print("Scissor beats paper. Computer wins!")
                
                elif user_choice == "paper" and computer_choice == "rock":
                    print("Paper beats rock. You win!")
            
                else:
                    print("Invalid choice.")
            
            elif which == "3":
                give_me_words = input("Enter 5 words: ").split()
                print(f"The {give_me_words[0]} was slimy, it tasted like {give_me_words[1]}. I stayed at {give_me_words[2]} place. He made me {give_me_words[3]} in the morning. We packed up at {give_me_words[4]}.")



        
        elif command == "quit":
            sys.exit()

        else:
            print(f'Unknown command: "{command}" ')

run_tool()
