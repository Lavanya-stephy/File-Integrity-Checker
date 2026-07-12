import hashlib
import json
import os
import modify

def check(folder,files):
    new_hash={}
    with open("baseline.json","r") as f:
        old_hash=json.load(f)

    for file in files:
        sha=hashlib.sha256()
        pa=os.path.join(folder,file)
        with open(pa,"rb") as f:
            chunk=f.read(4096)
            while chunk:
                sha.update(chunk)
                chunk=f.read(4096)
        hash=sha.hexdigest()
        new_hash[file]=hash
    print("-"*130)
    print()
    modify.compare_hashes(old_hash,new_hash)
    print()
    print("-"*130)
