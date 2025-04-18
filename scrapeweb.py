from playwright.sync_api import sync_playwright
import os
import re
import time
from urllib.parse import urlparse

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)
visited_urls = set()

def sanitize_filename(url):
    parsed_url = urlparse(url)
    filename = re.sub(r'[<>:"/\\|?*]', '_', parsed_url.path.strip('/'))
    return filename if filename else "index"

def save_page_content(url, text_content):
    filename = sanitize_filename(url) + ".txt"
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text_content)

    print(f"saved text content: {file_path}")

def extract_text_content(page):
    return page.eval_on_selector_all("body *:not(script):not(style)", """
        elements => elements.map(e => e.innerText.trim()).filter(t => t.length > 0).join('\\n')
    """)

def wait_for_dynamic_data(page):
    try:
        page.wait_for_selector("table, p, div.dynamic-content", timeout=10000)
    except:
        print("No dynamic content detected or timeout reached.")

def interact_with_map(page):
    try:
        map_element = page.query_selector("canvas, svg, #map")
        if map_element:
            print("Map detected! Clicking to load data...")
            map_element.click()
            time.sleep(5)
            wait_for_dynamic_data(page)
        else:
            print("No map detected on this page.")
    except Exception as e:
        print(f"Error interacting with map: {e}")

def scrape_page(page, url):
    print(f"scraping: {url}")

    try:
        page.goto(url, timeout=60000)
        wait_for_dynamic_data(page)
        interact_with_map(page)
        text_content = extract_text_content(page)
        save_page_content(url, text_content)
        links = page.eval_on_selector_all("a", "elements => elements.map(e => e.href)")

        for link in links:
            if link.startswith(url) and link not in visited_urls:
                visited_urls.add(link)
                scrape_page(page, link)

        time.sleep(1)

    except Exception as e:
        print(f"Error scraping {url}: {e}")

def mainscrape(url):
    with sync_playwright() as p:
        BASE_URL = url
        browser = p.chromium.launch(headless=False)  # Change to True for background scraping
        page = browser.new_page()

        visited_urls.add(BASE_URL)
        scrape_page(page, BASE_URL)

        browser.close()