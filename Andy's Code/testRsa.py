'''
Author: AndyYe
Date: 2022-12-12 18:41:09
LastEditors: AndyYe
LastEditTime: 2022-12-12 18:51:43
FilePath: \Andy's Code\testRsa.py
Description: 

Copyright (c) 2022 by AndyYe, All Rights Reserved. 
'''
import rsa


# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    print("公钥:\n%s\n私钥:\n%s" % (pubkey, privkey))
    # 明文编码格式
    content = str.encode("utf-8")
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode("utf-8")
    return con


if __name__ == "__main__":
    str, pk = rsaEncrypt("what the fuck")
    print("加密后密文：\n%s" % str)

    content = rsaDecrypt(str, pk)
    print("解密后明文：\n%s" % content)

