# RSA数字签名和验证

from Crypto.PublicKey import RSA
from hashlib import sha512

# generate  RSA key pair
keyPair = RSA.generate(bits=1024)
print(f"Public key: (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# RSA sign the message
msg = b'RSA digital signature and verify'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# RSA verify signature
msg = b'RSA digital signature and verify'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)

# RSA verify signature (tampered msg)
msg = b'RSA digital signature and verify (tampered)'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid (tampered):", hash == hashFromSignature)
