from selenium import webdriver
from selenium.common.exceptions import WebDriverException,TimeoutException
import requests
import os
import time
import re

def browser(file_path,time_out ):
    # Pattern for getting domain 
    pattern = r"^https?://"
    # Set up browser options
    options = webdriver.FirefoxOptions()
    # Run Chrome in headless mode (no GUI)
    options.add_argument("--headless") 

    # Start with a clean browsing session 
    options.add_argument("--incognito") 

    # Initialize Chrome WebDriver
    browser = webdriver.Firefox(options=options)
    

    target_domains = []

    # Read the file and append each domain to the target_domains list
    try:
        with open(file_path, "r") as file:
            target_domains = file.read().split()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        browser.quit()
        exit()

    # Make screenshot path 
    if os.path.isdir("screenshots"):
        pass
    else :
        os.mkdir("screenshots")
    
    # Iterate through each domain and take a screenshot
    for domain in target_domains:
        
        if domain.startswith("https") or domain.startswith("http"):
            url = domain
        else:
           print("It does not start with http or https")
           print("example: https://abc.com/")
           quit()
                


        # File name for save each images 
        file_name = re.sub(pattern,' ', url)

        try:
            response = requests.get(url)
            browser.get(url)
            time.sleep(time_out)
            #screenshot_name = f"{domain.replace('.', '_')}.png"
            browser.save_screenshot(f"screenshots/{file_name}.png")
            print(f"Screenshot saved {file_name} ")
        except (requests.exceptions.RequestException, WebDriverException) as e:
            print(f"Error accessing {url}: {e}")
        except TimeoutException:
            print(f"Timeout accessing {url}")
        
    

    # Close the browser after taking all screenshots
    browser.quit()

