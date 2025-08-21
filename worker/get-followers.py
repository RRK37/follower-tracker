from playwright.sync_api import sync_playwright
from datetime import datetime
import csv
import os
import re

def get_followers(username):
    url = f"https://www.instagram.com/{username}/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        # Just grab the meta description content
        meta_content = page.get_attribute('meta[name="description"]', "content")
        browser.close()

        # Extract followers from the meta content
        match = re.search(r"([\d,.]+)\s+Followers", meta_content)
        if match:
            followers_text = match.group(1)
            followers = normalize_followers(followers_text)
            return followers
        else:
            raise ValueError(f"Could not find followers in: {meta_content}")

def normalize_followers(text):
    """Convert Instagram-style follower counts into an integer."""
    text = text.lower().replace(",", "").strip()
    if "k" in text:
        return int(float(text.replace("k", "")) * 1000)
    elif "m" in text:
        return int(float(text.replace("m", "")) * 1_000_000)
    elif "b" in text:
        return int(float(text.replace("b", "")) * 1_000_000_000)
    else:
        return int(text)

# --- Logging to CSV ---
with open("username.txt", "r") as f:
    username = f.read().strip()
followers = get_followers(username)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
csv_file = "/data/followers.csv"

file_exists = os.path.isfile(csv_file)
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["time_and_date", "count"])
    writer.writerow([now, followers])

print(f"Logged {followers} followers at {now}") 
