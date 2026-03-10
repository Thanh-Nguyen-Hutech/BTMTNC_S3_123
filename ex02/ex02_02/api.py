from flask import Flask, request, jsonify
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    encrypt_text = vigenere_cipher.vigenere_encrypt(plaintext, key)
    return jsonify({'encrypted_text': encrypt_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypt_text = vigenere_cipher.vigenere_decrypt(ciphertext, key)
    return jsonify({'decrypted_text': decrypt_text})

#main function
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)