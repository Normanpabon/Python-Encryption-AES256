# FileSecureStorageWithAES256

Encrypt and keep safe your files with AES256 cipher


# Requeriments

- Python 3.5+
- Python cryptography module cryptography (install with: pip install cryptography)

# Usage

run with:
-- python Script.py

then, put the files that you want to encrypt in 'Input' folder and continue

The encrypted files will be in 'Output' folder

For Decrypting the procedure is the same




# Security limitation (at least for now)

Memory wiping is used to protect secret data or key material from attackers with access to deallocated memory.
This is a defense-in-depth measure against vulnerabilities that leak application memory.

Source: https://cryptography.io/en/latest/limitations/
