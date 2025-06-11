class RailFenceCipher:
    def __init__(self):
        pass
    
    def railfence_cipher(self, plain_text: str, num_rails: int) -> str:
        if num_rails < 2:
            raise ValueError("Number of rails must be at least 2")
            
        # Create empty rails
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1 for down, -1 for up
        
        # Fill the rails
        for char in plain_text:
            rails[rail_index].append(char)
            
            # Change direction if we hit the top or bottom rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
                
            rail_index += direction
            
        # Combine all rails
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def railfence_decipher(self, cipher_text: str, num_rails: int) -> str:
        if num_rails < 2:
            raise ValueError("Number of rails must be at least 2")
            
        # Calculate the length of each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        # Split cipher text into rails
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length
            
        # Read the plain text
        plain_text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            if rails[rail_index]:
                plain_text += rails[rail_index].pop(0)
                
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text