# RSA加密解密实现

from Crypto.PublicKey import RSA    
from Crypto.Cipher import PKCS1_OAEP
from binascii import hexlify

# 生成RSA密钥对
keyPair = RSA.generate(1024)
pubKey = keyPair.publickey()
print(f"Public key:(n = {hex(pubKey.n)}, e = {hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key:(n = {hex(pubKey.n)}, d = {hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# RSA数据加密
msg = b'I like cryptography'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", hexlify(encrypted))

# RSA数据解密
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted:", decrypted)
