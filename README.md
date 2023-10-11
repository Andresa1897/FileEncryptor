# File Encryptor

File Encryptor is a Python script that allows you to encrypt and decrypt files using symmetric key encryption. This tool provides a simple way to secure your sensitive data.

## Usage

### Prerequisites
Before you begin, make sure you have Python installed on your system.

### How to Run
1. Clone the repository:
Git clone Repository_URL]

2. Navigate to the project directory:
cd File-Encryptor

3. Run the script:
python file_encryptor.py


### Options
- **Encrypt a File:**
- Choose option 1 to encrypt a file.
- Enter the path of the file you want to encrypt.
- The encrypted file will be saved with a `.enc` extension.

![Encrypting](https://github.com/Andresa1897/FileEncryptor/assets/98703359/3d8de0a2-a8cb-4d36-a1f3-7e89ea211855)

- **Decrypt a File:**
- Choose option 2 to decrypt a file.
- Enter the path of the encrypted file (with `.enc` extension).
- The decrypted file will be saved without the `.enc` extension.

![Decrypt](https://github.com/Andresa1897/FileEncryptor/assets/98703359/faef6816-8150-4492-9a49-9b378fc21431)

- ### Key Handling
- The symmetric key is saved as `key.key` in the script directory.
- Keep this key secure for decryption. Do not share it with anyone.

**Note:** Ensure you have the necessary permissions to read, write, and execute files in the specified paths.

## Acknowledgments
Thanks to Vinslov for the inspiration and guidance.
