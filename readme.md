# Encryption_Decryption_IPFS
This Repository Contains All The Effective Algorithms Of Encryption &amp; Decryption in Python 2 & 3. Please Go through "File_Encrypt_Decrypt.ipynb" for executed script. 

  1. Transposition File Cipher
  2. pyDES
  3. Tripple DES
  4. GnUPG
  5. AES
  6. RSA
  7. Blowfish
  8. ARC4
  9. Fernet
  10. Simple-crypt

## Uploading files onto IPFS
IPFS is the Inter PLanetary File System. It is a protocol and network designed to create a content-addressable, peer-to-peer method of storing and sharing hypermedia in a distributed file system.

### Prerequisites
You need to get IPFS up and running in your local machine. You can download a copy of IPFS from [here](https://ipfs.io/docs/install/) and install it. After installation you can initialise ipfs by using :

```
ipfs init
```
Once initialised you will have to now to start the IPFS daemon by using : 
 
```
ipfs daemon
```
where you'll see the following output if everything is working correctly :

```
Initializing daemon...
Successfully raised file descriptor limit to 2048.
Swarm listening on /ip4/127.0.0.1/tcp/4001
Swarm listening on /ip4/192.168.42.49/tcp/4001
Swarm listening on /ip6/::1/tcp/4001
Swarm listening on /p2p-circuit/ipfs/Qma4FuaPJ5hEP9gDURaRJ55G2H1X76qHRwwXEZEX5ebp9L
Swarm announcing /ip4/127.0.0.1/tcp/4001
Swarm announcing /ip4/192.168.42.49/tcp/4001
Swarm announcing /ip6/::1/tcp/4001
API server listening on /ip4/127.0.0.1/tcp/5001
Gateway (readonly) server listening on /ip4/127.0.0.1/tcp/8080
Daemon is ready


```
Now you are ready for testing.

### Running the Tests
In order to get the encryption & decryption working add your favourite encryption and decryption algorithm from the list provided to the uploader02.py and the downloader.py file. See to the fact that for some algorithms you'll need python 2 whereas for some others you'll need python 3. In my tests I have used an anaconda virtual environment for the python 2 files. For most of the encryption_decryption algorithms to work just pip install the modules imported in the respective files.But for Gnupg you also need to add the public keys to your key_ring.You can find more in the [gnupg documentation](https://pythonhosted.org/python-gnupg/).
A few of the algorithms here may require some upgrades and if you can fix them then please clone it, fix it and put up a pull request. Any pull requests are welcome. 
