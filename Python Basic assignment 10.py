#!/usr/bin/env python
# coding: utf-8
1. How do you distinguish between shutil.copy() and shutil.copytree()?
2. What function is used to rename files??
3. What is the difference between the delete functions in the send2trash and shutil modules?
4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
Q.1 How do you distinguish between shutil.copy() and shutil.copytree()?
Sol: copy() will copy a single file, shutil. copytree() will copy an entire folder and every folder and file contained in it. Calling shutil. copytree( source, destination ) will copy the folder at the path source , along with all of its files and subfolders, to the folder at the path destination .Q. 2. What function is used to rename files??
Sol: Python rename() file is a method used to rename a file or a directory in Python programming. The Python rename() file method can be declared by passing two arguments named src (Source) and dst (Destination).Q.3  What is the difference between the delete functions in the send2trash and shutil modules?
sol: Delete functions in Send2trash module is used to move files to the recycle bin or trash rather than permanently deleting them.
## The os module provides a portable way of interacting with the operating system.
To delete a single file with os.remove(), pass the path to the file as an argument:Q 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

sol: We have to open Zip files in write mode to write files to the archive file. It overrides all the existing files in the Zip. open() method is is equivalent to File objects’ open() method
# In[6]:


'''Q.5 5. Create a programme that searches a folder tree for files with a certain file extension 
(such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.'''


#!/usr/bin/env python3

# Write a program that walks through a folder tree 
# and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

#!/usr/bin/env python3

# Write a program that walks through a folder tree 
# and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import os, shutil

def selectiveCopy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
            fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.php', '.py']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:




