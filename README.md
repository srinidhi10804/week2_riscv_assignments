### Week 2 RISCV Assignments
This repository contains Python-based solutions for two assignments focused on file handling and automation.

### Assignment 1: Extract ZIP Files
**Purpose:**
Recursively search for all .zip files in a directory and extract them into their respective directories. If a .zip file is corrupted, it is skipped.

**How to Run:**
Place your .zip files in the desired directory.
**Run the script:**
python extract_zip_files.py

**Assignment 2: Copy Listed Files**
**Purpose:**
Search for specific files (listed in the script) in a given directory. If found, the script will create a folder named after the file (without the extension) in the output/ directory and copy the file there. If not found, a warning message is displayed.

**How to Run:**
Modify the files_to_find list in the script to specify the files you want to search for.
**Run the script:**
python copy_listed_files.py

**Assignment 3: Collect Failed Subdirectories**
**Purpose:**
Traverse all subdirectories to identify those containing a STATUS_FAILED file. Each such subdirectory is copied in its entirety into a new folder named failed_subdirectories located in the main directory.

**How to Run:**
Place the script in your working directory.

**Run the script:**
collect_failed.sh

**Assignment 4: Copy Matching Directories**
**Purpose:**
Find all subdirectories whose names start with test_v and copy them (with all their contents) into a specified destination directory. The destination directory will be created if it does not already exist.

**How to Run:**
Set the parent and destination directories in the script.

**Run the script:**
test_v1

**Assignment 5: Rename and Copy Co-directories**
**Purpose:**
Traverse all co-directories under the parent directory. For each co-directory that contains a dut subdirectory:

Rename all .elf files inside dut to match the co-directory's name (e.g., add.elf if the co-directory is add).

Copy the entire co-directory to a destination directory.

Skip copying any ref subdirectory inside the co-directory.

**How to Run:**
Adjust the parent and destination directory paths in the script.

Run the script:
python rename_and_copy_5.py
