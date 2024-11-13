import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

#API_key = os.getenv("API_key", default="demo")

API_key="b9f0ce582ec50b5a9fa3768177b7d945"

url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_key}"
}

response = requests.get(url, headers=headers)

# Convert response to JSON
data = response.json()
print(data)

# Use pandas
# df = pd.DataFrame(data)
# df.to_csv("trending_movies.csv", index=False)

# Get results key
# data = data["results"]
# print(len(data))