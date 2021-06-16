from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    mars = {}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit('https://redplanetscience.com/')
    mars['title']  = browser.find_by_css('div.content_title').text
    mars['paragraph'] = browser.find_by_css('div.article_teaser_body').text

    browser.visit('https://spaceimages-mars.com')
    browser.find_link_by_partial_text("FULL IMAGE").click()
    mars['img'] = browser.find_by_css("img.fancybox-image")["src"]

    mars['facts'] =pd.read_html('https://galaxyfacts-mars.com',index_col=0,header=0)[0].reset_index().to_html(index=False, escape=True, classes='table table-striped')

    browser.visit('https://marshemispheres.com/')
    links = browser.find_by_css('a.itemLink h3')
    hemispheres = []
    for i in range(4):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()
    mars['hemispheres'] = hemispheres
    browser.quit()
    return mars