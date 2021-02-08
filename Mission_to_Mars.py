#!/usr/bin/env python
# coding: utf-8

# 10.3.1. Import Splinter and Beatiful Soup
from splinter import Browser
from bs4 import BeautifulSoup as soup

# 10.3.1. Windows users
executable_path = {'executable_path': 'C://WebDrivers/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# 10.3.2. Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)
# In[5]:
# 10.3.2. Parse HTML
html = browser.html
html_soup = soup(html,'html.parser')

# 10.3.2. Scrape the Title
title = html_soup.find('h2').text
title
# In[7]:
# 10.3.2. Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')
for tag in tags:
    word = tag.text
    print(word)
# In[8]:
# 10.3.2. Assign an actual URL to the variable named "url"
url = 'http://quotes.toscrape.com/'
# Splinter will visit the webpage
browser.visit(url)
# In[9]:
# 10.3.2. Create a for loop to colect each quote, "click" the next button, then collect the next set of quotes
# Range(1,6) to visit the firs 5 pages of the website
for x in range(1, 6):
   html = browser.html
# Use BeautifulSoup to parse the 'html' object and span the tags with a 'class'
   quote_soup = soup (html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
# Use Splinter to click the "Next" button
   browser.links.find_by_partial_text('Next')
# In[10]:
# 10.3.3. Import Splinter, BeautifulSoup and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# 10.3.3. Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'C://WebDrivers/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
# In[12]:
# 10.3.3. Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# we're searching for elements with a specific combination of tag 'ul' and 'li' attribute 'item_list' and 'slide'
# Optional delay for loading the page by one second before searching components
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# 10.3.3. HTML parser. We assigned the variable 'slide-elem' 
# look for 'ul' tags with class 'item_list'
# Look for 'li' tags with class 'slide'
#We’re looking for a <div /> with a class of “content_title.”
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')
# In[14]:
# 10.3.3. We need to get just the text, and the extra HTML stuff isn't necessary: ".get_text()"
# Also we created a new variable for the title called 'news_title'
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title
# The result is the most recent title published on the website
# In[15]:
# 10.3.3. Use the parent element to find the paragraph text 'article_teaser_body'
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p
# Example Summary Output
# In[16]:
# 10.3.4. Visit URL
PREFIX = 'https://web.archive.org/web/20181114023733'
url = f'{PREFIX}/https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
#WAIT FOR THE PAGE TO COMPLETELY LOAD"
# In[17]:
#################################################
# JPL Mars Space Images - Featured Image
#################################################
# ## John McSwain code - use this
#10.3.4. Find the relative image url
article = browser.find_by_tag('article').first['style']
article_background = article.split("_/")[1].replace('"},',"")
print(f'{PREFIX}_if/{article_background}')

# 10.3.4 All in one step by John McSawin in slack
def featured_image(browser):
    # Visit URL
    try:
        PREFIX = "https://web.archive.org/web/20181114023733"
        url = f'{PREFIX}/https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)
        article = browser.find_by_tag('article').first['style']
        article_background = article.split("_/")[1].replace('");',"")
        return f'{PREFIX}_if/{article_background}'
    except:
        return 'https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/pia22486-main.jpg'
# In[19]:
# ## Mars Facts

# 10.3.5. Creating a new DataFrame from the HTML table
# The Pandas function 'read html()' specifically searchs for and returns a list of tables found on HTML
# 'df.columns=['description','value'] assigns columns to the new DataFrame
# 'df.set_index('description', inplace = True), the index will be done by description
import pandas as pd
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df
# In[20]:
# 10.3.5. Turn DataFrame into HTML by using function '.to_html'
df.to_html()
# In[21]:
# Clean the spaces
cleaner_html = df.to_html().replace('\n','').replace(' ','')
cleaner_html
# In[22]:
# 10.3.5. Quit the Notebook
browser.quit()