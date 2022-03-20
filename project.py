from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import requests 

dataset1 = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
dataset2 = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/kushaanagarwal/Desktop/Python/Class127/chromedriver')

browser.get(dataset1)
time.sleep(10)
headers = ['Star','Constellation','right_ascension','declination', 
    'distance', 'hyperlink', 'mass', 'eccentricity']

dwarf_data = []

new_dwarf_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    for ul_tag in soup.find_all('ul', attrs = {'class', 'brown_darf'}):
        li_tags = ul_tag.find_all('li')
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append('')
        hyperlink_li_tag = li_tags[0]
        temp_list.append('https://exoplanets.nasa.gov' + hyperlink_li_tag.find_all('a',href = True)[0]['href'])
        dwarf_data.append(temp_list)

    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    # with open('exoplanet_code.csv','w') as f:
    #     csvwriter = csv.writer(f)
    #     csvwriter.writerow(headers)
    #     csvwriter.writerows(planet_data)

def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content,'html.parser')
        temp_list = []
        for tr_tag in soup.find_all('tr', attrs = {'class':'fact_row'}):
            td_tags = tr_tag.find_all('td')
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all('div', attrs = {'class':'value'})[0].contents[0])
                except:
                    temp_list.append('')
        new_dwarf_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

scrape()

for data in dwarf_data:
    scrape_more_data(data[5])
    # print(f'{index+1} page done two!')

final_dwarf_data = []

for index, data in enumerate(dwarf_data):
   final_dwarf_data.append(data+final_dwarf_data[index])

with open('final.csv','w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(final_dwarf_data)