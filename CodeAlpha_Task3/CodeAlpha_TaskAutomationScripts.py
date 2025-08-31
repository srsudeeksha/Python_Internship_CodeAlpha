"""
Task Automation with Python Scripts - CodeAlpha Task 3
Collection of automation scripts for repetitive tasks.

Author: [Your Name]
Project: CodeAlpha Python Programming Internship
Task: Task 3 - Task Automation with Python Scripts

This file contains three automation scripts:
1. File Organizer - Move all .jpg files from a folder to a new folder
2. Email Extractor - Extract email addresses from text files
3. Web Scraper - Scrape webpage titles and save them

Key Concepts Used: os, shutil, re, requests, file handling
"""

import os
import shutil
import re
import requests
from datetime import datetime
import sys

class TaskAutomationSuite:
    """A comprehensive task automation toolkit"""
    
    def __init__(self):
        """Initialize the automation suite"""
        self.current_directory = os.getcwd()
        self.results_folder = "automation_results"
        self.ensure_results_folder()
    
    def ensure_results_folder(self):
        """Create results folder if it doesn't exist"""
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)
            print(f"📁 Created results folder: {self.results_folder}")
    
    def display_welcome(self):
        """Display welcome message and available automation tasks"""
        print("🤖 TASK AUTOMATION SUITE - CodeAlpha Task 3")
        print("=" * 60)
        print("Automate your repetitive tasks with Python!")
        print("\n🛠️  Available Automation Tasks:")
        print("1. 📸 File Organizer - Move .jpg files to organized folders")
        print("2. 📧 Email Extractor - Extract emails from text files")
        print("3. 🌐 Web Scraper - Scrape webpage titles")
        print("4. 🏃 Run All Tasks - Execute all automations")
        print("5. ❌ Exit")
        print("=" * 60)
    
    def display_menu(self):
        """Display the main menu"""
        print("\n🎯 AUTOMATION MENU")
        print("-" * 30)
        print("1. 📸 File Organizer")
        print("2. 📧 Email Extractor")
        print("3. 🌐 Web Scraper")
        print("4. 🏃 Run All Tasks")
        print("5. ❌ Exit")
        print("-" * 30)

    # ============================================================================
    # TASK 1: FILE ORGANIZER - Move .jpg files to organized folders
    # ============================================================================
    
    def file_organizer(self):
        """Move all .jpg files from source folder to destination folder"""
        print("\n📸 FILE ORGANIZER")
        print("=" * 50)
        print("This tool moves all .jpg files from a source folder to a destination folder.")
        
        # Get source folder
        source_folder = input("\nEnter source folder path (or press Enter for current directory): ").strip()
        if not source_folder:
            source_folder = self.current_directory
        
        if not os.path.exists(source_folder):
            print(f"❌ Source folder '{source_folder}' does not exist!")
            return
        
        # Create destination folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest_folder = os.path.join(self.results_folder, f"organized_images_{timestamp}")
        
        try:
            os.makedirs(dest_folder, exist_ok=True)
            print(f"📁 Created destination folder: {dest_folder}")
            
            # Find all .jpg files
            jpg_files = []
            for file in os.listdir(source_folder):
                if file.lower().endswith(('.jpg', '.jpeg')):
                    jpg_files.append(file)
            
            if not jpg_files:
                print("❌ No .jpg files found in the source folder!")
                # Create sample .jpg files for demonstration
                self.create_sample_jpg_files(source_folder)
                return
            
            print(f"\n🔍 Found {len(jpg_files)} .jpg files:")
            for i, file in enumerate(jpg_files, 1):
                print(f"  {i}. {file}")
            
            # Confirm operation
            confirm = input(f"\nMove {len(jpg_files)} files to {dest_folder}? (y/n): ").lower().strip()
            
            if confirm in ['y', 'yes']:
                moved_count = 0
                failed_count = 0
                
                for file in jpg_files:
                    source_path = os.path.join(source_folder, file)
                    dest_path = os.path.join(dest_folder, file)
                    
                    try:
                        shutil.move(source_path, dest_path)
                        print(f"✅ Moved: {file}")
                        moved_count += 1
                    except Exception as e:
                        print(f"❌ Failed to move {file}: {e}")
                        failed_count += 1
                
                # Summary
                print(f"\n📊 Operation Summary:")
                print(f"✅ Files moved successfully: {moved_count}")
                print(f"❌ Files failed to move: {failed_count}")
                print(f"📁 Destination: {dest_folder}")
                
                # Create operation log
                self.create_file_operation_log(jpg_files, dest_folder, moved_count, failed_count)
                
            else:
                print("❌ Operation cancelled.")
                
        except Exception as e:
            print(f"❌ Error during file organization: {e}")
    
    def create_sample_jpg_files(self, folder):
        """Create sample .jpg files for demonstration"""
        sample_files = ["sample1.jpg", "sample2.jpg", "photo.jpeg"]
        print(f"\n💡 Creating sample .jpg files in {folder} for demonstration...")
        
        for filename in sample_files:
            filepath = os.path.join(folder, filename)
            try:
                with open(filepath, 'w') as f:
                    f.write("Sample image file for automation demo")
                print(f"📄 Created: {filename}")
            except Exception as e:
                print(f"❌ Failed to create {filename}: {e}")
        
        print("✅ Sample files created! Run File Organizer again to see it in action.")
    
    def create_file_operation_log(self, files, destination, moved, failed):
        """Create a log file for the file operation"""
        log_filename = os.path.join(self.results_folder, f"file_operation_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        try:
            with open(log_filename, 'w') as log_file:
                log_file.write("FILE ORGANIZATION LOG\n")
                log_file.write("=" * 50 + "\n")
                log_file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.write(f"Destination: {destination}\n")
                log_file.write(f"Total files processed: {len(files)}\n")
                log_file.write(f"Successfully moved: {moved}\n")
                log_file.write(f"Failed to move: {failed}\n\n")
                
                log_file.write("FILES PROCESSED:\n")
                log_file.write("-" * 30 + "\n")
                for i, file in enumerate(files, 1):
                    log_file.write(f"{i}. {file}\n")
            
            print(f"📄 Operation log saved: {log_filename}")
            
        except Exception as e:
            print(f"❌ Failed to create log file: {e}")

    # ============================================================================
    # TASK 2: EMAIL EXTRACTOR - Extract emails from text files
    # ============================================================================
    
    def email_extractor(self):
        """Extract all email addresses from text files"""
        print("\n📧 EMAIL EXTRACTOR")
        print("=" * 50)
        print("This tool extracts email addresses from text files.")
        
        # Get input file
        input_file = input("\nEnter path to text file (or press Enter to create sample): ").strip()
        
        if not input_file:
            input_file = self.create_sample_text_file()
            if not input_file:
                return
        
        if not os.path.exists(input_file):
            print(f"❌ File '{input_file}' does not exist!")
            return
        
        try:
            # Read file content
            with open(input_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            print(f"📄 Reading file: {input_file}")
            print(f"📏 File size: {len(content)} characters")
            
            # Extract email addresses using regex
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, content)
            
            # Remove duplicates while preserving order
            unique_emails = list(dict.fromkeys(emails))
            
            if not unique_emails:
                print("❌ No email addresses found in the file!")
                return
            
            print(f"\n🔍 Found {len(unique_emails)} unique email addresses:")
            for i, email in enumerate(unique_emails, 1):
                print(f"  {i}. {email}")
            
            # Save results
            self.save_extracted_emails(unique_emails, input_file)
            
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    
    def create_sample_text_file(self):
        """Create a sample text file with email addresses"""
        sample_filename = os.path.join(self.results_folder, "sample_text_with_emails.txt")
        
        sample_content = """
        Sample Text File with Email Addresses
        =====================================
        
        Contact us at info@company.com for more information.
        
        Our team members:
        - John Doe: john.doe@example.com
        - Jane Smith: jane.smith@company.org  
        - Bob Wilson: bob.wilson123@gmail.com
        - Alice Johnson: alice.johnson@university.edu
        
        For support, email support@helpdesk.net or call our office.
        You can also reach our sales team at sales@business.co.uk
        
        Invalid emails (should not be extracted):
        - notanemail@
        - @invalid.com
        - plaintext
        
        More contacts:
        - tech@startup.io
        - admin@website.gov
        - contact@nonprofit.org
        """
        
        try:
            with open(sample_filename, 'w', encoding='utf-8') as file:
                file.write(sample_content)
            
            print(f"📄 Created sample file: {sample_filename}")
            return sample_filename
            
        except Exception as e:
            print(f"❌ Failed to create sample file: {e}")
            return None
    
    def save_extracted_emails(self, emails, source_file):
        """Save extracted emails to a file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = os.path.join(self.results_folder, f"extracted_emails_{timestamp}.txt")
        
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write("EXTRACTED EMAIL ADDRESSES\n")
                file.write("=" * 50 + "\n")
                file.write(f"Source file: {source_file}\n")
                file.write(f"Extraction date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total emails found: {len(emails)}\n\n")
                
                file.write("EMAIL ADDRESSES:\n")
                file.write("-" * 30 + "\n")
                for i, email in enumerate(emails, 1):
                    file.write(f"{i}. {email}\n")
            
            print(f"💾 Emails saved to: {output_filename}")
            
            # Also create CSV format
            csv_filename = os.path.join(self.results_folder, f"extracted_emails_{timestamp}.csv")
            with open(csv_filename, 'w', encoding='utf-8') as csvfile:
                csvfile.write("Email_Address\n")
                for email in emails:
                    csvfile.write(f"{email}\n")
            
            print(f"💾 CSV format saved to: {csv_filename}")
            
        except Exception as e:
            print(f"❌ Failed to save emails: {e}")

    # ============================================================================
    # TASK 3: WEB SCRAPER - Scrape webpage titles
    # ============================================================================
    
    def web_scraper(self):
        """Scrape titles from web pages"""
        print("\n🌐 WEB SCRAPER")
        print("=" * 50)
        print("This tool scrapes titles from web pages.")
        
        # Predefined URLs for demonstration
        default_urls = [
            "https://www.python.org",
            "https://github.com",
            "https://stackoverflow.com",
            "https://www.google.com",
            "https://www.wikipedia.org"
        ]
        
        print("\n🔗 Choose an option:")
        print("1. Use predefined URLs (recommended)")
        print("2. Enter custom URLs")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            urls = default_urls
            print(f"\n📋 Using {len(urls)} predefined URLs:")
            for i, url in enumerate(urls, 1):
                print(f"  {i}. {url}")
        else:
            urls = self.get_custom_urls()
            if not urls:
                return
        
        # Scrape titles
        results = self.scrape_titles(urls)
        
        if results:
            self.save_scraped_titles(results)
    
    def get_custom_urls(self):
        """Get custom URLs from user input"""
        urls = []
        print("\nEnter URLs to scrape (press Enter without typing to finish):")
        
        while True:
            url = input(f"URL {len(urls) + 1}: ").strip()
            if not url:
                break
            
            # Basic URL validation
            if not (url.startswith('http://') or url.startswith('https://')):
                url = 'https://' + url
            
            urls.append(url)
            print(f"✅ Added: {url}")
        
        if not urls:
            print("❌ No URLs provided!")
            return None
        
        return urls
    
    def scrape_titles(self, urls):
        """Scrape titles from the provided URLs"""
        print(f"\n🔍 Scraping titles from {len(urls)} URLs...")
        print("-" * 50)
        
        results = []
        
        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] Scraping: {url}")
            
            try:
                # Set headers to avoid being blocked
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                
                # Make request with timeout
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                # Extract title using regex
                title_match = re.search(r'<title[^>]*>([^<]+)</title>', response.text, re.IGNORECASE)
                
                if title_match:
                    title = title_match.group(1).strip()
                    title = re.sub(r'\s+', ' ', title)  # Clean up whitespace
                    print(f"  ✅ Title: {title}")
                    
                    results.append({
                        'url': url,
                        'title': title,
                        'status': 'Success',
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                else:
                    print(f"  ⚠️  No title found")
                    results.append({
                        'url': url,
                        'title': 'No title found',
                        'status': 'No Title',
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                
            except requests.exceptions.RequestException as e:
                print(f"  ❌ Error: {e}")
                results.append({
                    'url': url,
                    'title': f'Error: {str(e)}',
                    'status': 'Failed',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            
            except Exception as e:
                print(f"  ❌ Unexpected error: {e}")
                results.append({
                    'url': url,
                    'title': f'Unexpected error: {str(e)}',
                    'status': 'Failed',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
        
        # Summary
        successful = sum(1 for r in results if r['status'] == 'Success')
        print(f"\n📊 Scraping Summary:")
        print(f"✅ Successful: {successful}/{len(urls)}")
        print(f"❌ Failed: {len(urls) - successful}/{len(urls)}")
        
        return results
    
    def save_scraped_titles(self, results):
        """Save scraped titles to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save to text file
        txt_filename = os.path.join(self.results_folder, f"scraped_titles_{timestamp}.txt")
        try:
            with open(txt_filename, 'w', encoding='utf-8') as file:
                file.write("WEB SCRAPING RESULTS\n")
                file.write("=" * 60 + "\n")
                file.write(f"Scraping date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total URLs processed: {len(results)}\n\n")
                
                for i, result in enumerate(results, 1):
                    file.write(f"{i}. URL: {result['url']}\n")
                    file.write(f"   Title: {result['title']}\n")
                    file.write(f"   Status: {result['status']}\n")
                    file.write(f"   Time: {result['timestamp']}\n")
                    file.write("-" * 60 + "\n")
            
            print(f"💾 Results saved to: {txt_filename}")
            
        except Exception as e:
            print(f"❌ Failed to save results: {e}")
    
    # ============================================================================
    # MAIN PROGRAM LOGIC
    # ============================================================================
    
    def run_all_tasks(self):
        """Execute all automation tasks in sequence"""
        print("\n🏃 RUNNING ALL AUTOMATION TASKS")
        print("=" * 50)
        
        print("1. Starting File Organizer...")
        self.file_organizer()
        
        print("\n" + "="*50)
        print("2. Starting Email Extractor...")
        self.email_extractor()
        
        print("\n" + "="*50)
        print("3. Starting Web Scraper...")
        self.web_scraper()
        
        print("\n🎉 All automation tasks completed!")
    
    def run(self):
        """Main program loop"""
        self.display_welcome()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == '1':
                    self.file_organizer()
                elif choice == '2':
                    self.email_extractor()
                elif choice == '3':
                    self.web_scraper()
                elif choice == '4':
                    self.run_all_tasks()
                elif choice == '5':
                    print("\n👋 Thank you for using Task Automation Suite!")
                    print("🤖 Keep automating those repetitive tasks!")
                    break
                else:
                    print("❌ Invalid choice! Please enter 1-5.")
                
                # Pause before showing menu again
                if choice in ['1', '2', '3', '4']:
                    input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")

def display_project_info():
    """Display project information"""
    print("\n" + "=" * 70)
    print("PROJECT INFORMATION")
    print("=" * 70)
    print("Project: Task Automation with Python Scripts")
    print("Task: CodeAlpha Task 3")
    print("Description: Automate repetitive tasks with Python")
    print("Features:")
    print("• File Organizer - Move .jpg files to organized folders")
    print("• Email Extractor - Extract emails from text files using regex")
    print("• Web Scraper - Scrape webpage titles and save results")
    print("• Comprehensive error handling and logging")
    print("• Multiple output formats (TXT, CSV)")
    print("Key Concepts: os, shutil, re, requests, file handling")
    print("=" * 70)

def main():
    """Main function to start the task automation suite"""
    try:
        # Display project information
        display_project_info()
        input("\nPress Enter to start the Task Automation Suite...")
        
        # Create and run automation suite
        automation = TaskAutomationSuite()
        automation.run()
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please restart the program.")

if __name__ == "__main__":
    main()