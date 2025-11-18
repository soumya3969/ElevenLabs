"""
News Headlines Web Scraper
Scrapes top headlines from news websites and saves them to a text file.
"""

import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.headlines = []
    
    def scrape_bbc_news(self):
        """Scrape headlines from BBC News"""
        print("\n🔍 Scraping BBC News...")
        try:
            url = "https://www.bbc.com/news"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find headlines in various BBC News formats
            headlines_found = []
            
            # Method 1: h2 tags with data-testid
            for h2 in soup.find_all('h2', {'data-testid': 'card-headline'}):
                headline = h2.get_text(strip=True)
                if headline and headline not in headlines_found:
                    headlines_found.append(headline)
            
            # Method 2: h3 tags
            for h3 in soup.find_all('h3'):
                headline = h3.get_text(strip=True)
                if headline and len(headline) > 20 and headline not in headlines_found:
                    headlines_found.append(headline)
            
            # Method 3: Links with specific classes
            for link in soup.find_all('a', class_='sc-2e6baa30-0'):
                headline = link.get_text(strip=True)
                if headline and len(headline) > 20 and headline not in headlines_found:
                    headlines_found.append(headline)
            
            self.headlines.extend([("BBC News", headline) for headline in headlines_found[:15]])
            print(f"✅ Found {len(headlines_found[:15])} headlines from BBC News")
            
        except Exception as e:
            print(f"⚠️  Error scraping BBC News: {e}")
    
    def scrape_hacker_news(self):
        """Scrape headlines from Hacker News"""
        print("\n🔍 Scraping Hacker News...")
        try:
            url = "https://news.ycombinator.com/"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find headlines - Hacker News uses span with class 'titleline'
            headlines_found = []
            for span in soup.find_all('span', class_='titleline'):
                link = span.find('a')
                if link:
                    headline = link.get_text(strip=True)
                    if headline and headline not in headlines_found:
                        headlines_found.append(headline)
            
            self.headlines.extend([("Hacker News", headline) for headline in headlines_found[:15]])
            print(f"✅ Found {len(headlines_found[:15])} headlines from Hacker News")
            
        except Exception as e:
            print(f"⚠️  Error scraping Hacker News: {e}")
    
    def scrape_reddit_news(self):
        """Scrape headlines from Reddit r/news (via JSON API)"""
        print("\n🔍 Scraping Reddit r/news...")
        try:
            # Use Reddit's JSON API which is more scraper-friendly
            url = "https://www.reddit.com/r/news.json"
            reddit_headers = self.headers.copy()
            reddit_headers['User-Agent'] = 'python:news-scraper:v1.0.0 (by /u/newsbot)'
            
            response = requests.get(url, headers=reddit_headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            headlines_found = []
            
            for post in data['data']['children']:
                title = post['data']['title']
                if title and title not in headlines_found and len(title) > 10:
                    headlines_found.append(title)
            
            self.headlines.extend([("Reddit r/news", headline) for headline in headlines_found[:15]])
            print(f"✅ Found {len(headlines_found[:15])} headlines from Reddit")
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print(f"⚠️  Reddit blocked the request (403). Try using The Guardian instead (option 3).")
            else:
                print(f"⚠️  Error scraping Reddit: {e}")
        except Exception as e:
            print(f"⚠️  Error scraping Reddit: {e}")
    
    def scrape_guardian_news(self):
        """Scrape headlines from The Guardian"""
        print("\n🔍 Scraping The Guardian...")
        try:
            url = "https://www.theguardian.com/international"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find headlines in The Guardian's structure
            headlines_found = []
            
            # Method 1: Headlines in card links
            for link in soup.find_all('a', class_='dcr-lv2v9o'):
                headline_span = link.find('span')
                if headline_span:
                    headline = headline_span.get_text(strip=True)
                    if headline and headline not in headlines_found and len(headline) > 15:
                        headlines_found.append(headline)
            
            # Method 2: Any h3 tags (backup method)
            if len(headlines_found) < 10:
                for h3 in soup.find_all('h3'):
                    headline = h3.get_text(strip=True)
                    if headline and headline not in headlines_found and len(headline) > 15:
                        headlines_found.append(headline)
            
            self.headlines.extend([("The Guardian", headline) for headline in headlines_found[:15]])
            print(f"✅ Found {len(headlines_found[:15])} headlines from The Guardian")
            
        except Exception as e:
            print(f"⚠️  Error scraping The Guardian: {e}")
    
    def save_to_file(self, filename='headlines.txt'):
        """Save all scraped headlines to a text file"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                # Write header
                f.write("="*70 + "\n")
                f.write("NEWS HEADLINES SCRAPER\n")
                f.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*70 + "\n\n")
                
                # Group by source
                current_source = None
                for source, headline in self.headlines:
                    if source != current_source:
                        f.write(f"\n{'='*70}\n")
                        f.write(f"SOURCE: {source}\n")
                        f.write(f"{'='*70}\n\n")
                        current_source = source
                    
                    f.write(f"• {headline}\n")
                
                # Write footer
                f.write(f"\n{'='*70}\n")
                f.write(f"Total Headlines: {len(self.headlines)}\n")
                f.write(f"{'='*70}\n")
            
            print(f"\n✅ Headlines saved to: {filepath}")
            print(f"📊 Total headlines saved: {len(self.headlines)}")
            
        except Exception as e:
            print(f"⚠️  Error saving to file: {e}")
    
    def display_headlines(self):
        """Display scraped headlines in the console"""
        if not self.headlines:
            print("\n📭 No headlines found.")
            return
        
        print("\n" + "="*70)
        print("SCRAPED HEADLINES")
        print("="*70)
        
        current_source = None
        for source, headline in self.headlines:
            if source != current_source:
                print(f"\n{source}:")
                print("-"*70)
                current_source = source
            print(f"  • {headline}")
        
        print(f"\n{'='*70}")
        print(f"Total: {len(self.headlines)} headlines")
        print("="*70)

def display_menu():
    """Display the scraper menu"""
    print("\n" + "="*70)
    print("        NEWS HEADLINES WEB SCRAPER")
    print("="*70)
    print("Select news source to scrape:")
    print("1. BBC News")
    print("2. Hacker News")
    print("3. The Guardian")
    print("4. Reddit r/news (may have access issues)")
    print("5. Scrape All Sources")
    print("6. Display Scraped Headlines")
    print("7. Save to File")
    print("8. Exit")
    print("="*70)

def main():
    """Main function to run the news scraper"""
    scraper = NewsScraper()
    
    print("\n🎉 Welcome to News Headlines Web Scraper!")
    print("This tool scrapes headlines from popular news websites.")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            scraper.scrape_bbc_news()
        
        elif choice == '2':
            scraper.scrape_hacker_news()
        
        elif choice == '3':
            scraper.scrape_guardian_news()
        
        elif choice == '4':
            scraper.scrape_reddit_news()
        
        elif choice == '5':
            print("\n🔄 Scraping all sources...")
            scraper.scrape_bbc_news()
            scraper.scrape_hacker_news()
            scraper.scrape_guardian_news()
            scraper.scrape_reddit_news()
            print("\n✅ All sources scraped!")
        
        elif choice == '6':
            scraper.display_headlines()
        
        elif choice == '7':
            if scraper.headlines:
                filename = input("Enter filename (default: headlines.txt): ").strip()
                if not filename:
                    filename = 'headlines.txt'
                if not filename.endswith('.txt'):
                    filename += '.txt'
                scraper.save_to_file(filename)
            else:
                print("\n⚠️  No headlines to save. Please scrape some news first!")
        
        elif choice == '8':
            print("\n👋 Thank you for using News Headlines Scraper. Goodbye!")
            break
        
        else:
            print("\n⚠️  Invalid choice! Please select 1-8.")

if __name__ == "__main__":
    main()
