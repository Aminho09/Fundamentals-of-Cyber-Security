def rotate_left(n, d, width=8):
    return ((n << d) & (2**width - 1)) | (n >> (width - d))

def feistel_round_encrypt(L, R, K):
    F_result = rotate_left(R ^ K, 3)
    F_result = F_result ^ rotate_left(K, 1)
    new_L = R
    new_R = L ^ F_result
    return new_L, new_R

def encrypt(plaintext, key):
    KL = key >> 8
    KR = key & 0xFF
    
    L, R = plaintext >> 8, plaintext & 0xFF
    
    for i in range(4):
        if i % 2 == 0:
            Ki = rotate_left(KL, i+1)
            L, R = feistel_round_encrypt(L, R, Ki)
        else:
            Ki = rotate_left(KR, i+1)
            L, R = feistel_round_encrypt(L, R, Ki)
    
    ciphertext = (L << 8) | R
    return ciphertext

def feistel_round_decrypt(L, R, K):
    F_result = rotate_left(L ^ K, 3)
    F_result = F_result ^ rotate_left(K, 1)
    new_R = L
    new_L = R ^ F_result
    return new_L, new_R

def decrypt(ciphertext, key):
    KL = key >> 8
    KR = key & 0xFF
    
    L, R = (ciphertext >> 8) & 0xFF, ciphertext & 0xFF
    
    for i in range(3, -1, -1):
        if i % 2 == 0:
            newKL = rotate_left(KL, i+1)
            L, R = feistel_round_decrypt(L, R, newKL)
        else:
            newKR = rotate_left(KR, i+1)
            L, R = feistel_round_decrypt(L, R, newKR)
    
    plaintext = (L << 8) | R
    return plaintext

plaintext = 0x5367
key = 0xF2A1
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {hex(plaintext)}")
print(f"Ciphertext: {hex(ciphertext)}")
print(f"Decrypted: {hex(decrypted_text)}")
