from Crypto import Random  # 导入随机模块
from Crypto.Hash import SHA  # 导入sha加密
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5  # 加密数据和解密数据
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5  # 签名和解签
from Crypto.PublicKey import RSA  # 实现rsa加密
#签名和密文一起使用，私钥对密文进行签名，将密文和签名发送给公钥方，公钥方利用公钥对签名进行验证，签名通过后，再对数据进行解密
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Crypto import Random
from Crypto.PublicKey import RSA
def 公钥和私钥():
    random_generator = Random.new().read  # 生成随机偏移量
    # print(random_generator)
    rsa = RSA.generate(2048, random_generator)  # 生成一个私钥
    print(rsa)
    # 生成私钥
    private_key = rsa.exportKey()  # 导出私钥
    print(private_key.decode())
    # 生成公钥
    public_key = rsa.publickey().exportKey()  # 生成私钥所对应的公钥
    # print(public_key.decode())

    with open('rsa_private_key.pem', 'wb')as f:
        f.write(private_key)  # 将私钥内容写入文件中

    with open('rsa_public_key.pem', 'wb')as f:
        f.write(public_key)  # 将公钥内容写入文件中

#加密和解密
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

def get_key(key_file):
    with open(key_file) as f:
        data = f.read()  # 获取，密钥信息
        key = RSA.importKey(data)
    return key

def encrypt_data(msg):
    public_key = get_key('rsa_public_key.pem')  # 读取公钥信息
    cipher = PKCS1_cipher.new(public_key)  # 生成一个加密的类
    encrypt_text = base64.b64encode(cipher.encrypt(msg.encode()))  # 对数据进行加密
    return encrypt_text.decode()  # 对文本进行解码码


def decrypt_data(encrypt_msg):
    private_key = get_key('rsa_private_key.pem')  # 读取私钥信息
    cipher = PKCS1_cipher.new(private_key)  # 生成一个解密的类
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)  # 进行解密
    return back_text.decode()  # 对文本内容进行解码


#签名和解签
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature


def rsa_private_sign(data):
    private_key = get_key('rsa_private_key.pem')  # 导入私钥
    signer = PKCS1_signature.new(private_key)  # 设置签名的类
    digest = SHA.new()  # 创建sha加密的类
    digest.update(data.encode())  # 将要加密的数据进行sha加密
    sign = signer.sign(digest)  # 对数据进行签名
    # 对签名进行处理
    signature = base64.b64encode(sign)  # 对数据进行base64加密
    signature = signature.decode()  # 再进行编码
    return signature  # 返回签名


def rsa_public_check_sign(text, sign):
    publick_key = get_key('rsa_public_key.pem')  # 导入公钥
    verifier = PKCS1_signature.new(publick_key)  # 生成验证信息的类
    digest = SHA.new()  # 创建一个sha加密的类
    digest.update(text.encode())  # 将获取到的数据进行sha加密
    return verifier.verify(digest, base64.b64decode(sign))  # 对数据进行验证，返回bool值






if __name__ == "__main__":
    公钥和私钥()
    msg = "0x03,0x05,0x14,0x45,0xDE,0x92"
    encrypt_text = encrypt_data(msg)  # 加密
    decrypt_text = decrypt_data(encrypt_text)  # 解密
    print("加密后文件：",encrypt_text, "解密后文件：",decrypt_text)

    #sign = rsa_private_sign(msg) # 签名
    #print(rsa_public_check_sign(msg, sign))
