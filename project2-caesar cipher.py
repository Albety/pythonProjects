alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ''
    alphabet_length = len(alphabet)
    for letter in text:
        if letter in alphabet:
            alph_index = alphabet.index(letter)
            if (alph_index + shift) < alphabet_length:
                cipher_text += alphabet[alph_index + shift]
            else:
                cipher_text += alphabet[alph_index + shift - alphabet_length]
        else:
            cipher_text += letter
    print(f"Encoded text is {cipher_text}")

def decrypt(text, shift):
    decoded_text = ''
    for letter in text:
        if letter in alphabet:
            alph_index = alphabet.index(letter)
            decoded_text += alphabet[alph_index - shift]
        else:
            decoded_text += letter
    print(f"Decoded text is {decoded_text}")

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)







