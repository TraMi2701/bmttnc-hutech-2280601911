class CaesarCipher:
    def encrypt_text(self, plain_text, key):
        result = ''
        for char in plain_text:
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                result += char
        return result

    def decrypt_text(self, cipher_text, key):
        result = ''
        for char in cipher_text:
            if char.isupper():
                result += chr((ord(char) - 65 - key) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 - key) % 26 + 97)
            else:
                result += char
        return result
