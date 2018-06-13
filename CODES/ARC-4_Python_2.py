from Crypto.Cipher import ARC4
import time

cipher = ARC4.new("sample key of any length")
inputFilename = 'frankenstein.txt'
data = open(inputFilename).read()

start_time_encrypt = time.time()
encrypted_data = cipher.encrypt(data)
print("--- %s seconds ---" % (time.time() - start_time_encrypt))
outputFilename = 'frankenstein.encrypted.txt'
outputFileObj = open(outputFilename, 'wb')
outputFileObj.write(encrypted_data)
outputFileObj.close()

start_time_decrypt = time.time()
print(cipher.decrypt(encrypted_data))
print("--- %s seconds ---" % (time.time() - start_time_decrypt))
#print (encrypted_data)
#print (cipher.decrypt(encrypted_data))