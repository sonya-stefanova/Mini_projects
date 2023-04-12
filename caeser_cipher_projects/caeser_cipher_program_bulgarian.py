alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ю', 'я']
alphabet *=2
def caesar(start_text, shift_amount, cipher_instruction):
    end_text = ""
    if cipher_instruction == "разшифрирай":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Ето го и крайният резултат: {end_text}")


from caeser_cipher_art import logo
print(logo)

game_over = False
while not game_over:
    instruction = input("Моля, напиши 'дешифрирай' или 'разшифрирай':\n")
    text = input("Моля, напиши съобщението, което желаеш да дешифрираш или разшифрираш на български:\n").lower()
    shift = int(input("С каква стъпка желаеш да бъде видоизменено съобщението:\n"))
    shift = shift % 30 #in case the user enters a shift that is greater than the number of letters in the alphabet, we can use the modulus so we can find the remainder
    #calling the function:
    caesar(start_text=text, shift_amount=shift, cipher_instruction=instruction)
    play_again_request = input("Желаеш ли да продължиш да играеш?.\n")
    if play_again_request == "не":
        game_over = True
        print("Довиждане")
