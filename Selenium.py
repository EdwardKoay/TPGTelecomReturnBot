

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

def main(CN, CID, SN):
    excel_file = 'C:/Users/T6433677/Desktop/2021 09 9 Returns.xlsm'
    options = Options()
    options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\T6433677\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe')
    driver.get("https://google.com/ncr")

    df = pd.DataFrame(CN, CID, SN)
    df.to_excel(excel_file)


if __name__ == '__main__':
    main()



