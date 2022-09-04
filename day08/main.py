from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    shift = shift % 26
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            end_text += letter
            continue
        
        if (alphabet.index(letter) + shift) >= (len(alphabet)):
            temp_index = (alphabet.index(letter) + shift) - (len(alphabet))
            end_text += alphabet[temp_index]
        else:
            end_text += alphabet[alphabet.index(letter) + shift]
    print(f"Here's the {direction}d result: {end_text}")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    
    again = input("You want go again? type 'yes' or 'no'\n").lower()
    if again == 'no':
        break