# 🕷 Selenium Excel Downloader

This project is a Python automation script that uses Selenium WebDriver to open a website, close a popup window, click the Excel export button, and automatically download an Excel file.  
The script uses webdriver-manager, so there is no need to manually install ChromeDriver.

---

## 🚀 Features
- Automated Chrome browser session  
- Closes the initial popup  
- Clicks the Export to Excel button  
- Downloads files into the excel_dir folder  
- Uses webdriver-manager for automatic driver handling  
- Clean and modular Python code 

---

## 📦 Installation

### 1. Clone the repository
```
git clone https://github.com/SamiraSiavash/selenium-excel-scraper.git
cd selenium-excel-downloader
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the script
```
python src/scraper.py
```

The script will:
1. Open the website  
2. Close the popup  
3. Trigger the Excel export  
4. Download the file into excel_dir

---

## 📁 Download Location
Downloaded Excel files are saved in:
```
excel_dir/
```
This folder is created automatically when the script runs.

---

## 🛠 Tech Stack
- Python  
- Selenium  
- WebDriver Manager  

---

## 📄 License
MIT License (optional)

---

## ✨ Author
**Samira Siavash**

🔗 GitHub: [https://github.com/SamiraSiavash](https://github.com/SamiraSiavash)

🔗 LinkedIn: [https://linkedin.com/in/samira-siavash](https://linkedin.com/in/samira-siavash)
