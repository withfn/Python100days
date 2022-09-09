PLACEHOLDER = "[name]"

#Open list of names
with open("./input/Names/invited_names.txt", mode='r') as names:
    list_name = names.read().split('\n')

#Open the sample letter
with open("./input/Letters/starting_letter.txt", mode='r') as letter:
    sample_letter = letter.read()

#Create the letters
for name in list_name:
    new_letter = sample_letter.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as final_letter:
        final_letter.write(new_letter)
