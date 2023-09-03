#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

def main() -> None:
    names_file = "./Input/Names/invited_names.txt"
    letter_file = "./Input/Letters/starting_letter.txt"
    output_dir = "./Output/ReadyToSend"

    with open(names_file) as names:
        names_list = names.readlines()

    with open(letter_file) as letter:
        letter_content = letter.read()

    for name in names_list:
        stripped_name = name.rstrip()
        new_letter = letter_content.replace("[name]", stripped_name)
        output_file = os.path.join(output_dir, f"letter_for_{stripped_name}.txt")
        with open(output_file, mode="w") as new_letter_file:
            new_letter_file.write(new_letter)
            print(f"Letter for {stripped_name} created.")

if __name__ == "__main__":
    main()