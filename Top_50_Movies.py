import urllib3
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

title = input("Enter the title of the movie: ")
title = title.strip().replace(" ", "+")  # Replace spaces with '+' for URL encoding
url = "http://www.omdbapi.com/?apikey=" + api_key + "&t=" + title
response = urllib3.PoolManager().request('GET', url)
data = json.loads(response.data.decode('utf-8'))

# Testing
# print(data) # Print the title of the first movie in the search results
# print(data['totalResults']) # Print the total number of results returned by the API