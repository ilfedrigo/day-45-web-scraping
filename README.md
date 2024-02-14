# Movie Scraper

In my 45 day coding with Python I made an script that is designed to scrape movie titles from an archived webpage of Empire Online's list of best movies using BeautifulSoup and Requests. 

The extracted movie titles are then saved to a text file from 1 to 100. (The list provided from 100 to 1 that's why needs to reverse)

## How It Works

- **Imports**: The script imports the necessary libraries: BeautifulSoup for HTML parsing and requests for fetching web pages.

- **Fetch Web Page**: It sends a GET request to the specified URL (an archived page) using `requests.get()` and stores the response content in `archive`.

- **Parse HTML**: BeautifulSoup parses the HTML content of the page, creating a soup object.

- **Extract Movie Titles**: It finds all the `<h3>` elements with the class "title", which typically contain movie titles on the page.

- **Create Movie List**: It extracts the text from these elements (movie titles) and appends them to a list called `movies_list`.

- **Reverse the List**: The `movies_list` is reversed so that the first movie corresponds to the earliest entry on the webpage.

- **Write to File**: The movie titles from `movies_list` are written to a text file named `movies.txt`, with each title on a separate line.
