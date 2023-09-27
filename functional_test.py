from selenium import webdriver

chrome = "chromedriver.exe"
browser = webdriver.Chrome(chrome)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
