from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply the shift
            shifted = (ord(char) - ascii_offset + key) % 26
            # Convert back to character
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    
    encrypted_message = caesar_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted_message})

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    
    decrypted_message = caesar_decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_message})

if __name__ == '__main__':
    app.run(debug=True) 