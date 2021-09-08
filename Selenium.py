

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():

    options = Options()
    options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\T6433677\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe')
    driver.get("https://google.com/ncr")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    print(first_result.get_attribute("textContent"))

if __name__ == '__main__':
    main()

#
#path = "C:/Users/T6433677/PycharmProjects/pythonProject/geckodriver.exe"
#driver = webdriver.Firefox(path)
#driver.get("http://www.yahoo.com")
#driver.close()
#driver.quit()

