# Cryptography Algorithm Solver

This Flask application provides a simple web interface to solve various cryptography algorithms including Caesar, Substitution, and Vigenère ciphers. Users can input their plaintext along with the selected algorithm and key, and the application will return the corresponding ciphertext.

## Interface Screenshots

### Home Page
![Home Page](screenshots/cryptho.jpg)

### Solution Page
![Solution Page](screenshots/cryptosolve.jpg)

## Getting Started

To get started with this application, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using `pip install -r requirements.txt`.

3. **Run the Application**: Execute `flask run` or `python app.py` to start the Flask application.

4. **Access the Web Interface**: Open your web browser and go to `http://localhost:5000/solve` to access the application.

## Usage

Once the application is running, you can use the following steps to encrypt your plaintext:

1. Navigate to the homepage.

2. Enter your plaintext, select the desired algorithm (Caesar, Substitution, or Vigenère), and provide the encryption key.

3. Click on the "Solve" button to encrypt the plaintext.

4. The application will display the ciphertext along with the provided algorithm, plaintext, and key.

## Supported Algorithms

This application supports the following cryptography algorithms:

- **Caesar Cipher**: Shifts each letter in the plaintext by a certain number of places determined by the key.
  
- **Substitution Cipher**: Replaces each letter in the plaintext with a corresponding letter from the provided key.

- **Vigenère Cipher**: Uses a keyword to shift each letter in the plaintext by different amounts, creating a repeating key pattern.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

