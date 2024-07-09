import requests
from bs4 import BeautifulSoup

def search_facebook_marketplace(query, location, radius):
    # Define the URL for the Facebook Marketplace search
    url = f"https://www.facebook.com/marketplace/{location}/search?query={query}&radius={radius}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all listings on the page
        listings = soup.find_all('div', {'class': 'listing'})

        # Extract and print the details of each listing
        for listing in listings:
            title = listing.find('span', {'class': 'title'}).text
            price = listing.find('span', {'class': 'price'}).text
            location = listing.find('span', {'class': 'location'}).text
            print(f"Title: {title}\nPrice: {price}\nLocation: {location}\n")
    else:
        print(f"Failed to retrieve listings. Status code: {response.status_code}")



