import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 
import urllib.request
import time


# inputs are a list of strings as keywords and the number of images as an int
# keyword_list = ['tomato', 'meat', 'bloodstain']    n_images = 69
# Googles specified keywords and downloads the resulting images inside eponymous folders inside train-images folder
def download_images(keyword_list, n_images):

    PATH = './chromedriver'
    prefix = 'https://www.google.com/search?q='
    postfix = '&sxsrf=ALeKk021MCrnJ-FOLNJ3T-_MP5mIjFfSig:1614043486063&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjhzo3F7P7uAhXPJDQIHRYJBKUQ_AUoAXoECBcQAw&biw=1440&bih=764'

    # runs brower headlessly (does not open window)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(PATH, options=options)

    # makes a folder for training images inside cwd if it does not exist already
    folder = 'train-images'
    if not os.path.exists(folder):
        os.mkdir(folder)

    for keyword in keyword_list:
        search_url = prefix + keyword + postfix
        driver.get(search_url)

        # scroll 3 times (to get shit ton of images)
        count = 0
        for i in range(3):
            driver.execute_script("scrollBy(" + str(count) + ",+1000);")
            count += 1000
            time.sleep(1)

            # find element by id and tag name
            islmp = driver.find_element_by_id('islmp')
            img = islmp.find_elements_by_tag_name('img')

            # get n images from the page and downloads them into training images folder
            for j,i in enumerate(img):
                if j < n_images:
                    src = i.get_attribute('src')
                    if src != None:
                        src = str(src)
                        subfolder = folder + '/' + '{}'.format(keyword)
                        if not os.path.exists(subfolder):
                            os.mkdir(subfolder)
                        urllib.request.urlretrieve(src, os.path.join(subfolder, keyword + str(j) + '.jpg'))
    driver.quit()
