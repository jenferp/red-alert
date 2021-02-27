import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import time


# Function Definition:
def download_images(search_url, n_images):
    # Inputs must be a dictionary of lists of keywords as strings and the desired integer number of images per class.
    # Googles specified urls and downloads the resulting images into a subdirectory named after the key (class name)
    # inside the 'train-images' directory.
    '''data = {'Blood': 'https://www.google.com/search?q=bloody%20hands&tbm=isch&tbs=rimg:CTYdKDwBwpXlYZk2w-UEFods' \
                     '&rlz=1C1MSNA_enUS600US600&hl=en-US&sa=X&ved=0CAIQrnZqFwoTCJiJvrLUiO8CFQAAAAAdAAAAABAI&biw' \
                     '=1730&bih=852', 'No_blood':''}'''

    # run headless browser in incognito mode
    path = './chromedriver'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(path, options=options)

    # Make a directory for training images inside cwd if the path does not exist already
    folder = 'train_images_hands'
    if not os.path.exists(folder):
        os.mkdir(folder)

    # Make a subdirectory for each key if the path does not exist already
    subfolder = folder + '/' + 'No_blood2'
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)

    # search each url and store results in its respective subfolder

    print(search_url)
    driver.get(search_url)

    # Scroll 3 times
    count = 0
    for i in range(30):
        driver.execute_script("scrollBy(" + str(count) + ",+1000);")
        count += 1000
        time.sleep(0.5)

        # Find the element (image) in the page by id and tag name
        islmp = driver.find_element_by_id('islmp')
        img = islmp.find_elements_by_tag_name('img')

    # Get n images from the page and download them as jpg into the subdirectory
    count_images = 0
    for img, img_pic in enumerate(img):
        if img < n_images:
            src = img_pic.get_attribute('src')
            if src is not None:
                urllib.request.urlretrieve(src, os.path.join(subfolder, 'hands2_' + str(img) + '.jpg'))
                count_images += 1
    print(count_images)

    # Quit the driver instance
    driver.quit()


# Function Call:
url_hand_photo = 'https://www.google.com/search?q=hand%20photo&tbm=isch&tbs=rimg:CTS86OCt-XdWYam3YTGN8hLP&hl=en-US&sa' \
                 '=X&ved=0CAIQrnZqFwoTCIjnoP3Xiu8CFQAAAAAdAAAAABAG&biw=1440&bih=764'
url_hand_white = 'https://www.google.com/search?q=hands%20photos&tbm=isch&tbs=rimg:Cb5PJcxj1u7tYdLlW9ueiIac&rlz' \
                 '=1C1MSNA_enUS600US600&hl=en-US&sa=X&ved=0CBsQuIIBahcKEwiIuPy11IrvAhUAAAAAHQAAAAAQCA&biw=1730&bih=852'
url_hand_pinterest = 'https://www.google.com/search?q=hands+pinterest&tbm=isch&chips=q:hands+pinterest,' \
                     'g_1:photography:V60NEstTkPA%3D&rlz=1C5CHFA_enUS936US936&hl=en-US&sa=X&ved' \
                     '=2ahUKEwjN1IyX2IrvAhWHqZ4KHejBB-AQ4lYoA3oECAEQHg&biw=1440&bih=764'
# download_images(url_hand_photo, 150)
download_images(url_hand_white, 40)
# download_images(url_hand_pinterest, 70)

