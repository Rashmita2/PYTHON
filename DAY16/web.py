import pandas as pd
import requests

from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=31.46273304600004&lon=-99.33305008999997#.X_k4k-BMHfZ')
soup = BeautifulSoup(page.content, 'html.parser')
#soup is all the html content of the page
#print(soup)
#find all the a tag
#print(soup.find_all('a'))
#shows all the thing inside the div
week = soup.find(id='seven-day-forecast-body')
#print(week)
#print(wee.find_all('id'))
items = week.find_all(class_ ='tombstone-container')
#print(items[0])
'''
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

'''
#use a for loop to get all the items

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatues = [item.find(class_='temp').get_text() for item in items]
print(period_names)
print()
print(short_descriptions)
print()
print(temperatues)

#dictionary with pandas-it turns into the tables
weather_stuff = pd.DataFrame({
    'period':period_names,
    'short_descriptions':short_descriptions,
    'temperatures':temperatues
})
print(weather_stuff)

weather_stuff.to_csv('weather.csv')
