from .alphabet import alphabet

class CaesarCipher:
    def __init__(self):
        self.alphabet = alphabet

    def encrypt_text(self, plain_text: str, key: int) -> str:
        encrypted_text = ""
        for char in plain_text:
            if char in self.alphabet:
                position = self.alphabet.index(char)
                new_position = (position + key) % len(self.alphabet)
                encrypted_text += self.alphabet[new_position]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt_text(self, cipher_text: str, key: int) -> str:
        return self.encrypt_text(cipher_text, -key) 