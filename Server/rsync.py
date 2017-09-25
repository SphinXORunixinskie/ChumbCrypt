import getpass
import threading
import subprocess

class myclass(threading.Thread)
    def __init__(selfSelf):
        self.stdout = None
        self.stdderr = None
        threading.Thread.__init__(self)

    def run(self):
        p = subprocess.popen('rsync -av /etc/password/ /tmp'.split()
                             shell = False,
                                     stdout=subprocess.PIPE,
                                     stdderr=subprocess.PIPE)
        self.stdout, self.stdderr = p.communicate()

myclass = Myclass()
myclass.start()
myclass.join()
print myclass.stdout


#~~~~~~~~~~~~~~~~~~~~~~~~~#no thread

import subprocess

def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''

    # Poll process for new output until finished
    for line in iter(process.stdout.readline, ""):
        print line,
        output += line


    process.wait()
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else:
        raise Exception(command, exitCode, output)

execute(['ping', 'localhost'])






#~~~~~~~~~~~~~~~~~~~~~~~~#import getpass/pw
password = getpass.getpass('password fro %s' % opts.user)
try:
    #code uses password
except Exception, e:
    #a test to see if str(e) is
    # really an invalid password
    # error, if so tell user
    #and return or loop
    #else:
raise expection(e)
#Error raised in first place

#~~~~~~~~~~~~~~~~~~~~~~#xrysync



def rysyncBookContent(bookID, serverEnv):
    book path = []
    for books in booksIDs:
        bookPaths.append(options.bookDestDir + "/book" + str(b))
        arg = []
    for host in serverEnv['content.host']:
        args = ["rync", "-avs", "*.", "--include", "*.jpg", "--exclude", "*", "-e" "ssh"]
        args.extend(bookPaths)
        args.append("jill@" + host + ":/home/dsopfklsdjlv"])
        print "executing" + ' '.join(args)
        subprocess.call(args)