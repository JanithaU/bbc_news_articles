import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openai

# OpenAI API setup
openai.api_key = '#### update with your open api key ####'

# Function to generate a comment/summary using OpenAI
def generate_comment(article_content):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a thoughtful comment based on this article: {article_content}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to set up Selenium WebDriver
def set_up_driver():
    driver = webdriver.Firefox()
    driver.get("https://www.bbc.com")
    return driver

# Function to search the news site for articles related to a specific keyword
def search_for_keyword(driver, keyword):
    search_box = driver.find_element(By.ID, "orb-search-q")  # BBC's search box
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # wait for the results page to load
    return driver

# Function to extract article URLs from the search results
def extract_article_urls(driver):
    articles = driver.find_elements(By.CSS_SELECTOR, "a[href*='/news/']")  # Sample CSS selector for news articles
    urls = [article.get_attribute("href") for article in articles]
    return urls

# Function to post comments on each article (hypothetical example)
def post_comments_on_articles(driver, article_urls):
    for url in article_urls:
        driver.get(url)
        time.sleep(3)  # Wait for the article page to load

        try:
            # Extract article content (replace with appropriate element locators)
            article_content = driver.find_element(By.TAG_NAME, "body").text[:500]  # Sample extraction of the first 500 characters
            
            # Generate a comment using OpenAI
            comment = generate_comment(article_content)

            # Post comment - Hypothetical section (Assuming BBC has a comment form)
            comment_box = driver.find_element(By.CSS_SELECTOR, "textarea.comment-input")  # Replace with the actual CSS selector for the comment box
            comment_box.send_keys(comment)
            
            # Submit the comment
            submit_button = driver.find_element(By.CSS_SELECTOR, "button.submit-comment")  # Replace with actual CSS selector for the submit button
            submit_button.click()

            print(f"Posted comment on {url}")
        except Exception as e:
            print(f"Failed to post comment on {url}: {e}")

if __name__ == "__main__":
    keyword = "climate change"  # Keyword to search for
    
    # Set up Selenium driver and search for articles
    driver = set_up_driver()
    search_for_keyword(driver, keyword)

    # Extract article URLs from the search results
    article_urls = extract_article_urls(driver)
    
    # Post generated comments on each article (hypothetical)
    post_comments_on_articles(driver, article_urls)
    
    # Close the driver
    driver.quit()
