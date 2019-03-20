from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import system, name
import time
import re
from getpass import getpass
import string
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def	search():
	clear()
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
	elem_img = browser.find_element_by_xpath("""//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td/a/img""")
	img_url = elem_img.get_attribute('src')
	page_title = browser.title
	page_title = re.sub(' - Wikipedia', '', page_title)
	elem_txt = browser.find_element_by_xpath("""//*[@id="mw-content-text"]/div/p[3]""")
	para = elem_txt.text
	t = ''
	for i in para:
		for j in i:
			if not (j.isdigit()):
				t = t + j
	strl = t
	var1 = re.sub(r'[?|$|.|!]',r'',para)
	var = re.sub(r'[^a-zA-Z0-9 ]',r'', var1)

	outline = """
		<!DOCTYPE html>
		<html>
		<head>
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
			<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
			<title>"""+page_title+"""</title>
		</head>
		<style type="text/css">

		.container{
			background-color: #e74c3c;
			font-size: ;
			padding: 100px 0 160px 0;
        }

		</style>
		<body>
		<br><br>
		<div class="profile">
			<div class="container">
				<div class="row">
					<center>
						<div class="col-md-4 col-md-offset-4">
							<h1>PROFILER</h1>
							<br><br><br><br>
							<img src=" """+img_url+""" " class="img-responsive">
						</div>
					</center>
				</div>
				<br><br>
				<div class="row">
					<div class="col-md-8 col-md-offset-2 text-center">
						"""+str(var)+"""
					</div>
				</div>
			</div>
		</div>
		</body>
		</html>
	"""
	f = open("profile.html", "w")
	f.write(outline)
	f.close()
	browser.close()
	
	

search()
