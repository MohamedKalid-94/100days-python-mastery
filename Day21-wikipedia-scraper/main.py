# Day 21 - Wikipedia Article Scraper
# Concept: Web Scraping
# Goal: Practice fetching a web page and extracting data from its HTML

# Requires: pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# --- Step 1: Fetch the raw HTML of a page using requests ---
# Many sites (including Wikipedia) reject or throttle requests that don't
# send a proper User-Agent header, since the default one from requests
# looks like an obvious bot. Always send one for real scraping.
topic = "Python_(programming_language)"
url = f"https://en.wikipedia.org/wiki/{topic}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers, timeout=10)
print("Status code:", response.status_code)

# --- Always verify the request actually succeeded before parsing ---
if response.status_code != 200:
    print("Request failed - stopping here instead of parsing a bad response.")

# --- The raw response is just a big string of HTML ---
html_content = response.text
print("\nFirst 300 characters of raw HTML:")
print(html_content[:300])

# --- Step 2: Parse the HTML using BeautifulSoup ---
# This turns the raw string into a structured object we can search through
soup = BeautifulSoup(html_content, "html.parser")
print("\nType of parsed object:", type(soup))

# --- Getting the page title - defensively, in case it's missing ---
# soup.title can be None if the page didn't load as expected (e.g. blocked,
# redirected, or an error page). Always check before accessing .text on it.
if soup.title:
    page_title = soup.title.text
    print("\nPage title:", page_title)
else:
    print("\nNo <title> tag found - the page may not have loaded correctly.")
    print("Check the status code and the first characters of html_content above.")

# --- find() - gets the FIRST matching element ---
first_heading = soup.find("h1")
print("\nFirst <h1> on the page:", first_heading.text)

# --- find_all() - gets ALL matching elements as a list ---
all_paragraphs = soup.find_all("p")
print(f"\nFound {len(all_paragraphs)} <p> (paragraph) tags on the page.")

# --- Extracting text from the first few real paragraphs ---
print("\n--- First 3 paragraphs of the article ---")
count = 0
for paragraph in all_paragraphs:
    text = paragraph.text.strip()
    if text:   # skip empty paragraphs
        print(f"\n{text[:300]}...")   # print only the first 300 characters
        count += 1
    if count == 3:
        break

# --- Finding elements by class or id ---
# In real scraping, you inspect the page's HTML (right-click -> Inspect)
# to find the class/id names you need to target.
content_div = soup.find("div", {"id": "mw-content-text"})
if content_div:
    print("\nFound the main content div by its id.")

# --- Finding all links on the page ---
all_links = soup.find_all("a")
print(f"\nFound {len(all_links)} links on the page.")

# --- Extracting the href attribute from links ---
print("\n--- First 5 links (with href) ---")
count = 0
for link in all_links:
    href = link.get("href")   # .get() avoids an error if href doesn't exist
    if href and href.startswith("/wiki/"):   # only internal Wikipedia links
        print(href)
        count += 1
    if count == 5:
        break

# --- Extracting all headings (h2) - usually section titles ---
headings = soup.find_all("h2")
print(f"\n--- Section headings found ({len(headings)}) ---")
for heading in headings[:8]:   # just show the first 8
    print(heading.text.strip())

# --- Being respectful when scraping ---
# Always check a site's robots.txt and terms of service before scraping.
# Add delays between requests if scraping multiple pages, so you don't
# overload the server. For Wikipedia specifically, they even provide a
# proper API which is a better choice than scraping for real projects.
print("\nNote: always check robots.txt and terms of service before scraping a real site.")


# ============================================================
# A reusable function to get a summary of any Wikipedia article
# ============================================================
def get_wikipedia_summary(article_title):
    url = f"https://en.wikipedia.org/wiki/{article_title.replace(' ', '_')}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        return f"Could not fetch article: {error}"

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")

    for paragraph in paragraphs:
        text = paragraph.text.strip()
        if text:
            return text   # return the first non-empty paragraph as the summary

    return "No summary found."


# ============================================================
# Interactive part: look up any topic
# ============================================================
print("\n--- Wikipedia Article Scraper ---")
user_topic = input("Enter a topic to search on Wikipedia: ")
summary = get_wikipedia_summary(user_topic)
print(f"\nSummary:\n{summary[:500]}")