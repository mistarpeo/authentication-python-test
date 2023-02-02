import hashlib
import secrets

string = 'dlrmfdkdlv3@'
encodings_string = string.encode()

hexdigest = hashlib.sha256(encodings_string).hexdigest()
print(hexdigest)

salt = secrets.token_hex(16)
print(salt)

rawAndSalt = 'dlrmfdkdlv3@'+"66cf33a7010d20e2520487434a619679"
encodings_string2 = rawAndSalt.encode("UTF-8")

hexdigest2 = hashlib.sha256(encodings_string2).hexdigest()
print(rawAndSalt)
print(hexdigest2)

# fb8707cceb291d16b565b343bd16e54d462d1e36d7649ba4ae8ccec3ca214947
# OqKlN7IOBut9Px+W/YzPsw==
# 13deb4ce9a59478f9df78d136e2e3fb7

# fb8707cceb291d16b565b343bd16e54d462d1e36d7649ba4ae8ccec3ca214947
# fb8707cceb291d16b565b343bd16e54d462d1e36d7649ba4ae8ccec3ca214947
