#using os module we can find the all folder and file 

import os
path = r"C:\Users\rajak\OneDrive\Desktop\Python"  # EXACT folder path

if not os.path.exists(path):
    print(" Path exist nahi karta:", path)
else:
    for root, dirs, files in os.walk(path):
        print("\n Folder:", root)

        for d in dirs:
            print("   ", d)

        for f in files:
            print("   ", f)
