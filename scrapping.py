
from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv 
from selenium.webdriver.common.by import By 
import pandas as pd
import requests 
 

Starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome('C:/Users/RITU.000/Desktop/vidhi seth/whitHat/web scrappin 128/chromedriver')
browser.get(Starturl)
time.sleep(10)

def scrap():
  headers = ["name" , " lightyears" , "planetmass" , " stellar" , " discovery date "] 
  planetdata = [] 
  #finding all the url tags with class exoplanet 
  for i in range (0,428):
        soup = BeautifulSoup(browser.page_source , "html.parcel") 
        
        for ul_tag in soup.find_all('ul' , attrs = {'class' , 'exoplanet'}):
              li_tags = ul_tag.find_all('li')
              templist = []
              
              for index , li_tag in enumerate(li_tags):
                    if index == 0 : 
                      templist.append(li_tag.find_all('a') [0].contents[0])
                    else: 
                      try:
                        templist.append(li_tag.contents[0])
                      except:
                        templist.append('')
                        
                        
              hyperlink_li_tag = li_tags[0]
              
              templist.append("https://exoplanets.nasa.gov"+ hyperlink_li_tag.find_all('a' , href = True) [0]['href'])  
              
              planetdata.append(templist)
              
        browser.find_element_by_xpath('//*[@id = "primary_column"]/fwter/div/div/div/nav/span[2]/a').click()
        print(f'page{i} scrapping completed')
        
  with open("scrapper2.csv" , "w")as f :
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata) 


scrap()     
    
    
   
        
                      



                    
              
        