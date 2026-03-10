from flask import Flask, request, jsonify
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

#RAIL FENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plaintext = data['plaintext']
    num_rails = int(data['num_rails'])
    encrypt_text = railfence_cipher.rail_fence_encrypt(plaintext, num_rails)
    return jsonify({'encrypted_text': encrypt_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    ciphertext = data['ciphertext']
    num_rails = int(data['num_rails'])
    decrypt_text = railfence_cipher.rail_fence_decrypt(ciphertext, num_rails)
    return jsonify({'decrypted_text': decrypt_text})

#main function
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)