# -*- coding: utf-8 -*-
#
# Multiplicative Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 乘法密码: 密文 = 明文 x 密钥 (mod 26)
# 与仿射密码 (b=0) 同族, 要求密钥与 26 互质, 否则无法唯一解密
# 可用密钥: 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
#

#
# 求密钥在 mod 26 下的乘法逆元
#
def mod_inverse(key):
    for i in range(1, 26):
        if key * i % 26 == 1:
            return i
    raise ValueError('密钥 %s 必须与 26 互质' % key)


#
# 加密
#
def encrypt(key, words):
    ciphertext = ''
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base) * key % 26 + base)
        else:
            ciphertext += ch
    return ciphertext


#
# 解密
#
def decrypt(key, words):
    inverse = mod_inverse(key)
    ciphertext = ''
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base) * inverse % 26 + base)
        else:
            ciphertext += ch
    return ciphertext


if __name__ == '__main__':
    # 与仿射密码 E(x) = (a*x + b) mod 26 的 b=0 情形一致
    # 规则见 http://en.wikipedia.org/wiki/Affine_cipher

    # 明文
    plaintext = 'hello world, this is multiplicative cipher.'

    # 密匙
    key = 5

    # 加密
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
