import os
import shutil
import time as t

def copyFiles(origin = "c:\\Users\\My HP\\Desktop\\FolderA\\",
              target = "c:\\Users\\My HP\\Desktop\\FolderB\\"):
    for f in os.listdir(origin):
        src = os.path.join(origin, f)
        dst = target
        if checkIfMod(src):
            shutil.copy2(src, dst)
            print (os.path.join(dst,f))

        
def checkIfMod(fname):
    past24 = t.time() - 24*60*60 
    if os.path.getmtime(fname) >= past24:
        return True
    
    return False

if __name__=='__main__':
    copyFiles()
