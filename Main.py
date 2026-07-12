import os
import create_json
import create_baseline
import integrity_check

val=int(input("Choose one option:\n1. Create Baseline\n2. Verify Integrity\n"))
folder=input("Enter Folder path: ").strip()
try:
    files=os.listdir(folder)
except FileNotFoundError:
    print("Enter a valid path. Try again!")
    exit()
if val==1 :
    data=create_baseline.h(folder,files)
    create_json.j_son(data)
    print("Baseline created successfully")

elif val==2:
    print("\nVerifying the integrity of yours files")
    integrity_check.check(folder,files)
    

            
