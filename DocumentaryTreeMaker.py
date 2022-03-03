import os, collections, pathlib
from os.path import isfile

#list full path to your workspace
directory = r"C:\Users\G\!\Arcadanee\Garca\Das\daseven"

#list full path to your desired location to place the output
output_directory = r"C:\Users\G\!\Arcadanee\Garca\Docs\hi"

#extension type 
extension_type = ".md" # use .md for github pages and other services that rely on .md files

###############################################
dq = collections.deque([directory])
stoppable = False


def finderskeepers(dqt):
    output_current_directory = os.path.relpath(dqt, directory)
    
    for object in os.listdir(dqt):
        item = os.path.join(current_path, object)
        if os.path.isfile(item) and not object.startswith('.'):
            x = object.rsplit('.', 1)
            text_file = x[0] + extension_type
            try:
                open(os.path.join(output_directory, output_current_directory,text_file), "x")
            except FileExistsError:
                text_file = x[0] +  "-" + x[1] + extension_type 
                open(os.path.join(output_directory, output_current_directory, text_file), "x")


        elif os.path.isdir(item) and not object.startswith('.'):
            d = os.path.join(output_directory, output_current_directory, object)
            os.mkdir(d)
            dq.append(item)
        else:
            print("Unknown! (It's probably a hidden file) and we're ignoring it because it wants to stay hidden: ", item)
        
while stoppable != True and len(dq) != 0:
    current_path = dq.popleft()
    finderskeepers(current_path)
    stoppable == True



print("Successful 🥺")


    
