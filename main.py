import base64
import hashlib
from mnemonic import Mnemonic

def load_display():
    try:
        with open('exluminate.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Welcome to PrivKeyEd25519 converter!"

print(load_display())

# Input
priv_key_base64 = input("\nInput PrivKeyEd25519 (Base64 format): ").strip()

try:
    # Decode Private Key from Base64 to Bytes
    priv_key_bytes = base64.b64decode(priv_key_base64)

    # Hash private key to get entropy
    entropy = hashlib.sha256(priv_key_bytes).digest()

    # Convert to mnemonic using BIP39
    mnemo = Mnemonic("english")
    mnemonic = mnemo.to_mnemonic(entropy)

    # Print to mnemonic phrases
    print("\nMnemonic phrases: ")
    print(mnemonic)
except Exception as e:
    print("❌ Theres an error: ", str(e))
