# -*- coding: utf-8 -*-
#
# Trithemius Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 特里特米乌斯密码: 逐字母位移递增的凯撒密码
# 第 i 个字母位移 i 位 (0 起始), 即 tabula recta 的对角线
#

#
# 加密
#
def encrypt(words):
    ciphertext = ''
    count = 0
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base + count) % 26 + base)
            count += 1
        else:
            ciphertext += ch
    return ciphertext


#
# 解密
#
def decrypt(words):
    ciphertext = ''
    count = 0
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base - count) % 26 + base)
            count += 1
        else:
            ciphertext += ch
    return ciphertext


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Trithemius_cipher

    # 明文
    plaintext = 'hello world, this is trithemius cipher.'

    # 加密
    ciphertext = encrypt(plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext))
