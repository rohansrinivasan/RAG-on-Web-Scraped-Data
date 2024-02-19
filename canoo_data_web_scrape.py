import csv
import requests
from bs4 import BeautifulSoup

def scrape_text_from_website(urls):
    all_text = {}  # Dictionary to store text content from all URLs

    # Iterate over each URL
    for url in urls:
        # Send a GET request to the URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.1 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove script and style tags
            for script in soup(["script", "style"]):
                script.extract()

            # Extract text from the parsed HTML
            text = soup.get_text(separator=' ')

            # Store the text content in the dictionary with the URL as key
            all_text[url] = text.strip()

        else:
            print(f"Failed to retrieve data from {url}. Status Code: {response.status_code}")

    return all_text

def save_text_to_csv(text_data, output_file):
    # Write the text data to a CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Text'])  # Write column headers

        # Write each URL and its corresponding text content to a separate row
        for url, text in text_data.items():
            writer.writerow([url, text])

    print(f"Text has been saved to {output_file}")

if __name__ == "__main__":
    # List of URLs to search
    urls = ['https://www.cbinsights.com/company/evelozcity/alternatives-competitors',
            'https://www.spglobal.com/mobility/en/topic/electric-vehicle-trends.html',
            'https://dcf.fm/blogs/blog/goev-history-mission-ownership',
            'https://dcf.fm/blogs/blog/goev-mission-vision',
            'https://dcf.fm/blogs/blog/goev-swot-analysis',
            'https://dcf.fm/blogs/blog/goev-business-model-canvas',
            'https://dcf.fm/blogs/blog/goev-porters-five-forces-analysis',
            'https://dcf.fm/blogs/blog/goev-bcg-matrix',
            'https://dcf.fm/blogs/blog/goev-marketing-mix',
            'https://dcf.fm/blogs/blog/goev-pestel-analysis',
            'https://www.press.canoo.com/press-release/canoo-inc-announces-third-quarter-2023-results',
            'https://en.wikipedia.org/wiki/Canoo',
            'https://www.bloomberg.com/quote/GOEV:US',
            'https://www.google.com/finance/quote/GOEV:NASDAQ',
            'https://www.iea.org/reports/global-ev-outlook-2021/trends-and-developments-in-electric-vehicle-markets',
            'https://www.marketsandmarkets.com/Market-Reports/electric-vehicle-market-209371461.html',
            'https://www.precedenceresearch.com/electric-vehicle-market',
            'https://www.bloomberg.com/news/newsletters/2024-01-09/electric-vehicle-market-looks-headed-for-22-growth-this-year',
            'https://www.virta.global/en/global-electric-vehicle-market',
            'https://en.wikipedia.org/wiki/Tesla,_Inc',
            'https://en.wikipedia.org/wiki/Rivian',
            'https://en.wikipedia.org/wiki/General_Motors',
            'https://en.wikipedia.org/wiki/Ford_Motor_Company']

    # Scrape text from the websites
    website_text = scrape_text_from_website(urls)

    if website_text:
        # Save the text to a CSV file
        output_file = "website_text.csv"
        save_text_to_csv(website_text, output_file)
 