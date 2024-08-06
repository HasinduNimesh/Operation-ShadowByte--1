import requests
from bs4 import BeautifulSoup
import time

def search_person(name):
    # Encode the person's name for URL
    query = '+'.join(name.split())
    URL = f'https://www.bbc.com/search?q={query}'
    
    # Request the website
    response = requests.get(URL)
    print("The Response code is :", response.status_code)
    
    if response.status_code == 200:
        # Parse the HTML document
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the news headlines
        headlines = soup.find_all('h1') + soup.find_all('h2') + soup.find_all('h3') # Add more as needed
        
        # Display the headlines and their URLs
        for headline in headlines:
            print(headline.text.strip())
            time.sleep(1)
    else:
        print("Failed to retrieve the page.")

# Input person's name
person_name = input("Enter the person's name to search for: ")
search_person(person_name)
