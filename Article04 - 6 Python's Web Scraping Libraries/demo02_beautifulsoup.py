from bs4 import BeautifulSoup
import requests
import pandas as pd

# Read url
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=30.2676&lon=-97.743")

# Download the page and start parsing
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

# Extract the name of the forecast item, the short description, and the temperature
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# Extract the title attribute from the img tag
img = tonight.find("img")
desc = img['title']

# Extracting all the information from the page
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# Combining our data into a Pandas Dataframe
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})

# Print the dataframe
print(weather)