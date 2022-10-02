import pyaes

# A 256 bit (32 byte) key
key = "................................"
plaintext = "Text may be any length you wish, no padding is required"

key = key.encode('utf-8')

aes = pyaes.AESModeOfOperationCTR(key)    
ciphertext = aes.encrypt(plaintext)
print (ciphertext)

# DECRYPTION
aes = pyaes.AESModeOfOperationCTR(key)


decrypted = aes.decrypt(ciphertext).decode('utf-8')

print (decrypted == plaintext)
