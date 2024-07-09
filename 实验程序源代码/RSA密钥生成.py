# RSA密钥生成、加密解密和身份认证

import Crypto.PublicKey.RSA
import Crypto.Random
import Crypto.Cipher.PKCS1_v1_5
import Crypto.Signature.PKCS1_v1_5
import Crypto.Hash

x = Crypto.PublicKey.RSA.generate(1024)
publickey = x.exportKey("PEM")                  # 生成私钥
privatekey = x.publickey().exportKey()          # 生成公钥

with open("publickey.pem", "wb") as x:
    x.write(publickey)
with open("privatekey.pem", "wb") as x:
    x.write(privatekey)

with open("publickey.pem", "rb") as x:
    xx = Crypto.PublicKey.RSA.importKey(x.read())

b = xx.publickey().exportKey()  # 生成公钥
with open("privatekey.pem", "wb") as x:
    x.write(b)

a = xx.exportKey("DER")  # 生成 DER 格式的证书
with open("a.der", "wb") as x:
    x.write(a)

y = b"abcdefg1234567"
with open("privatekey.pem", "rb") as x:
    b = x.read()
    cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(b))
    cipher_etxt = cipher_public.encrypt(y)  # 使用公钥进行加密


with open("publickey.pem", "rb") as x:
    a = x.read()
    # 如果私钥有密码，则使用对应的密码Crypto.PublicKey.RSA.importKey(a, "Password")
    cipher_private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(a))
    text = cipher_private.decrypt(cipher_etxt, Crypto.Random.new().read)    # 使用私钥进行解密
    assert text == y    # 断言验证

with open("publickey.pem", "rb") as x:
    c = x.read()
    c_rsa = Crypto.PublicKey.RSA.importKey(c)
    signer = Crypto.Signature.PKCS1_v1_5.new(c_rsa)
    msg_hash = Crypto.Hash.SHA256.new()
    msg_hash.update(y)
    sign = signer.sign(msg_hash)    # 使用私钥进行‘sha256’签名


with open("publickey.pem", "rb") as x:
    d = x.read()
    d_rsa = Crypto.PublicKey.RSA.importKey(d)
    verifier = Crypto.Signature.PKCS1_v1_5.new(d_rsa)
    msg_hash = Crypto.Hash.SHA256.new()
    msg_hash.update(y)
    result = verifier.verify(msg_hash, sign)
    print(result)
