import urllib3
from dotenv import load_dotenv
import os
import json
import tkinter as tk

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

def search_movie():
    title = entry.get()
    title = title.strip().replace(" ", "+")  # Replace spaces with '+' for URL encoding
    url = "http://www.omdbapi.com/?apikey=" + api_key + "&t=" + title
    response = urllib3.PoolManager().request('GET', url)
    data = json.loads(response.data.decode('utf-8'))

    # Testing
    # print(data) # Print the title of the first movie in the search results
    # print(data['totalResults']) # Print the total number of results returned by the API
    
    result_label.config(text=(
        "Title: " + data['Title'] + "\n" +
        "Year: " + data['Year'] + "\n" +
        "Rating: " + data['imdbRating'] + "\n" +
        "Plot: " + data['Plot']
    ))

# GUI Implementation
root = tk.Tk()
root.title("IMDB Movie Search")

label = tk.Label(root, text="Enter the title of the movie: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=search_movie)
button.pack()

result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack()

root.mainloop()