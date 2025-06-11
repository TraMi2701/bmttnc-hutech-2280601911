class PlayFairCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    def create_playfair_matrix(self, key: str) -> list:
        # Remove J and convert to uppercase
        key = key.replace("J", "I").upper()
        
        # Create matrix with key first, then remaining letters
        matrix = []
        used_chars = set()
        
        # Add key characters
        for char in key:
            if char not in used_chars and char in self.alphabet:
                matrix.append(char)
                used_chars.add(char)
        
        # Add remaining alphabet characters
        for char in self.alphabet:
            if char not in used_chars:
                matrix.append(char)
                used_chars.add(char)
        
        # Convert to 5x5 matrix
        return [matrix[i:i+5] for i in range(0, 25, 5)]
    
    def find_letter_coords(self, matrix: list, letter: str) -> tuple:
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None
    
    def playfair_cipher(self, plain_text: str, matrix: list) -> str:
        # Prepare text
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""
        
        # Process text in pairs
        i = 0
        while i < len(plain_text):
            # Get first character
            char1 = plain_text[i]
            
            # Get second character or add padding
            if i + 1 < len(plain_text):
                char2 = plain_text[i + 1]
                if char1 == char2:
                    char2 = 'X'
                    i += 1
                else:
                    i += 2
            else:
                char2 = 'X'
                i += 1
            
            # Find coordinates
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)
            
            # Encrypt based on position
            if row1 == row2:  # Same row
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        
        return encrypted_text
    
    def playfair_decipher(self, cipher_text: str, matrix: list) -> str:
        # Prepare text
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        # Process text in pairs
        for i in range(0, len(cipher_text), 2):
            char1 = cipher_text[i]
            char2 = cipher_text[i + 1]
            
            # Find coordinates
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)
            
            # Decrypt based on position
            if row1 == row2:  # Same row
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]
        
        # Remove padding X if it's the last character
        if decrypted_text and decrypted_text[-1] == 'X':
            decrypted_text = decrypted_text[:-1]
            
        return decrypted_text