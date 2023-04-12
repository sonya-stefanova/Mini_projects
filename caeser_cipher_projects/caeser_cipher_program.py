alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet*=2

def caesar(start_text, shift_amount, cipher_instruction):
    end_text = ""
    if cipher_instruction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_instruction}d result: {end_text}")


from caeser_cipher_art import logo
print(logo)

game_over = False
while not game_over:
    instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Please, type your message:\n").lower()
    shift = int(input("Please, type the shift number:\n"))
    shift = shift % 26 #in case the user enters a shift that is greater than the number of letters in the alphabet, we can use the modulus so we can find the remainder
    #calling the function:
    caesar(start_text=text, shift_amount=shift, cipher_instruction=instruction)
    play_again_request = input("Do you want to play again? Type 'yes' if you want to restart the game or 'no' to stop it.\n")
    if play_again_request == "no":
        game_over = True
        print("Goodbye")
