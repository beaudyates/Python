import os, shutil

origin = "c:\\Users\\My HP\\Desktop\\Folder A\\"
target = "c:\\Users\\My HP\\Desktop\\Folder B\\"

for f in os.listdir(origin):
    src = origin + f
    dst = target + f
    shutil.move(src, dst)
    print (dst + f)

