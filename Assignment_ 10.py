#!/usr/bin/env python
# coding: utf-8

# QUESTION 1
# 
# Ans:- 
# While shutil. copy() will copy a single file, shutil. copytree() will copy an entire folder and every folder and file contained in it.

# QUESTION 2
# 
# Ans:- 
# We can rename files using the os.rename()

# QUESTION 3
# 
# Ans:-
# The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files and folders.

# QUESTION 4
# 
# Ans:-
# The equivalent method in ZipFile for open() method of File objects is the ZipFile() constructor method.

# QUESTION 5

# In[1]:


import os
import shutil

def copy_files_with_extension(source_folder, target_folder, extension):
    """
    Copies all files with a given extension from a source folder and its subfolders to a target folder.
    """
    # Create the target folder if it does not already exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Traverse the source folder tree recursively
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            # Check if the file has the desired extension
            if filename.endswith(extension):
                # Construct the full path of the source file
                source_path = os.path.join(foldername, filename)

                # Construct the full path of the target file
                target_path = os.path.join(target_folder, filename)

                # Copy the file to the target folder
                shutil.copy(source_path, target_path)

# Example usage
source_folder = '/path/to/source/folder'
target_folder = '/path/to/target/folder'
extension = '.pdf'

copy_files_with_extension(source_folder, target_folder, extension)

