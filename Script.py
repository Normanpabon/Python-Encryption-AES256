import base64, os
import shutil as sht
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


defaultPath = os.getcwd()

def createFolders():    #checks if folders 'Input' and 'Decrypted' exists
    Te = 0
    Td = 0
    DirList = os.listdir()
    for dirs in DirList:
        if dirs == "Input":
            Te = 1
        if dirs == "Output":
            Td = 1
    if Te == 0:
        os.mkdir("Input")
    if Td == 0:
        os.mkdir("Output")

def PrintProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def ListAllFiles(): #part of progress bar


    InputRootFileCount = os.listdir()

    for file in InputRootFileCount:
        if os.path.isdir(file):
            InputRootFileCount.remove(file)


    return len(InputRootFileCount)
    '''
    returnToFolder = os.getcwd()

    print('DEBUG FOLDER'+str(os.getcwd()))
    FileCount = []
    FileList = os.listdir()
    for file in FileList:
        if os.path.isfile(file):
            FileCount.append(file)
        if os.path.isdir(file)
    '''



def GenerateKey():

    password_provided = input("Provide a safe password: ") # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = (password_provided[::-1]+password_provided[::-1]).encode() # Reverse password_provided by the user and concatenate with the same to generate the salt
    kdf = PBKDF2HMAC( algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


def EncryptFile(TotalFiles):
    os.chdir('Input')
    filesInput = os.listdir()
    key = GenerateKey()
    z = 0
    deleteFiles = int(input('\nWARNING: for security your old files will be deleted\n Do you want to continue ? \n 0. No  \n 1. Yes\n -- '))

    if  deleteFiles == 1:

        for x in filesInput:
            PrintProgressBar(iteration=z, total=TotalFiles, prefix = 'Encrypting:', suffix = 'Complete', length = 50)



            #Open the file to encrypt and read the data
            with open(x, 'rb') as file:
                Fdata = file.read()
            fernet = Fernet(key)
            EncryptedData = fernet.encrypt(Fdata)
            file.close()

            #Write the new file
            with open(x+'.wkt', 'wb') as file:
                file.write(EncryptedData)
                file.close()

            os.remove(x)
            z +=1
    else:
        exit()

    encryptedFiles = os.listdir()

    for y in encryptedFiles:
        sht.move(y ,defaultPath+"/Output/"+'/'+y)

    os.chdir(defaultPath)



def DecryptFile(TotalFiles):
    os.chdir('Input')
    filesInput = os.listdir()
    key = GenerateKey()
    z=0

    for x in filesInput:

        PrintProgressBar(iteration=z, total=TotalFiles, prefix = 'Decrypting:', suffix = 'Complete', length = 50)


        with open(x, 'rb') as file:
            Fdata = file.read()
            file.close()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(Fdata)
        outPutFile = x[:-4] # remove .wkt extention

        with open(outPutFile, 'wb') as file:
            file.write(decrypted)
            file.close()
        z =+1
        os.remove(x)

    decryptedFiles = os.listdir()

    for y in decryptedFiles:
        sht.move(y ,defaultPath+"/Output/"+'/'+y)

    os.chdir(defaultPath)


def main():

    FileCount = int(ListAllFiles())
    createFolders()
    print('\nFile encryption with AES-256')

    option = int(input('\nSelect a option: \n 1. Encrypt files \n 2. Decrypt files \n -- '))

    if option == 1:
        input('\nPut the files to encrypt in the "Input" folder and then press ENTER to continue')
        EncryptFile(FileCount)
    if option == 2:
        input('\nPut the files to decrypt in the "Input" folder and then press ENTER to continue')
        DecryptFile(FileCount)









main()





