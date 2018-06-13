import gnupg
import time

def encrypt(gpg_home,filename,recipients):
	out_filename = filename + '.gpg'
	gpg = gnupg.GPG(gpg_home)
	try:
		f = open(filename,"rb")
	except:
		print("file not found")
		quit()
	t0 = time.clock()
	encrypted = gpg.encrypt(f,recipients,always_trust=True,output = out_filename)
	print("encryption time : " + str(time.clock()-t0))
	print(encrypted.ok)

#python 3
gpg_home = input()
filename = input()
recipients = input()
encrypt(gpg_home,filename,recipients)

#python 2
gpg_home = raw_input()
filename = raw_input()
recipients = raw_input()
encrypt(gpg_home,filename,recipients)
