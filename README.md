﻿# Day7-File-Handling-projects
#  Python File Handling & Automation Projects 

This repository contains beginner-friendly automation projects built using Python's file handling and CSV modules.
---

##  Projects Included

### 1. Auto Note Writer
**Description:**  
Adds user notes with a timestamp into a text file.

**Skills Used:**  
- `datetime` for current date/time  
- File writing with `open("a")` mode
- 
###  2. Log Scanner & Cleaner
**Description:**  
Scans a log file, finds lines containing `error` or `warning`, replaces them with `ALERT`, and counts the total.

**Skills Used:**  
- `re.sub`, `re.search`  
- Case-insensitive pattern matching  
- File read/write and text processing


###  3. Batch File Renamer
**Description:**  
Renames all `.txt` files in a folder by adding a prefix `renamed_`.

**Skills Used:**  
- `os.listdir()`  
- `os.path.join()`  
- `os.rename()`


### 4. Attendance CSV Writer
**Description:**  
Writes employee attendance into a CSV file using headers.

**Skills Used:**  
- `csv.DictWriter()`  
- Writing structured data to `.csv`

###  5. CSV Sales Analyzer
**Description:**  
Reads sales data from a CSV file and calculates the total sales for each product.

**Skills Used:**  
- `csv.DictReader()`  
- Basic math and data parsing


##  How to Run

1. Make sure you have Python installed.
2. Open terminal or VS Code in the project folder.
3. Run each script individually:
   ```bash
   python auto_note_writer.py
   python log_cleaner.py

  
 ### Topics Covered
File Read & Write

Search & Replace using Regex

Working with Folders (move/rename/delete)

CSV Read/Write using csv.DictReader & DictWriter

 ### Author
Ganesh – Python Automation Learner 
Connect with me on Linkedin
https://www.linkedin.com/in/ganesh-596306371/

