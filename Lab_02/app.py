from flask import Flask, render_template, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher  import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")   
def caesar():
    return render_template("caesar.html")

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

#Caesar Cipher
@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])
        if not text:
            return "Error: Text cannot be empty", 400
        if not isinstance(key, int):
            return "Error: Key must be an integer", 400
            
        Caesar = CaesarCipher()
        encrypted_text = Caesar.encrypt_text(text, key)
        return render_template("caesar.html", 
                             result=f"Encrypted text: {encrypted_text}",
                             input_text=text,
                             input_key=key)
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])
        if not text:
            return "Error: Text cannot be empty", 400
        if not isinstance(key, int):
            return "Error: Key must be an integer", 400
            
        Caesar = CaesarCipher()
        decrypted_text = Caesar.decrypt_text(text, key)
        return render_template("caesar.html", 
                             result=f"Decrypted text: {decrypted_text}",
                             input_text=text,
                             input_key=key)
    except Exception as e:
        return f"Error: {str(e)}", 400

#Vigenere Cipher
@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        text = request.form["inputPlainText"]
        key = request.form["inputKeyPlain"]
        if not text:
            return "Error: Text cannot be empty", 400
        if not key:
            return "Error: Key cannot be empty", 400
        if not all(c.isalpha() for c in key):
            return "Error: Key must contain only letters", 400
            
        Vigenere = VigenereCipher()
        encrypted_text = Vigenere.vigener_cipher(text, key)
        return render_template("vigenere.html", 
                             result=f"Encrypted text: {encrypted_text}",
                             input_text=text,
                             input_key=key)
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        text = request.form["inputCipherText"]
        key = request.form["inputKeyCipher"]
        if not text:
            return "Error: Text cannot be empty", 400
        if not key:
            return "Error: Key cannot be empty", 400
        if not all(c.isalpha() for c in key):
            return "Error: Key must contain only letters", 400
            
        Vigenere = VigenereCipher()
        decrypted_text = Vigenere.vigener_decipher(text, key)
        return render_template("vigenere.html", 
                             result=f"Decrypted text: {decrypted_text}",
                             input_text=text,
                             input_key=key)
    except Exception as e:
        return f"Error: {str(e)}", 400

#Railfence Cipher
@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])
        if not text:
            return "Error: Text cannot be empty", 400
        if key < 2:
            return "Error: Key must be at least 2", 400
            
        Railfence = RailFenceCipher()
        encrypted_text = Railfence.railfence_cipher(text, key)
        return render_template("railfence.html", 
                             result=f"Encrypted text: {encrypted_text}",
                             input_text=text,
                             input_key=key)
    except ValueError:
        return "Error: Key must be a number", 400
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])
        if not text:
            return "Error: Text cannot be empty", 400
        if key < 2:
            return "Error: Key must be at least 2", 400
            
        Railfence = RailFenceCipher()
        decrypted_text = Railfence.railfence_decipher(text, key)
        return render_template("railfence.html", 
                             result=f"Decrypted text: {decrypted_text}",
                             input_text=text,
                             input_key=key)
    except ValueError:
        return "Error: Key must be a number", 400
    except Exception as e:
        return f"Error: {str(e)}", 400

# #Transposition Cipher

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted_text: {decrypted_text}"

# #Playfair Cipher

@app.route("/matrix", methods=["POST"])
def create_playfair_matrix():
    key = request.form["inputKeyPlain"].upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    
    matrix_html = "<table border='1'>"
    for row in playfair_matrix:
        matrix_html += "<tr>"
        for char in row:
            matrix_html += f"<td>{char}</td>"
        matrix_html += "</tr>"
    matrix_html += "</table>"
    
    return matrix_html

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"].upper().replace("J", "I")
    key = request.form["inputKeyPlain"].upper().replace("J", "I")
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_cipher(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"].upper().replace("J", "I")
    key = request.form["inputKeyCipher"].upper().replace("J", "I")
    Playfair = PlayFairCipher()
    matrix =  Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decipher(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted_text: {decrypted_text}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)