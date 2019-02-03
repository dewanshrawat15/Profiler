from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import system, name
import time
from getpass import getpass
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def	search():
	clear
	name = input('enter the input : ')
	language = input('Enter Language Code according to ISO 639-1 Nomenclauture Conventions : ')
	browser = webdriver.Chrome()
	site_url = "https://www.wikipedia.org/"
	browser.get(site_url)
	search_box = browser.find_element_by_id('searchInput')
	search_box.send_keys(name)
	browser.find_element_by_xpath("//select[@id='searchLanguage']/option[@value='%s']" % language).click()
	search_button = browser.find_element_by_class_name('pure-button')
	search_button.click()
	
	time.sleep(20)


search()
