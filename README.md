# Week 2 RISCV Assignments

This repository contains Python-based solutions for two assignments focused on file handling and automation.

---

## Assignment 1: Extract ZIP Files

### Purpose:
Recursively search for all `.zip` files in a directory and extract them into their respective directories. If a `.zip` file is corrupted, it is skipped.

### How to Run:

1. Place your `.zip` files in the desired directory.
2. Run the script:
   ```bash
   python extract_zip_files.py

## Assignment 2: Copy Listed Files

### Purpose:
Search for specific files (listed in the script) in a given directory. If found, the script will create a folder named after the file (without the extension) in the `output/` directory and copy the file there. If not found, a warning message is displayed.

### How to Run:

1. Modify the `files_to_find` list in the script to specify the files you want to search for.
2. Run the script:
   ```bash
   python copy_listed_files.py
