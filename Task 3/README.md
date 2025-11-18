# Task 3: News Headlines Web Scraper

## 📋 Overview
A Python-based web scraper that automatically collects top headlines from popular news websites and saves them to a text file. The application provides an interactive command-line interface for scraping multiple news sources with proper error handling.

## ✨ Features Implemented

### Core Functionality
- ✅ **Multiple News Sources** - Scrapes from BBC News, Hacker News, The Guardian, and Reddit r/news
- ✅ **HTML Fetching** - Uses `requests` library to fetch web pages
- ✅ **HTML & JSON Parsing** - Uses `BeautifulSoup` for HTML and JSON API for Reddit
- ✅ **File Export** - Saves all headlines to a formatted text file
- ✅ **Interactive Menu** - User-friendly command-line interface

### Technical Features
- ✅ **Error Handling** - Graceful handling of network errors, 403 blocks, and parsing issues
- ✅ **Enhanced Headers** - Complete browser-like headers to prevent blocking
- ✅ **JSON API Support** - Uses Reddit's JSON API for more reliable scraping
- ✅ **Duplicate Prevention** - Removes duplicate headlines from same source
- ✅ **Timestamp Recording** - Records when headlines were scraped
- ✅ **Multiple Scraping Methods** - Uses various parsing strategies for reliability
- ✅ **Organized Output** - Headlines grouped by source in output file
- ✅ **Display Option** - View headlines in console before saving

## 🛠️ Technologies Used
- **Language**: Python 3.12
- **Libraries**:
  - `requests` - HTTP library for fetching web pages
  - `beautifulsoup4` - HTML parsing and data extraction
  - `os` - File path operations
  - `datetime` - Timestamp generation

## 📁 Project Structure
```
Task 3/
├── news_scraper.py      # Main application file
├── requirements.txt     # Python dependencies
├── headlines.txt        # Generated headlines file (after scraping)
├── requirement.md       # Task requirements
└── README.md            # This file
```

## 🚀 How to Run

### 1. Install Dependencies
```bash
cd "/workspaces/ElevenLabs/Task 3"
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests beautifulsoup4
```

### 2. Run the Application
```bash
python news_scraper.py
```

### 3. Follow the Interactive Menu
- Select news sources to scrape
- Display headlines in console
- Save headlines to a text file

## 💡 Usage Guide

### Main Menu
```
======================================================================
        NEWS HEADLINES WEB SCRAPER
======================================================================
Select news source to scrape:
1. BBC News
2. Hacker News
3. The Guardian
4. Reddit r/news (may have access issues)
5. Scrape All Sources
6. Display Scraped Headlines
7. Save to File
8. Exit
======================================================================
```

### Scraping Workflow

1. **Choose a Source** (Options 1-4 for individual, 5 for all)
2. **Wait for Scraping** - The app fetches and parses headlines
3. **View Headlines** (Option 6) - Display in console
4. **Save to File** (Option 7) - Export to text file
5. **Exit** (Option 8) - Close the application

### Example Session

```
🎉 Welcome to News Headlines Web Scraper!

Enter your choice (1-8): 5

🔄 Scraping all sources...

🔍 Scraping BBC News...
✅ Found 15 headlines from BBC News

🔍 Scraping Hacker News...
✅ Found 15 headlines from Hacker News

🔍 Scraping The Guardian...
✅ Found 15 headlines from The Guardian

🔍 Scraping Reddit r/news...
✅ Found 15 headlines from Reddit

✅ All sources scraped!

Enter your choice (1-8): 7
Enter filename (default: headlines.txt): 

✅ Headlines saved to: /workspaces/ElevenLabs/Task 3/headlines.txt
📊 Total headlines saved: 60
```

## 🔧 Implementation Details

### Class Structure

**`NewsScraper`** - Main class handling all scraping operations

#### Methods:
- **`__init__()`** - Initializes the scraper with enhanced headers and empty headlines list
- **`scrape_bbc_news()`** - Scrapes headlines from BBC News website
- **`scrape_hacker_news()`** - Scrapes headlines from Hacker News
- **`scrape_guardian_news()`** - Scrapes headlines from The Guardian
- **`scrape_reddit_news()`** - Scrapes headlines from Reddit r/news via JSON API
- **`save_to_file()`** - Saves all headlines to a formatted text file
- **`display_headlines()`** - Displays headlines in the console

### Key Design Decisions

1. **Enhanced Headers**
   ```python
   self.headers = {
       'User-Agent': 'Mozilla/5.0 ...',
       'Accept': 'text/html,application/xhtml+xml,...',
       'Accept-Language': 'en-US,en;q=0.5',
       'Accept-Encoding': 'gzip, deflate, br',
       'Connection': 'keep-alive',
       'Upgrade-Insecure-Requests': '1'
   }
   ```
   - Complete browser-like headers to prevent 403 blocks
   - Mimics real browser behavior more accurately
   - Required by many websites for scraping

2. **Reddit JSON API**
   ```python
   url = "https://www.reddit.com/r/news.json"
   data = response.json()
   for post in data['data']['children']:
       title = post['data']['title']
   ```
   - Uses Reddit's public JSON API instead of HTML scraping
   - More reliable and less likely to be blocked
   - Handles 403 errors with helpful error messages

3. **Multiple Parsing Strategies**
   - Uses multiple methods to find headlines (h2, h3, specific classes)
   - Increases reliability when website structure changes
   - Filters out short/invalid headlines

4. **Error Handling**
   ```python
   try:
       response = requests.get(url, headers=self.headers, timeout=10)
       response.raise_for_status()
   except requests.exceptions.HTTPError as e:
       if e.response.status_code == 403:
           print(f"⚠️  Site blocked the request (403)...")
   except Exception as e:
       print(f"⚠️  Error scraping: {e}")
   ```
   - Timeout protection (10 seconds)
   - Specific handling for 403 Forbidden errors
   - Graceful error messages
   - Continues operation even if one source fails

5. **Data Structure**
   - Stores headlines as tuples: `(source, headline)`
   - Allows grouping by source in output
   - Easy to extend with more metadata

6. **File Output Format**
   - Structured format with headers and separators
   - Timestamp for reference
   - Total count at the end
   - UTF-8 encoding for international characters

## 📊 Supported News Sources

| Source | URL | Headlines Count | Method |
|--------|-----|-----------------|--------|
| BBC News | https://www.bbc.com/news | Up to 15 | HTML Parsing |
| Hacker News | https://news.ycombinator.com/ | Up to 15 | HTML Parsing |
| The Guardian | https://www.theguardian.com/international | Up to 15 | HTML Parsing |
| Reddit r/news | https://www.reddit.com/r/news.json | Up to 15 | JSON API |

### Why These Sources?

- **BBC News** - Major international news source
- **Hacker News** - Tech news and discussions
- **The Guardian** - Reliable UK-based global news (scraper-friendly)
- **Reddit r/news** - Community-curated news via JSON API
- All sources are publicly accessible without authentication

## 📄 Output File Format

```
======================================================================
NEWS HEADLINES SCRAPER
Scraped on: 2025-11-18 14:30:45
======================================================================

======================================================================
SOURCE: BBC News
======================================================================

• First headline from BBC
• Second headline from BBC
• ...

======================================================================
SOURCE: Hacker News
======================================================================

• First headline from Hacker News
• Second headline from Hacker News
• ...

======================================================================
SOURCE: The Guardian
======================================================================

• First headline from The Guardian
• Second headline from The Guardian
• ...

======================================================================
Total Headlines: 60
======================================================================
```

## 🎯 Learning Outcomes

Through this project, the following concepts were practiced:
- ✅ Web scraping with Python
- ✅ HTTP requests and response handling
- ✅ HTML parsing with BeautifulSoup
- ✅ CSS selectors and HTML structure analysis
- ✅ Error handling for network operations
- ✅ File I/O operations with UTF-8 encoding
- ✅ Object-oriented programming
- ✅ Working with external libraries
- ✅ Data extraction and cleaning
- ✅ User interface design for CLI applications

## 🔍 Web Scraping Techniques Used

### 1. **Finding Headlines**
```python
# Method 1: By tag and attribute
soup.find_all('h2', {'data-testid': 'card-headline'})

# Method 2: By tag name
soup.find_all('h3')

# Method 3: By CSS class
soup.find_all('a', class_='title')

# Method 4: By nested structure
span.find('a')
```

### 2. **Text Extraction**
```python
headline = element.get_text(strip=True)
```
- `strip=True` removes leading/trailing whitespace

### 3. **Duplicate Prevention**
```python
if headline and headline not in headlines_found:
    headlines_found.append(headline)
```

### 4. **Content Filtering**
```python
if headline and len(headline) > 20:
    # Only include substantial headlines
```

## ⚠️ Important Notes

### Legal & Ethical Considerations
- ✅ Scrapes only publicly accessible content
- ✅ Includes User-Agent for transparency
- ✅ Respects website structure
- ⚠️ Always check website's `robots.txt` and Terms of Service
- ⚠️ Use responsibly and don't overload servers

### Technical Considerations
- Headlines are from the time of scraping
- Website structure changes may affect scraping
- Network issues may cause failures for some sources
- Some websites may block scraping attempts

## 🔮 Future Enhancements (Optional)

Potential features that could be added:
- More news sources (CNN, NYTimes, Guardian, etc.)
- Scheduled scraping with automation
- Export to JSON, CSV, or database
- Sentiment analysis of headlines
- Keyword filtering and search
- Email notifications for specific topics
- GUI interface using Tkinter or web interface
- Caching to avoid duplicate scraping
- Concurrent scraping for faster performance
- Image downloading along with headlines

## 🐛 Troubleshooting

### Common Issues

**1. Import Error**
```
ModuleNotFoundError: No module named 'requests'
```
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

**2. Connection Timeout**
```
Error scraping: ReadTimeout
```
**Solution**: Check internet connection or increase timeout value

**3. Reddit 403 Error**
```
Reddit blocked the request (403)
```
**Solution**: The app now uses Reddit's JSON API which is more reliable. If still blocked, use The Guardian (option 3) instead.

**4. Empty Headlines**
```
No headlines found
```
**Solution**: Website structure may have changed, or it may be blocking scraping

**5. SSL Certificate Errors**
```
SSLError
```
**Solution**: Update certificates or add `verify=False` to requests (not recommended)

## 📝 Dependencies

### requirements.txt
```
requests==2.31.0
beautifulsoup4==4.12.2
```

### Why These Versions?
- **requests 2.31.0**: Latest stable version with security fixes
- **beautifulsoup4 4.12.2**: Latest version with improved parsing

## 👨‍💻 Author

Developed as part of the ElevenLabs coding assessment - Task 3

## 📄 License

This project is created for educational purposes.

---

**Note**: Web scraping should be done responsibly. Always respect website terms of service and robots.txt files. This tool is for educational purposes only.
