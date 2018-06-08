from Crypto.Cipher import Blowfish
import time
import ipfsapi
import os

INPUT_SIZE = 8

def pad_string(str):

	new_str = str
	pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
	return new_str

def uploader02(filename,password):
	#os.system("ipfs daemon")
	arr = filename.split('.')
	outputFilename = arr[0] + "_encrypted.txt"

	d = open(filename, "rb")
	data = d.read()
	d.close()

	crypt_obj = Blowfish.new(password, Blowfish.MODE_ECB)

	start_time_encrypt = time.time()
	ciphertext = crypt_obj.encrypt(pad_string(data))
	print("--- %s seconds ---" % (time.time() - start_time_encrypt))
	#ciphertext
	fd = open(outputFilename, "wb")
	fd.write(ciphertext)
	fd.close()
	api = ipfsapi.connect('127.0.0.1',5001) # 127.0.0.1 
	res = api.add(outputFilename)
	print(res)

filename = raw_input()
password = raw_input()
uploader02(filename,password)
