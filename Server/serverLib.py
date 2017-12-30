#!/usr/bin/python2.7
# 
import io
import subprocess
import gnupg
import paramiko
from multiprocessing.dummy import Pool as ThreadPool 

#dependencies: rngd(pkgAPT), python-gnupg(pymodule), paramiko(pymodule)

#========SSH========
class SSHCl:
	USERNAME = usr
	PASSWORD = passwd
	COMMAND  = cmd
	ADDRESS  = addr
	terminated = None

	def __init__(self, usr, passwd, cmd, addr):
		self.USERNAME = usr
		self.PASSWORD = passwd
		self.COMMAND  = cmd
		self.ADDRESS  = addr

		print('Initializing SSH session...')

	def __connect_ex():
		ssh = paramiko.SSHClient()
		ssh.connect(remote, username=self.USERNAME, password=self.PASSWORD)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
		exit_status = ssh_stdout.channel.recv_exit_status()

		print('SSH session finished: ' + len(exit_status))

	def didTerminate():
		if terminated == 1:
			return 0
		elif terminated != 1:
			return 1

#========GPG========
def keyGen(lengthOfKey, EMAIL, PASSWD):
    #TODO: Find a way of generating entropy on a headless machine.
    # Create thread for entropy

    # Create set of empty threads with reserved PIDs.
    pool = ThreadPool(4)

    #Entropy
    array_ans = []
    results= pool.map(os.system('rngd -r /dev/urandom &'), array_ans)

    for i in array_ans:
    	print(array_ans[i]) # Print each thread return code.

    input_data = gpg.gen_key_input(key_type="RSA", key_length=lengthOfKey, name_email=str(EMAIL), passphrase=PASSWD)

def ExportKey(keyID, public, private, nameOfStor):
    gpg = gnupg.GPG(gnupghome='/root')
    if public == True:
        asc_pub_keys = gpg.export_keys(keyID)
        f = open(nameOfStor, 'w+')
        f.write(asc_pub_keys)
        f.close()

    if private == True:
        asc_priv_keys = gpg.export_keys(keyID, True)
        f = open(nameOfStor + '-priv', 'w+')
        f.write(asc_pub_keys)
        f.close()

    else:
        print('No key specified!')

def ImportKey(file):
    gpg = gnupg.GPG(gnupghome='/root')
    f = open(file, 'r')
    import_result = gpg.import_key(f.read())
    f.close()

def ListAvailableKeys(ShowPrivate):
    gpg = gnupg.GPG(gnupghome='/root')
    if ShowPrivate == False:
        public_keys = gpg.list_keys() # same as gpg.list_keys(False)
    else:
        public_keys = gpg.list_keys() # same as gpg.list_keys(False)
        private_keys = gpg.list_keys(True) # True => private keys

def Encrypt(data, recipients, stream):
    gpg = gnupg.GPG(gnupghome='/root')
    f = open(stream, 'w+')
    f.write(gpg.encrypt(data, recipients))
    f.close()

def Decrypt(passwd, stream):
    gpg = gnupg.GPG(gnupghome='/root')
    f = open(stream, 'r')
    data = f.read()

    decrypted_data = gpg.decrypt(data)
    f.close()
    result = open(stream + '-result', 'w+')
    result.write(decrypted_data)
    result.close()

def VerifyData(file):
    gpg = gnupg.GPG(gnupghome='/root')
    f = open(file, r)
    data = f.read()
    verified = gpg.verify(data)
if not verified: raise ValueError("Signature could not be verified!") #TODO: Find a way to reject client session

# Transfer protocol
class RsyncSession:
     args = None
     path = None
     addr = None

     def __init__(self, rArgs, rPath, rAddr):
           self.args = rArgs
	   self.path = rPath
           self.addr = rAddr

    def send(self):
        os.system('rsync ' + self.args + ' ' + self.rAddr + ':' + self.path)



