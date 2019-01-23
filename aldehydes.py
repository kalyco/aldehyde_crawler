# Run me w $ python aldehydes.py
from selenium import webdriver
import os
import urllib.request
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='output.log',level=logging.DEBUG)

wiki = 'https://en.m.wikipedia.org/wiki/Category%3AAldehydes'

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
directory = '/aldehyde_images'

def scrape(url):
	try:
		driver.get(url)
		page = driver.find_element(By.ID, 'mw-pages')
		categories = page.find_elements(By.CLASS_NAME, 'mw-category-group')
		# for category in categories:
		category = categories[0]
		elems = category.find_elements_by_tag_name('a')
		# for elem in elems:
		elem = elems[0]
		print(elem.text)
		elem.click()
		wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'thumbimage')))
		img = driver.find_element(By.CLASS_NAME, 'thumbimage')
		name = img.text
		filename = '/something.png'
		imgurl = img.get_attribute('src')
		driver.get(imgurl)
		wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'transparent')))
		imagefile = os.getcwd() + directory + filename
		print(imagefile)
		urllib.request.urlretrieve(imgurl, imagefile)
	finally:
		driver.close
		driver.quit

scrape(wiki)
