from flask import Flask, render_template, request

app = Flask(__name__)

# Define routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['GET', 'POST'])
def solve_problem():
    if request.method == 'POST':
        algorithm = request.form.get('algorithm')
        plaintext = request.form.get('plaintext')
        key = request.form.get('key')
        if algorithm == 'caesar':
            solution = solve_caesar_cipher(plaintext, key)
        elif algorithm == 'substitution':
            solution = solve_substitution_cipher(plaintext, key)
        elif algorithm == 'vigenere':
            solution = solve_vigenere_cipher(plaintext, key)
        else:
            solution = "Algorithm not supported"
        return render_template('solution.html', algorithm=algorithm, plaintext=plaintext, key=key, solution=solution)
    return render_template('solve.html')

# Define functions to solve algorithms

def solve_caesar_cipher(plaintext, key):
    # Caesar cipher solution code
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + int(key)
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

def solve_substitution_cipher(plaintext, key):
    # Substitution cipher solution code
    substitution_key = {}
    for i in range(len(plaintext)):
        substitution_key[plaintext[i]] = key[i]
    ciphertext = "".join(substitution_key.get(char, char) for char in plaintext)
    return ciphertext

def solve_vigenere_cipher(plaintext, key):
    # Vigenère cipher solution code
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ""
    for i in range(len(plaintext_int)):
        shift = key_as_int[i % key_length]
        shifted = (plaintext_int[i] + shift) % 256
        ciphertext += chr(shifted)
    return ciphertext

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
