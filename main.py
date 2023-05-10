from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ser = Service(r"C:\\Users\\casey\\OneDrive\\Github Repositories\\USSoccer Data\\USSoccer-Data\\msedgedriver.exe")
op = webdriver.EdgeOptions()
driver = webdriver.Edge(service = ser, options = op)

base_url = "https://1xbet.whoscored.com/"

MLS_url = "https://www.whoscored.com/Regions/233/Tournaments/85/USA-Major-League-Soccer"
driver.get(MLS_url)


driver.find_element("id", "standings-21623").get_attribute()

# Get the links to each team, fill a dict with them:
# https://www.whoscored.com/Regions/233/Tournaments/85/USA-Major-League-Soccer

# At each team link: get list of all players, with all relevant data included - dict of matrices? Key is team name and year.

# Will need data structure for stored data - store by

# At each team link - need to go to history remember to subtract year difference off of age to get past age

# For each year that exists, need to store full table

# Could also go to each player page and store birth date? Maybe once


# print(driver)
# driver.find_element(By.ID, )

# Getting html

# html_text = requests.get('https://fbref.com/en/players/d70ce98e/all_comps/Lionel-Messi-Stats---All-Competitions').text

# print(html_text)


# with open('page.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     tags = soup.find_all('h5')
#     # for tag in tags: