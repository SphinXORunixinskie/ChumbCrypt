# CreepyMuffin.py - A integrity checker for ChumbCrypt
# It checks the hash of a certificate, in this case any GPG certificate and warns if it's invalid.

import sys, io, os

def checkHash(CertFile):
    # Open downloaded hash file
    # We need a hash already premade for every existent certificate.

    os.system('md5sum ' + str(CertFile))

    # It will manually print if the certificate is okay or not.

def clearKey(CertFile):
    # Delete a certain key
    os.system('rm ' + str(CertFile))
