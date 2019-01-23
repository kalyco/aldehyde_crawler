# Run me w $ python aldehydes.py
from selenium import webdriver
import os
import time
import urllib.request
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='output.log',level=logging.DEBUG)

wiki = 'https://en.m.wikipedia.org/wiki/Category%3AAldehydes'
directory = '/aldehyde_images'

def setUp():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	driver = webdriver.Chrome(chrome_options=options)
	driver.set_window_size(1120, 550)
	driver.get(wiki)

	return driver

def scrape():
	driver = setUp()
	wait = WebDriverWait(driver, 100)
	page = driver.find_element(By.ID, 'mw-pages')
	categories = page.find_elements(By.CLASS_NAME, 'mw-category-group')
	for category in categories:
		elems = category.find_elements_by_tag_name('a')
		print(category.text)
		for elem in elems:
			name = elem.text
			try:
				elem.click()
				wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'thumbimage')))
				img = driver.find_element(By.CLASS_NAME, 'thumbimage')
				filename = '/' + name + '.png'
				imgurl = img.get_attribute('src')
				driver.get(imgurl)
				imagefile = os.getcwd() + directory + filename
				print(imagefile)
				urllib.request.urlretrieve(imgurl, imagefile)
			finally:
				driver.back()
	driver.quit

scrape()
