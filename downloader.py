import gnupg
import ipfsapi
import time
from Crypto.Cipher import Blowfish
''' downloader code for Blowfish encryption'''
def downloader(hash,filename,password):
	arr = filename.split('.')
	outputFilename = arr[0] + "_decrypted." + arr[1]

	api = ipfsapi.connect('127.0.0.1',5001)
	res = api.cat(hash)
	arr = filename.split('.')
	'''
	gpg = gnupg.GPG('/home/abhiwin2010/gpghome')
	t0 = time.clock()
	status = gpg.decrypt(res,passphrase=passphrase,output=filename)
	print("decryption time: " + str(time.clock()-t0))
	print(status.ok)
	'''
	crypt_obj = Blowfish.new(password, Blowfish.MODE_ECB)
	start_time_encrypt = time.time()
	ciphertext_decrypted = crypt_obj.decrypt(res)
	print("--- %s seconds ---" % (time.time() - start_time_encrypt))
	fd = open(outputFilename, "wb")
	fd.write(ciphertext_decrypted)
	fd.close()


hash = raw_input()
filename = raw_input()
password = raw_input()
downloader(hash,filename,password)
