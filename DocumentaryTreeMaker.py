from dis import findlinestarts
import os, collections, pathlib
from os.path import isfile

#list full path to your workspace
directory = r"C:\Users\G\OneDrive - ekdls\!Programs\Python\Stuff\SameStructureStyleDocumenting\config"

#list full path to your desired location to place the output
output_directory = r"C:\Users\G\OneDrive - ekdls\!Programs\Python\Stuff\SameStructureStyleDocumenting\Testing"
print(output_directory)

#extension type 
extension_type = ".md" # use .md for github pages and other services that rely on .md files

###############################################
dq = collections.deque([directory])
stoppable = False

def finderskeepers(dqt):
    output_current_directory = os.path.relpath(dqt, directory)
    for object in os.listdir(dqt):
        item = os.path.join(current_path, object)
        if os.path.isfile(item):
            x = object.rsplit('.', 1)
            text_file = x[0] + extension_type
            open(os.path.join(output_directory, output_current_directory,text_file), "x")
        elif os.path.isdir(item):
            d = os.path.join(output_directory, output_current_directory, object)
            os.mkdir(d)
            dq.append(item)
        else:
            print("Unknown!")
        
while stoppable != True and len(dq) != 0:
    current_path = dq.popleft()
    finderskeepers(current_path)
    stoppable == True

print("Successful 🥺")


    