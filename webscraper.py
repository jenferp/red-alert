import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request
import time

PATH = '/Users/jenniferpark/Desktop/chromedriver'
save_folder = 'train-images'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    download_images()

def download_images():

    keyword = input('what are you looking for? ')
    n_images = int(input('how many images do you want? '))

    driver = webdriver.Chrome(PATH)
    driver.get('https://images.google.com/')
    search = driver.find_element_by_name('q')
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)

    count = 0
    for i in range(3):
        driver.execute_script("scrollBy("+ str(count) + ",+1000);")
        count += 1000
        time.sleep(1)

    islmp = driver.find_element_by_id('islmp')
    img = islmp.find_elements_by_tag_name('img')

    for j,i in enumerate(img):
        if j < n_images:
            src = i.get_attribute('src')
            try:
                if src != None:
                    src = str(src)
                    print(src)
                    urllib.request.urlretrieve(src, os.path.join(save_folder, keyword+str(j)+ '.jpg'))
                else:
                    raise TypeError
            except Exception as e:
                print('fail')
    driver.close()

if __name__ == '__main__':
    main()

