import sys, time, platform gnupg
import pip
import socket
from subprocess import call

White  = '\033[0m'
Red    = '\033[31m'
Green  = '\033[32m'
Orange = '\033[33m'
Blue   = '\033[34m'
Purple = '\033[35m'
Cyan   = '\033[36m'
Gray   = '\033[37m'

####GPG####
gpg = gnupg.GPG(gnupghome='/root')

def keyGen(lengthOfKey, EMAIL, PASSWD):


    #TODO: Find a way of generating entropy on a headless machine.
    input_data = gpg.gen_key_input(key_type="RSA", key_length=lengthOfKey, name_email=str(EMAIL), passphrase=PASSWD)
                                                    #2048
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
####END OF GPG####

def OSDetect():
    print('Detected OS: ' + Orange + str(platform.system()) + White + '.')

def banner():
    print(Blue + '==================================' + White)
    print(Blue + '=' + Green + '        ChumbCrypt v0.01        ' + Blue + '=' + White)
    print(Blue + '=' + Green + '   Written by Nicole Gossett    ' + Blue + '=' + White)
    print(Blue + '==================================' + White)
    OSDetect()

def clientInit():
    banner()
    print('')
    try:
        import nmap # For diagnostics and problem checking
        import urllib  # For any future cert fetching 
        import urllib2 # Same here
        import smtplib # Admin SMTP sender

    except ImportError:
        print(Red + '[!] Missing dependencies! Installing them via pip...' + White)
        pip.main(['install', 'python-nmap', 'beautifulsoup', 'urllib', 'urllib2'])

    print(Orange + '[+] Initializing....' + White)
    #TODO: GPG module interaction here, setting up home dir.
    print(Red + '[!] Make sure to have a GPG key ready!' + White)
    print('======================================')
    print('Type \'help\' for command guide')
    print('')

    #TODO: Write documentation for the commands
    #TODO: portal is within kerb. realm

    while True:
        Input = input('[>] ')
        if Input == 'help':
            print('**** HELP ****')
            print('login - log in to portal')
            print('mount - mount remote storage')
            print('exit  - quit ChumbCrypt')
        elif Input == 'login':
            Username = input('Username: ')
            Password = input('Password: ')
            Key      = input('GPG Key: ')

            RUNNING = True
            while RUNNING == True:
                s.recv = 0
                data = s.recv(0)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(('127.0.0.1', 8080))  # Bind port to socket. #TODO: Make this server IP
                amount_expected = 120
                if data < amount_expected:
                    s.send = [Username, Password, Key]
                if amount_expected != s.send:
                    return shit

                #if [Username, Password, Key] != 0:
                #    USRNAME = s[Username]
                #    PASSWD = s[Password]
                #    Key = s[Key]
                #    
                #if s[Username] != Username:
                #    s.close()
                #if s[Password] != Password:
                #    s.close()
                #if s[Key] != Key:
                #    s.close()

                s.received += len(data)

                print('Content of sent message: ' + s[Username, Password, Key])
                RUNNING = False




        #letsnot till rdy



                print('Done.')
        elif Input == 'mount':
            print('Coming soon!')
        elif Input == 'exit':
            exit()
        else:
            print(Red + '[!] Command not found!' + White)

clientInit()
