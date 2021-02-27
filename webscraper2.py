import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import time


# Function Definition:
def download_images(n_images):
    # Inputs must be a dictionary of lists of keywords as strings and the desired integer number of images per class.
    # Googles specified urls and downloads the resulting images into a subdirectory named after the key (class name)
    # inside the 'train-images' directory.

    # run headless browser in incognito mode
    path = './chromedriver'
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(path, options=options)

    # Make a directory for training images inside cwd if the path does not exist already
    folder = 'train_images_hands'
    if not os.path.exists(folder):
        os.mkdir(folder)

        # Make a subdirectory for each key if the path does not exist already
    subfolder = folder + '/' + 'blood'
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)

    search_url = 'https://www.google.com/search?q=bloody%20hands&tbm=isch&tbs=rimg:CTYdKDwBwpXlYZk2w-UEFods' \
                 '&rlz=1C1MSNA_enUS600US600&hl=en-US&sa=X&ved=0CAIQrnZqFwoTCJiJvrLUiO8CFQAAAAAdAAAAABAI&biw' \
                 '=1730&bih=852'
    driver.get(search_url)

    # Scroll 3 times
    count = 0
    for i in range(20):
        driver.execute_script("scrollBy(" + str(count) + ",+1000);")
        count += 1000
        time.sleep(0.5)

        # Find the element (image) in the page by id and tag name
        islmp = driver.find_element_by_id('islmp')
        img = islmp.find_elements_by_tag_name('img')

    # Get n images from the page and download them as jpg into the subdirectory
    for img, img_pic in enumerate(img):
        if img < n_images:
            src = img_pic.get_attribute('src')
            if src is not None:
                urllib.request.urlretrieve(src, os.path.join(subfolder, 'bloody_hands' + str(img) + '.jpg'))

    # Quit the driver instance
    driver.quit()

# Function Call:
download_images(200)
