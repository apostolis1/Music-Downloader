from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request
import re 
import os
import time

class UrlExtractor:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
    
    def __del__(self):
        self.driver.close()
    
    def extract(self):
        uniqueUrls = []
        self.driver.get(self.url)
        items = self.driver.find_elements_by_xpath("//a[@href]")
        prevLast = items[0]

        while True:
            contents = self.driver.find_element_by_id("contents")
            print(contents.size)
            items = self.driver.find_elements_by_xpath("//a[@href]")
            for item in items:
                currentUrl = item.get_attribute("href")
                if currentUrl not in uniqueUrls:
                    uniqueUrls.append(currentUrl)
                    last_item = item
            # self.driver.execute_script("arguments[0].scrollIntoView();", last_item)
            self.driver.execute_script("window.scrollTo(0, Math.max(document.documentElement.scrollHeight, document.body.scrollHeight, document.documentElement.clientHeight));")
            if last_item == prevLast:
                break
            prevLast = last_item


        referenceUrls = list(filter(lambda x: "watch" in x, uniqueUrls))
        return referenceUrls

if __name__ == "__main__":
    
    mybot = UrlExtractor("YOUR_PLAYLIST_URL_HERE")
    mylist = mybot.extract()
    f = open(r"YOUR_txt_FILE_HERE", 'w')
    for i in mylist:
        f.write(i+'\n')
    f.close()