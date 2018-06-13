from Crypto.Cipher import Blowfish
import time

INPUT_SIZE = 8

def pad_string(str):

	new_str = str
	pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)
	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
		
	return new_str

cipher = Blowfish.new("key must be 4 to 56 bytes")

#inputFilename = 'frankenstein.txt'

#inputFilename = 'IntegratedBRAC_Negative-SampleReport.pdf'

inputFilename = 'img.jpg'

data = open(inputFilename).read()
data = pad_string(data)
#len(data)
start_time_encrypt = time.time()
encrypted_data = cipher.encrypt(data)
print("--- %s seconds ---" % (time.time() - start_time_encrypt))
print (encrypted_data)
#outputFilename = 'img_encrypt.txt'
#outputFileObj = open(outputFilename, 'wb')
#outputFileObj.write(encrypted_data)
#outputFileObj.close()

start_time_decrypt = time.time()
decrypted_data = cipher.decrypt(encrypted_data).decode('latin-1')
print("--- %s seconds ---" % (time.time() - start_time_decrypt))

#outputFilename = 'img_decrypt.jpg'
#outputFileObj = open(outputFilename, 'wb')
#outputFileObj.write(encrypted_data)
#outputFileObj.close()
