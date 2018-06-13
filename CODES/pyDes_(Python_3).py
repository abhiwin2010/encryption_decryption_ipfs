from pyDes import *
import time

inputFilename = 'frankenstein.txt'

data = open(inputFilename).read()
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

start_time_encrypt = time.time()
#if myMode == 'encrypt':
d = k.encrypt(data)
#elif myMode == 'decrypt':
#        d = k.encrypt(data)
print("--- %s seconds ---" % (time.time() - start_time_encrypt))

outputFilename = 'frankenstein.encrypted.txt'
outputFileObj = open(outputFilename, 'wb')
outputFileObj.write(d)
outputFileObj.close()

start_time_decrypt = time.time()
do = k.decrypt(d)
print("--- %s seconds ---" % (time.time() - start_time_decrypt))
#print ("Encrypted: %r" % d)
#totalTime = round(time.time() - startTime, 2)
#print('%sion time: %s seconds' % (myMode.title(), totalTime))

#print ("Decrypted: %r" % k.decrypt(d))
#assert k.decrypt(d, padmode=PAD_PKCS5) == data
#outputFilename = 'frankenstein.encrypted.txt'
#outputFileObj = open(outputFilename, 'wb')
#outputFileObj.write(d)
#outputFileObj.close()
    
#print('Done using %s (%s characters).' % (inputFilename, len(data)))
#print('New file is %s.' % (outputFilename))