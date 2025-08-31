# 🤖 Task Automation Scripts - CodeAlpha Task 3

A comprehensive automation suite that handles repetitive tasks including file organization, email extraction, and web scraping.

## 🎯 Project Overview
This project was developed as part of the **CodeAlpha Python Programming Internship - Task 3**.

## ✨ Features
This automation suite includes **three powerful automation tools**:

### 1. 📸 File Organizer
- **Moves all .jpg/.jpeg files** from source to destination folders
- **Automatic folder creation** with timestamps
- **Operation logging** with detailed reports
- **Sample file creation** for demonstration
- **Comprehensive error handling**

### 2. 📧 Email Extractor
- **Extracts email addresses** from text files using regex
- **Duplicate removal** while preserving order
- **Multiple output formats** (TXT and CSV)
- **Sample text file generation** for testing
- **Advanced email pattern matching**

### 3. 🌐 Web Scraper
- **Scrapes webpage titles** from multiple URLs
- **Predefined URL sets** for reliable testing
- **Custom URL input** capability
- **Professional request headers** to avoid blocking
- **Comprehensive error handling** for network issues

## 🔧 Key Concepts Used
- **os** - Operating system interface
- **shutil** - High-level file operations
- **re** - Regular expressions for pattern matching
- **requests** - HTTP library for web scraping
- **File handling** - Reading and writing various file formats
- **Error handling** - Robust exception management
- **Object-oriented programming** - Comprehensive class structure

## 📦 Requirements
```txt
requests>=2.28.0
```

## 🚀 How to Run
```bash
# Install requirements
pip install -r requirements.txt

# Run the automation suite
python CodeAlpha_TaskAutomationScripts.py
```

## 🛠️ Automation Tasks

### 📸 File Organizer Usage
```
📸 FILE ORGANIZER
Enter source folder path: /path/to/images
Found 5 .jpg files:
  1. photo1.jpg
  2. image.jpeg
  3. picture.jpg
Move 5 files to organized_images_20250831_153045? (y/n): y
✅ Moved: photo1.jpg
✅ Files moved successfully: 5/5
📁 Destination: automation_results/organized_images_20250831_153045/
```

### 📧 Email Extractor Usage
```
📧 EMAIL EXTRACTOR
📄 Reading file: sample_text.txt
🔍 Found 8 unique email addresses:
  1. info@company.com
  2. john.doe@example.com
  3. support@helpdesk.net
💾 Emails saved to: extracted_emails_20250831_153046.txt
💾 CSV format saved to: extracted_emails_20250831_153046.csv
```

### 🌐 Web Scraper Usage
```
🌐 WEB SCRAPER
🔍 Scraping titles from 3 URLs...
[1/3] Scraping: https://www.python.org
  ✅ Title: Welcome to Python.org
[2/3] Scraping: https://github.com
  ✅ Title: GitHub: Let's build from here
📊 Scraping Summary: ✅ Successful: 2/3
💾 Results saved to: scraped_titles_20250831_153047.txt
```

## 📁 Output Structure
```
automation_results/
├── organized_images_20250831_153045/
│   ├── photo1.jpg
│   ├── image.jpeg
│   └── picture.jpg
├── extracted_emails_20250831_153046.txt
├── extracted_emails_20250831_153046.csv
├── scraped_titles_20250831_153047.txt
├── file_operation_log_20250831_153045.txt
└── sample_text_with_emails.txt
```

## 🔄 Run All Tasks
The suite includes a "Run All Tasks" feature that executes all three automation scripts in sequence, perfect for comprehensive automation workflows.

## 🛡️ Error Handling
- **Network timeouts** for web scraping
- **File permission errors** for file operations
- **Invalid input validation** for all user inputs
- **Graceful failure recovery** with detailed error messages
- **Comprehensive logging** for troubleshooting

## 🏆 CodeAlpha Requirements Met
✅ Automates real-life repetitive tasks  
✅ File organizer moves .jpg files to new folders  
✅ Email extractor processes .txt files with regex  
✅ Web scraper extracts titles and saves them  
✅ Uses os, shutil, re, requests, file handling  

## 🎯 Technical Implementation
- **Modular design** with separate methods for each automation task
- **Professional user interface** with clear menus and feedback
- **Timestamped outputs** for organized result tracking
- **Multiple file format support** for versatile data export
- **Robust error handling** for production-ready reliability

## 📁 Files
- `CodeAlpha_TaskAutomationScripts.py` - Main automation suite implementation
- `Readme.md` - Project documentation

## 👨‍💻 Author
**CodeAlpha Python Programming Intern**

## 📧 Contact
- GitHub: https://github.com/srsudeeksha/Python_Internship_CodeAlpha/tree/main/CodeAlpha_Task3
- LinkedIn: www.linkedin.com/in/ranga-sudeeksha

---
*This project is part of the CodeAlpha Python Programming Internship program.*
