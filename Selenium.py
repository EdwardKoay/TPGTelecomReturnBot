from selenium import webdriver


path = "C:/Users/T6433677/PycharmProjects/pythonProject/geckodriver.exe"
driver = webdriver.Firefox(path)
driver.get("http://www.yahoo.com")
driver.close()
driver.quit()
#if __name__ == '__main__':
    #main()

#def main(CN, CID, SN):
