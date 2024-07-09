from Crypto.Cipher import AES
import base64
# 密钥（key），密钥偏移量（iv），CBC模式加密
BLOCK_SIZE = 16 # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s)-1:])]

vi = '0102030405060708'

def AES_Encrypt(key, data):
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, vi.encode('utf-8'))
    encrytedbytes = cipher.encrypt(data.encode('utf-8'))
    # 加密后得到的是bytes类型的数据，使用Base64进行编码，返回bytes字符串
    encodestrs = base64.b64encode(encrytedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf-8')
    return enctext


def AES_Decrypt(key, data):
    data= data.encode('utf-8')
    encoderbytes = base64.decodebytes(data)
    # 将加密数据转换为bytes类型数据
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, vi.encode('utf-8'))
    text_decrypted = cipher.decrypt(encoderbytes)
    # 去补位
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf-8')
    return text_decrypted

if __name__ == '__main__':
    key = '1234567890123456'
    print("Key is:",key)
    data = 'I like cryptography and network security'
    print("Plaintext is:", data)
    enctext = AES_Encrypt(key, data)
    print("Ciphertext is:", enctext)
    decryptedtext = AES_Decrypt(key, enctext)
    print("Decryptedtext is:", decryptedtext)
