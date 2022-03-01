from dis import findlinestarts
import os, collections, pathlib
from os.path import isfile

#list full path to your workspace
directory = r""

#list full path to your desired location to place the output
output_directory = r""
print(output_directory)

#extension type 
extension_type = ".md" # use .md for github pages and other services that rely on .md files

###############################################
dq = collections.deque([directory])
stoppable = False
beentheredonethat = False

def finderskeepers(dqt):
    for object in os.listdir(dqt):
        print(object)
        item = os.path.join(current_path, object)
        print("path ITEM", item)
        if os.path.isfile(item):
            print(item + " is a file")
            x = object.rsplit('.', 1)
            text_file = x[0] + extension_type
            print("text file: ", text_file)
            output_current_directory = os.path.relpath(dqt, directory)
            print("LOOKA THISSSS : ", output_current_directory)
            t = open(os.path.join(output_directory + "\\" + output_current_directory,text_file), "x")
            
        elif os.path.isdir(item):
            print(item + " is a dir")
            print("After attempting to append: ", dq)
            d = os.path.join(output_directory, object)
            os.mkdir(d)
            dq.append(item)

    
        else:
            print("Unknown!")
        


while stoppable != True and len(dq) != 0:
    print("Deque inventory: ", dq)
    current_path = dq[0]

    finderskeepers(dq[0])
    lol = dq.popleft()
    print("BEEN THERE TRUE")

    
print("End of Program")


    