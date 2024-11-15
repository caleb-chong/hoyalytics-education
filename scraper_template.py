#Necessary imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date
from datetime import timedelta

# Set up the webdriver (optional argument to run headless)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

#initialize the webdriver to use the chrome browser
driver = webdriver.Chrome(service=Service(), options=options)

current_date = date(2024, 1, 1)
num_days = 10

for i in range(num_days):
    day_string = current_date.strftime("%Y-%m-%d")
    current_date += timedelta(days=1)
    
    print(f"Scraping data for: {day_string}")

    url = f"https://www.hoyaeats.com/menu-hours/?date={day_string}"

    #use selenium to load the webpage
    driver.get(url)

    table_rows_with_location_class = driver.find_elements(By.CLASS_NAME, "location")

    entries = []

    for row in table_rows_with_location_class:
        # print(row.get_attribute("innerHTML"))
        location_name_element = row.find_element(By.TAG_NAME, "a")
        location_name = location_name_element.get_attribute("innerHTML")

        meals = row.find_elements(By.CLASS_NAME, "hours-row")

        for meal in meals:
            meal_type = meal.find_element(By.CLASS_NAME, "hours-name").get_attribute("innerHTML")
            open_at = meal.find_element(By.CLASS_NAME, "open_at").get_attribute("innerHTML")
            close_at = meal.find_element(By.CLASS_NAME, "close_at").get_attribute("innerHTML")

            # print(location_name, meal_type, open_at, close_at)

            entries.append({
                "date": day_string,
                "location": location_name,
                "meal": meal,
                "open_at": open_at,
                "close_at": close_at
            })

        # print(location_name)

df = pd.DataFrame(entries)
df.to_csv("hoyaeatsdata.csv")

input("Press Enter to quit the program...")

driver.quit()