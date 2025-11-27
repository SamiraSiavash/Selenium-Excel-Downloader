import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://mdp.ihio.gov.ir/"


def create_download_directory():
    current_directory = os.path.join(os.getcwd(), "excel_dir")
    os.makedirs(current_directory, exist_ok=True)
    return current_directory


def setup_driver(download_dir):
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enable": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--safebrowsing-disable-download-protection")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def download_excel(driver):
    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)

    close_button = driver.find_element(By.XPATH, '//*[@id="tool-1182-toolEl"]')
    close_button.click()
    time.sleep(1)

    export_button = driver.find_element(By.XPATH, '//*[@id="btnExcelExport-btnInnerEl"]')
    export_button.click()
    time.sleep(2)

    confirm_button = driver.find_element(By.XPATH, '//*[@id="button-1006-btnEl"]')
    confirm_button.click()

    time.sleep(30)
    print("Excel file downloaded successfully.")


def main():
    download_dir = create_download_directory()
    driver = setup_driver(download_dir)
    try:
        download_excel(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
