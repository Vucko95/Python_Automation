from selenium import webdriver
PATH = "C:\Users\ronal\Documents\GitHub\Python_Automation\chromedriver.exe"
# PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://automated.pythonanywhere.com")
