import hashlib
import os

def h(folder,files):
    data={}
    for file in files:
        sha=hashlib.sha256()
        pa=os.path.join(folder,file)
        with open(pa,"rb") as f:
            chunk=f.read(4096)
            while chunk:
                sha.update(chunk)
                chunk=f.read(4096)
        hash=sha.hexdigest()
        data[file]=hash
    return data
