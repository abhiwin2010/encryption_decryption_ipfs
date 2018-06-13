from binascii import hexlify
from getpass import getpass
from sys import stdin
from simplecrypt import encrypt, decrypt
import time

# read the password from the user (without displaying it)
password = getpass("password: ")

# read the (single line) plaintext we will encrypt
inputFilename = 'frankenstein.txt'
message = open(inputFilename).read()
#print("message: abcdefghij12345")
#message = stdin.readline()

# encrypt the plaintext.  we explicitly convert to bytes first (optional)
start_time_encrypt = time.time()
ciphertext = encrypt(password, message.encode())
print("--- %s seconds ---" % (time.time() - start_time_encrypt))

outputFilename = 'frankenstein.encrypted.txt'
outputFileObj = open(outputFilename, 'wb')
outputFileObj.write(ciphertext)
outputFileObj.close()
# the ciphertext plaintext is bytes, so we display it as a hex string
#print("ciphertext: %s" % hexlify(ciphertext))

# now decrypt the plaintext (using the same salt and password)
start_time_decrypt = time.time()
plaintext = decrypt(password, ciphertext)
print("--- %s seconds ---" % (time.time() - start_time_decrypt))


outputFilename = 'frankenstein.encrypted_REAL.txt'
outputFileObj = open(outputFilename, 'w')
outputFileObj.write(plaintext.decode())
outputFileObj.close()

# the decrypted plaintext is bytes, but we can convert it back to a string
#print("plaintext: %s" % plaintext)
#print("plaintext as string: %s" % plaintext.decode('utf8'))