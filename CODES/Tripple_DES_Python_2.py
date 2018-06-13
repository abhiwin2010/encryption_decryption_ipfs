from Crypto.Cipher import DES3
import time

INPUT_SIZE = 8

def pad_string(str):

	new_str = str
	pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)
	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
		
	return new_str
cipher = DES3.new("sixteen byte key") # or 24-byte key
inputFilename = 'frankenstein.txt'
data = open(inputFilename).read()
data = pad_string(data)

start_time_encrypt = time.time()
encrypted_data = cipher.encrypt(data)
print("--- %s seconds ---" % (time.time() - start_time_encrypt))

#print (encrypted_data)

outputFilename = 'frankenstein.encrypted.txt'
outputFileObj = open(outputFilename, 'wb')
outputFileObj.write(encrypted_data)
outputFileObj.close()

start_time_decrypt = time.time()
decrypted_data = cipher.decrypt(encrypted_data)
print("--- %s seconds ---" % (time.time() - start_time_decrypt))
#print (cipher.decrypt(encrypted_data))