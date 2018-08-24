from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

###### VARIABLES ######

#      Main URL      #
base_url = 'https://www.mohawkflooring.com'


#      Directory by category      #
solid_url = base_url + '/solid-wood/search?page=8'
engineered_url = base_url + '/engineered-wood/search?page=6'
laminate_url = base_url + '/laminate-wood/search?page=7'



###### FUNCTIONS ######

class Item_links:
    def __init__(self, driver):
        self.driver = driver
        self.url = solid_url

    def navigate(self):
        return self.driver.get(self.url)

    def time_wait(self):
        for x in range(80):
            time.sleep(1)
            print(x,'s')

    def get_links(self):
        page_source = bs(browser.page_source, 'html.parser')
        boxes = page_source.find('div', {'class': 'product-wrapper'}).find('ul', {'class': 'products'}).find_all('li', {
            'class': 'product-item'})
        href_links = [box.find('a').get('href') for box in boxes]
        return href_links

    def mount_product_links(self):
        list = []
        for href in Item_links.get_links(self):
            list.append(base_url + href)
        return list[1]

    def product_page_source(self):
        browser.get(Item_links.mount_product_links(self))
        time.sleep(3)
        page_source = bs(browser.page_source, 'html.parser')
        return page_source


    def product_name(self):
        page_source = Item_links.product_page_source(self)

        #Get name of product
        name = page_source.find('h2', {'class': 'style-name'}).text

        #Get Color of product
        boxes = page_source.find('div', {'class': 'owl-stage'})
        product_color = boxes.find_all('a')

        list = []

        for a in product_color:
            color = a.get('title')
            list.append(color)
        return list





        '''
        list = []
        for link in Item_links.mount_product_links():
            browser.get(link)
            page_source = bs(browser.page_source. 'html.parser')
            list.append(page_source.find('dive', {'class': 'product-details-container'}))
        '''


###### MAIN FUNCTIONS ######


browser = webdriver.Chrome()
item_links = Item_links(browser)
item_links.navigate()
item_links.time_wait()
print(item_links.product_name())






























