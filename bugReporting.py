import re
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog

print("  _                 _____                       _   \n\
 | |               |  __ \                     | |  \n\
 | |__  _   _  __ _| |__) |___ _ __   ___  _ __| |_ \n\
 | '_ \| | | |/ _` |  _  // _ \ '_ \ / _ \| '__| __|\n\
 | |_) | |_| | (_| | | \ \  __/ |_) | (_) | |  | |_ \n\
 |_.__/ \__,_|\__, |_|  \_\___| .__/ \___/|_|   \__|\n\
               __/ |          | |                   \n\
              |___/           |_|                   \n")

print("author: ttiapras")
print("date  : 13/12/22",end='\n\n')

# Take directory
directory_root = Tk()
directory_root.withdraw()
ContainingDir = filedialog.askdirectory()
if(ContainingDir == ''):
    exit()
#create bug reporting csv
ContainingDir = Path(ContainingDir)
output = open(ContainingDir/"bugs.csv","w+")
output.write("Path:"+str(ContainingDir)+'\n')
output.write("File,Line,Owner,Description\n")

#suffixes to open
suffix_val = ['.c','.h']
print("Files scanned:")

#Iterate through files
for filePath in ContainingDir.iterdir():
    if(filePath.suffix not in suffix_val):
        continue
    
    fd     = open(filePath,"r")
    line = '\n'
    lineN=0
    bugsInFile = False
    while(line!=''):
        line = fd.readline()
        lineN+=1
        bugs = re.findall("/\*.*\[!\]\[(.*)\]\s*(.*)\*/", line)
        for (owner,descr) in bugs:
            output.write(filePath.name+","+str(lineN)+","+str(owner)+','+str(descr)+'\n')
            bugsInFile = True
    fd.close()
    if bugsInFile:
        print("[+] "+filePath.name)
    else:
        print("[-] "+filePath.name)

output.close()
input("Press enter to exit:")