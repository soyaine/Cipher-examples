# -*- coding: utf-8 -*-
#
# Hill Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 加密
#
def encrypt(matrix, words):
    check_param(matrix, words)
    cipher = ''
    length = len(matrix)
    words = words.lower()
    arr = [ord(i) - ord('a') for i in words]
    count = 0
    for ch in words:
        if str.isalpha(str(ch)):
            cipher += chr(sum(m * a for m, a in zip(matrix[count % length], arr)) % 26 + ord('a'))
            count += 1
    return cipher


#
# 解密
#
def decrypt(matrix, words):
    check_param(matrix, words)
    cipher = ''
    length = len(matrix)
    inv = mod_inverse_matrix(matrix)
    words = words.lower()
    arr = [ord(i) - ord('a') for i in words]
    count = 0
    for ch in words:
        if str.isalpha(str(ch)):
            cipher += chr(sum(m * a for m, a in zip(inv[count % length], arr)) % 26 + ord('a'))
            count += 1
    return cipher


#
# 行列式 (递归展开)
#
def determinant(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in m[1:]]
        det += (-1) ** j * m[0][j] * determinant(minor)
    return det


#
# 求矩阵在 mod 26 下的逆: 行列式逆元 x 伴随矩阵 (整数运算, 避免浮点误差)
#
def mod_inverse_matrix(matrix):
    length = len(matrix)
    det = determinant(matrix) % 26
    det_inv = None
    for i in range(1, 26):
        if det * i % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError('矩阵行列式与 26 不互质, 无法求模逆')

    adj = [[0] * length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            minor = [row[:c] + row[c+1:] for i, row in enumerate(matrix) if i != r]
            cofactor = (-1) ** (r + c) * determinant(minor)
            # 伴随矩阵是代数余子式矩阵的转置
            adj[c][r] = cofactor * det_inv % 26
    return adj


#
# 检查
#
def check_param(matrix, words):
    if len(matrix) * len(matrix) != \
       sum([len(matrix[i]) for i in range(len(matrix))]):
        print("Error: 矩阵必须是 m * m")
        quit()
    elif len(matrix) != len(words):
        print("Error: 明文的长度必须是 m （与矩阵的长宽相等）")
        quit()
    if determinant(matrix) % 26 == 0 or \
       all(determinant(matrix) % 26 * i % 26 != 1 for i in range(1, 26)):
        print("Error: 矩阵行列式与 26 不互质, 矩阵不可逆")
        quit()


if __name__ == '__main__':
    # 本例推算见《密码学基础》(西安电子科技大学出版社) 第7页

    # 密匙
    secret = [[ 8,  6,  9, 5  ],
              [ 6,  9,  5, 10 ],
              [ 5,  8,  4, 9  ],
              [ 10, 6, 11, 4  ]]
    # 明文
    text = "hill";

    # 使用密匙（矩阵）加密字符串
    ciphertext = encrypt(secret, text)

    # 密文
    print(ciphertext)

    # 解密字符串
    print(decrypt(secret, ciphertext))
