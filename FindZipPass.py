import pyzipper
def func1():
    
    with open('wordlist.txt', 'r') as f:
        myNames = [line.strip() for line in f]
    i=0
    for word in myNames:
       i=i+1
       try:
        with pyzipper.AESZipFile('secret.zip', 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode(word))
            print("successsssss: {}".format(word))
            return;
       except NameError:
          print("NameError : ")   
       except:
          print(i)
func1()
    
