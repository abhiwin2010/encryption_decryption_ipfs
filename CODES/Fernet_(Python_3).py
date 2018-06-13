from cryptography.fernet import Fernet
import time

key = Fernet.generate_key()
cipher_suite = Fernet(key)

inputFilename = 'frankenstein.txt'
data = open(inputFilename).read().encode()

start_time_encrypt = time.time()
cipher_text = cipher_suite.encrypt(data)
print("--- %s seconds ---" % (time.time() - start_time_encrypt))

print(cipher_text)

outputFilename = 'frankenstein.encrypted.txt'
outputFileObj = open(outputFilename, 'wb')
outputFileObj.write(encrypted_data)
outputFileObj.close()

start_time_decrypt = time.time()
plain_text = cipher_suite.decrypt(cipher_text)
print("--- %s seconds ---" % (time.time() - start_time_decrypt))

print(plain_text.decode())