import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request
import time

keyword_list = ['tomato', 'meat', 'bloodstain']
n_images = 2

def download_images(keyword_list, n_images):

    PATH = os.path.relpath('chromedriver')
    driver = webdriver.Chrome(PATH)
    driver.get('https://images.google.com/')
    search = driver.find_element_by_name('q')

    folder = 'train-images'
    if not os.path.exists(folder):
        os.mkdir(folder)

    for keyword in keyword_list:
        search.send_keys(keyword)
        search.send_keys(Keys.RETURN)

        # scroll 3 times (to get shit ton of images)
        count = 0
        for i in range(3):
            driver.execute_script("scrollBy(" + str(count) + ",+1000);")
            count += 1000
            time.sleep(1)

            # find element
            islmp = driver.find_element_by_id('islmp')
            img = islmp.find_elements_by_tag_name('img')

            # get the image
            for j,i in enumerate(img):
                if j < n_images:
                    src = i.get_attribute('src')
                    try:
                        if src != None:
                            src = str(src)
                            print(src)
                            subfolder = '{}'.format(keyword)
                            os.makedirs(subfolder)
                            urllib.request.urlretrieve(src, os.path.join(subfolder, keyword+str(j)+ '.jpg'))
                        else:
                            raise TypeError
                    except:
                        print('fail')
    driver.close()
    
    download_images(keyword_list, n_images)
