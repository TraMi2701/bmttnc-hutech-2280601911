class VigenereCipher:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_upper = self.alphabet.upper()
    
    def vigener_cipher(self, plain_text: str, key: str) -> str:
        encrypted_text = ""
        key_index = 0
        key = key.lower()
        
        for char in plain_text:
            if char.isalpha():
                # Get the shift value from the key
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char) - ord('a')
                
                if char.isupper():
                    # Handle uppercase letters
                    position = ord(char) - ord('A')
                    new_position = (position + key_shift) % 26
                    encrypted_text += chr(new_position + ord('A'))
                else:
                    # Handle lowercase letters
                    position = ord(char) - ord('a')
                    new_position = (position + key_shift) % 26
                    encrypted_text += chr(new_position + ord('a'))
                
                key_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                encrypted_text += char
                
        return encrypted_text
    
    def vigener_decipher(self, cipher_text: str, key: str) -> str:
        decrypted_text = ""
        key_index = 0
        key = key.lower()
        
        for char in cipher_text:
            if char.isalpha():
                # Get the shift value from the key
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char) - ord('a')
                
                if char.isupper():
                    # Handle uppercase letters
                    position = ord(char) - ord('A')
                    new_position = (position - key_shift) % 26
                    decrypted_text += chr(new_position + ord('A'))
                else:
                    # Handle lowercase letters
                    position = ord(char) - ord('a')
                    new_position = (position - key_shift) % 26
                    decrypted_text += chr(new_position + ord('a'))
                
                key_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                decrypted_text += char
                
        return decrypted_text