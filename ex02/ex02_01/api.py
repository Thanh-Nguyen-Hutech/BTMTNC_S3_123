from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plaintext = data['plaintext']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plaintext, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    ciphertext = data['ciphertext']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(ciphertext, key)
    return jsonify({'decrypted_message': decrypt_text})

#main function
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)