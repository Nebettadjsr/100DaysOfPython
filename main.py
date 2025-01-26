# A Caesar cipher is a simple encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet.
# For example, with a shift of 3, "A" becomes "D", "B" becomes "E", and so on, wrapping around at "Z".
# It was famously used by Julius Caesar to securely transmit military messages to his generals.


from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter.isalpha():
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}\n")


restart = True
while restart:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    reset= input("Do you want to en~ or decode something else?\nY/N? ").lower()
    if reset == "n":
        restart = False

