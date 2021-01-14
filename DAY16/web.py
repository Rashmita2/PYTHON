import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=31.46273304600004&lon=-99.33305008999997#.X_6I8uBMH-Y')
soup = BeautifulSoup(page.content, 'html.parser')
#contains html course in that webpage
#print(soup)
#create a variable to store the div, id from the webpages
week = soup.find(id='seven-day-forecast-body')
#contains all the tombstone-container
items = week.find_all(class_ = 'tombstone-container')
print(items[2])
#get all the names of days, weather and temperature and put into one column
#this can print the first items
#print(items[0].find(class_ = 'period-name').get_text())
#print(items[0].find(class_ = 'short-desc').get_text())
#print(items[0].find(class_ = 'temp').get_text())

#writing a for loop to get all the items using list comprehension
period_name = [item.find(class_ = 'period-name').get_text() for item in items]
short_description = [item.find(class_ = 'short-desc').get_text() for item in items]
temperature = [item.find(class_ = 'temp').get_text() for item in items]
print(period_name)
print(short_description)
print(temperature)

#import in the csv file using pandas
weather_stuff = pd.DataFrame({
    'Period': period_name,
    'Description': short_description,
    'temperature': temperature
})
print()
print(weather_stuff)
weather_stuff.to_csv('result.csv')

