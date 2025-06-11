from .alphabet import alphabet

class CaesarCipher:
    def __init__(self):
        self.alphabet = alphabet
        self.alphabet_upper = alphabet.upper()

    def encrypt_text(self, plain_text: str, key: int) -> str:
        if not isinstance(key, int):
            raise ValueError("Key must be an integer")
            
        encrypted_text = ""
        for char in plain_text:
            if char in self.alphabet:  # lowercase
                position = self.alphabet.index(char)
                new_position = (position + key) % len(self.alphabet)
                encrypted_text += self.alphabet[new_position]
            elif char in self.alphabet_upper:  # uppercase
                position = self.alphabet_upper.index(char)
                new_position = (position + key) % len(self.alphabet)
                encrypted_text += self.alphabet_upper[new_position]
            else:  # spaces and special characters
                encrypted_text += char
        return encrypted_text

    def decrypt_text(self, cipher_text: str, key: int) -> str:
        return self.encrypt_text(cipher_text, -key) 