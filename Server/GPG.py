import os, sys, gnupg
gpg = gnupg.GPG(gnupghome='/root')

def keyGen(lengthOfKey, EMAIL, PASSWD):
    #TODO: Find a way of generating entropy on a headless machine.

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

