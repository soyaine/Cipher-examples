# -*- coding: utf-8 -*-
#
# Trifid Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import re

#
# 三分密码 (Delastelle): 用密钥生成 3x3x3 立方体, 每个字母对应三元组(层,行,列)
# 明文按 period 分组, 组内各字母的三元组竖写成三行, 横向拼成一串后
# 每 3 位重新查表得到密文; 建议分组长度与 3 互质以获得最大扩散
#

#
# 生成立方体: 密钥去重在前, 其余字母(含第 27 字符 '+')按序补齐, 按 层->行->列 填入
#
def generate_cube(key=''):
    mixed = ''
    for ch in re.sub(r'[^A-Za-z]', '', key).upper():
        if ch not in mixed:
            mixed += ch
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ+':
        if ch not in mixed:
            mixed += ch
    cube = {}
    for i, ch in enumerate(mixed):
        cube[ch] = (i // 9 + 1, i % 9 // 3 + 1, i % 3 + 1)
    return cube


#
# 加密
#
def encrypt(key, period, words):
    cube = generate_cube(key)
    inverse = dict((v, k) for k, v in cube.items())
    words = re.sub(r'[^A-Za-z]', '', words).upper()

    ciphertext = ''
    for i in range(0, len(words), period):
        group = words[i:i+period]
        layers, rows, cols = [], [], []
        for ch in group:
            l, r, c = cube[ch]
            layers.append(l)
            rows.append(r)
            cols.append(c)
        # 三行竖写, 横向拼成一串
        digits = layers + rows + cols
        for j in range(0, len(digits), 3):
            ciphertext += inverse[tuple(digits[j:j+3])]
    return ciphertext


#
# 解密
#
def decrypt(key, period, words):
    cube = generate_cube(key)
    inverse = dict((v, k) for k, v in cube.items())
    words = re.sub(r'[^A-Za-z+]', '', words).upper()

    plaintext = ''
    for i in range(0, len(words), period):
        group = words[i:i+period]
        digits = []
        for ch in group:
            digits.extend(cube[ch])
        n = len(group)
        # 横串还原为三行, 逐列竖读出三元组
        for j in range(n):
            plaintext += inverse[(digits[j], digits[n+j], digits[2*n+j])]
    return plaintext


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Trifid_cipher
    # 密钥 FELIXMARDSTB 恰好复现 wiki 示例的立方体

    # 明文
    plaintext = 'aide-toi, le ciel t\'aidera'

    # 密匙与分组长度
    key, period = 'FELIXMARDSTB', 5

    # 加密
    ciphertext = encrypt(key, period, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, period, ciphertext))
