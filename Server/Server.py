import sys
import io
import pip
import os
import gnugp
import socket
import subprocess


# Initialize application data.
# This program guesses that you supply the directory ~/Gaikai

TCP_IP   = '127.0.0.1'
TCP_PORT = 8080 # Can be changed.
KeyID    = None


def ListenForKey(addr, port, maxRequests):

	RSA      = None
	Name     = None
	Email    = None
	ClientID = None
	CanRun   = True

	if port != 0:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((addr, port)) # Bind port to socket.
		s.listen(maxRequests)

		print('Connected: ' + addr + ':' + str(port))
		while CanRun == True:
			f = open('icepted.txt', 'aw+')

			f.write(str(s.listen(maxRequests)))
			conn, addr = s.accept()
			f.close()
		print('Goodbye.')
		s.close()

	else:
		print('ERR: Unable to connect!')

def rsync():
    process[] = subprocess.Popen([cmd], shell = True,
                                      stdout=subprocess.Pipe,
                                      stdrr=subprocess.STDOUT)
    output = ''

    for line in iter(process.stdout.readline, ''):
        line = line.replace('\r', '').replace('\n', '')
        print(line)
        sys.stdout.flush()

        output += line
        process.wait()
        exitCode = process.returncode

    if exitCode == 0:
        return output
    else
        raise Expection(KeyID, cmd, exitCode, output)
    execute(['ping', 'localhost'])


#   system('rsync -avz' + () + () + "")
#def MountStorage(Key, StorageDV):
#/dev




#def backup(self, source, destination, archive = None,
          # excludeList = None, passwordFile = None):

#ListenForKey(TCP_IP, TCP_PORT, 500)
