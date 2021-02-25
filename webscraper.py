import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import time

'''
# Sample Data:
data = {'blood': ['bloodstain', 'blood spatter'],
        'non_blood': ['tomato', 'cherry']}
download_images(data, 4)
'''


# Function Definition:
def download_images(data, n_class):
    # Inputs must be a dictionary of lists of keywords as strings and the desired integer number of images per class.
    # Googles specified urls and downloads the resulting images into a subdirectory named after the key (class name)
    # inside the 'train-images' directory.

    # for search_url later
    prefix = 'https://www.google.com/search?q='
    postfix = '&sxsrf=ALeKk021MCrnJ-FOLNJ3T-_MP5mIjFfSig:1614043486063&source=lnms&tbm=isch&sa=X&ved' \
              '=2ahUKEwjhzo3F7P7uAhXPJDQIHRYJBKUQ_AUoAXoECBcQAw&biw=1440&bih=764 '

    # run headless browser in incognito mode
    path = './chromedriver'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(path, options=options)

    # Make a directory for training images inside cwd if the path does not exist already
    folder = 'train_images'
    if not os.path.exists(folder):
        os.mkdir(folder)

    for key in data:

        # Make a subdirectory for each key if the path does not exist already
        subfolder = folder + '/' + '{}'.format(key)
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)

        # Divide num of images in each class by num of keywords to get num of images to get per page
        n_images = n_class // len(data[key])
        print(n_images)

        # Search the url for each keyword in the list
        for keyword in data[key]:

            keyword = keyword.replace(' ', '+')
            search_url = prefix + keyword + postfix
            driver.get(search_url)

            # Scroll 3 times
            count = 0
            for i in range(3):
                driver.execute_script("scrollBy(" + str(count) + ",+1000);")
                count += 1000
                time.sleep(1)

                # Find the element (image) in the page by id and tag name
                islmp = driver.find_element_by_id('islmp')
                img = islmp.find_elements_by_tag_name('img')

                # Get n images from the page and download them as jpg into the subdirectory
                for j, i in enumerate(img):
                    if j < n_images:
                        src = i.get_attribute('src')
                        if src is not None:
                            urllib.request.urlretrieve(src, os.path.join(subfolder, keyword + str(j) + '.jpg'))

    # Quit the driver instance
    driver.quit()


# Training Data: search keywords by class:
train = {'blood': ['bloody person', 'bloody knife', 'bloodstain', 'blood', 'blood spatter', 'wound bleeding',
                   'bloody crime scene', 'tissue with blood', 'blood covered person', 'bleeding person stock photo'],
         'non_blood': ['tomato', 'cherry', 'roses', 'red shirt', 'ketchup', 'ketchup stain', 'meat', 'red paint',
                       'red hair', 'red clothes', 'red car', 'red balloons', 'jam', 'apple', 'cut watermelon',
                       'pomegranate', 'strawberry', 'raspberry', 'chili', 'fire']}

# Function Call:
download_images(train, 200)
