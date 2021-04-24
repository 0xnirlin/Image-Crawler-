import os
import requests
from bs4 import BeautifulSoup

def  sitemap():
    #First we will get the sitemaps of indivisual parts site been divided

    site_map = "http://www.pngmart.com/sitemapindex.xml/"

    #Now get the sitemap using the requests

    response = requests.get(site_map)

    #Now parse the response using the beautifulsoup

    soup = BeautifulSoup(response.text,'xml')

    #Now as the sitemap is parsed next step is to get each indivisual link into a singal list 

    site_map_parts = []

    for parts in soup.find_all('loc'):
        url = parts.text
        if 'part' in url:
            site_map_parts.append(url)
    
    return site_map_parts
def scrape():
    site_map_parts = sitemap()
    for siteparts in site_map_parts:
        print(siteparts)
        site_map = siteparts
        response = requests.get(site_map)
        soup = BeautifulSoup(response.text,'xml')
        for link in soup.find_all('loc'):
            url = link.text
            response = requests.get(url)
            soup = BeautifulSoup(response.text,'html.parser')
            image_link = soup.find('a',{"class":"download"})['href']
            response = requests.get(image_link)
            soup = BeautifulSoup(response.text,'html.parser')
            image_download = soup.find('a',{"class":"download"})['href']
            image = requests.get(image_download)
            image_title = image_link.split('/')[-1]+'-'+image_download.split('/')[-1]
            print(image_title)
            with open(image_title,'wb') as file:
                file.write(image.content)
            
scrape()