
alphabets = [chr(i) for i in range(97, 123)]
print(alphabets)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift numbeer:\n").lower())

def encrypt(text, shift):
    # Encrypts text by shifting each letter by shift amount
    encrypted_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position + shift) % 26
            encrypted_text += alphabets[new_position]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, shift):
    # Decrypts text by shifting each letter back by shift amount
    decrypted_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position - shift) % 26
            # % 26 is the modulo operator that ensures the position stays within the alphabet range (0-25)
            # For example:
            # If position + shift = 27, then 27 % 26 = 1, wrapping back to 'b'
            # If position + shift = 28, then 28 % 26 = 2, wrapping back to 'c'
            # This allows the cipher to wrap around from 'z' back to 'a'            
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += letter
    return decrypted_text

if direction == "encode":
    result = encrypt(text, shift)
    print(f"The encoded text is {result}")
elif direction == "decode":
    result = decrypt(text, shift)
    print(f"The decoded text is {result}")