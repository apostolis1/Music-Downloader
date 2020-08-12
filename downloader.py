from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import urllib.request
import re 
import os
import UrlExtractor


class Downloader:
    def __init__(self, downloadLocation, maxTime = 20):
        #This part of the code is used to decide where to download files
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : downloadLocation}
        chrome_options.add_experimental_option('prefs', prefs)
    
        self.downloadSite = "https://ytmp3.cc/en13/"
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.MAX_WAITING_TIME = maxTime
    
    def __del__(self):
        time.sleep(self.MAX_WAITING_TIME) #wait for the last item to download
        self.driver.close()

    def openDownloadSite(self):
        self.driver.get(self.downloadSite)
    
    def downloadSong(self, youtubeUrl):
        self.openDownloadSite()
        inputBox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "input")))
        inputBox.send_keys(youtubeUrl)
        submitBox = self.driver.find_element_by_id("submit")
        submitBox.click()
        #xpath for buttons is //div[@id='buttons']//*, the buttons are in this order: Download, Dropbox, Next
        downloadBtn = WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='buttons']//*)[1]")))
        downloadBtn.click()
    
    def downloadListOfSongs(self, listOfUrls):
        self.openDownloadSite()
        for url in listOfUrls:
            
            '''Check if the site redirected as to an ad, close the ad and return to working site
            Could also be done like that if we dont care about closing the ad:
            try:
                self.driver.switch_to_window(self.driver.window_handles[0])
            except:
                pass
            '''
            try:
                self.driver.switch_to_window(self.driver.window_handles[1])
                print("Detected Redirect")
                self.driver.close()
                self.driver.switch_to_window(self.driver.window_handles[0])
            except:
                pass
            """
            Some videos are only available for premium users, or there might be some other restrictions that prevent the site from converting and downloading.
            This will cause a TimeoutException as the MAX_WAITING_TIME will pass without finding the correct element because the converting process will fail.
            To bypass that, we simply continue with the next url in the page after reloading.
            
            Be careful: This will bypass every url that causes a timeout exception, so you might want to provide a higer MAX_WAITING_TIME if your internet connection is
            not very fast or if you want to download incredibly big playlists.
            """
            try:
                time.sleep(1)
                inputBox = WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(EC.element_to_be_clickable((By.ID, "input")))
                inputBox.send_keys(url)
                submitBtn = WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(EC.element_to_be_clickable((By.ID, "submit")))
                submitBtn.click()
                downloadBtn = WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='buttons']//*)[1]")))
                downloadBtn.click()
                nextBtn = WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='buttons']//*)[3]")))
                nextBtn.click()
            except:
                print("Failed to download from url %s", url)
                self.openDownloadSite()
                continue
        
    def extractUrlsFromPlaylist(self, url):

        f = open(os.path.join("", 'file.txt'), 'w')
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), features="html.parser")

        href_tags = soup.find_all('a', href=True)
        alreadyFound = []       
        for i in href_tags:       
            if 'watch' in str(i):
                completeUrl = "youtube.com"+str(i['href'])
                if completeUrl not in alreadyFound: 
                    f.write("youtube.com"+i['href']+'\n')
                    alreadyFound.append(completeUrl)
        f.close()


    def downloadPlayilistFromText(self, location):
        f = open(location, 'r')
        mylist = f.read().splitlines()
        try:
            mylist.remove('youtube.com/')
        except:
            pass
        self.downloadListOfSongs(mylist)

    def downloadPlayilistFromUrl(self, url):
        tempExtractor = UrlExtractor.UrlExtractor(url)
        tempList = tempExtractor.extract()
        self.downloadListOfSongs(tempList)

def main():
    #Example use of code

    #Create a Downloader object, by passing the folder where you want the songs to be downloaded (required) and the MAX_WAITING_TIME (optional)
    myBot = Downloader(r'YOUR_PATH_HERE', 30)

    #Provide a playilist link to download
    # myBot.extractUrlsFromPlaylist('https://www.youtube.com/playlist?list=PLEaWXpLoxDDptgWjTUCLsbfDeUB_umf-d')

    # #Download the playilist from a text file, where the links are seperated by '\n'
    # myBot.downloadPlayilistFromText(r"D:\Apostolis\Project\Github\MusicDownloader\file.txt")

    myBot.downloadPlayilistFromUrl("YOUR_PLAYLIST_HERE")

    
if __name__ == "__main__":
    main()
