from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCcipher
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'})
    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    return jsonify({'encrypted_message': encrypted_hex})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertext']
    key_type = data['key_type']
    
    # Convert hex back to bytes
    ciphertext = bytes.fromhex(ciphertext_hex)

    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'})
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_message})

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign():
    data = request.json
    message = data['message']
    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key = rsa_cipher.load_keys()[1] # Get public key
    
    # Convert hex back to bytes
    signature = bytes.fromhex(signature_hex)

    is_verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

# Assuming the ECCcipher class from the previous code snippet is defined and available.

ecc_cipher = ECCcipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    _, public_key = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    text = data.get('plain_text')
    key = int(data.get('key'))
    cipher = CaesarCipher()
    encrypted = cipher.encrypt_text(text, key)
    return jsonify({'cipher_text': encrypted})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    text = data.get('cipher_text')
    key = int(data.get('key'))
    cipher = CaesarCipher()
    decrypted = cipher.decrypt_text(text, key)
    return jsonify({'plain_text': decrypted})

if __name__ == "__main__":
    app.run(debug=True, port=5000)