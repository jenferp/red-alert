import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 
import urllib.request
import time

# number of keywords: 10 blood, 20 non_blood
data = {'blood': ['bloody person', 'bloody knife', 'bloodstain', 'blood', 'blood spatter', 'wound bleeding',
                  'bloody crime scene', 'tissue with blood', 'blood covered person', 'bleeding person stock photo'],
        'non_blood': ['tomato', 'cherry', 'roses', 'red shirt', 'ketchup', 'ketchup stain', 'meat', 'red paint',
                      'red hair', 'red clothes', 'red car', 'red balloons', 'jam', 'apple', 'cut watermelon',
                      'pomegranate', 'strawberry', 'raspberry', 'chili', 'fire']}
num = 200

'''data = {'blood': ['bloodstain', 'blood spatter'],
        'non_blood': ['tomato', 'cherry']}
num = 4'''

# Function Definition
def download_images(data, num):
# Inputs: dictionary with subdirectory names (str) and corresponding lists of keywords (str), number of images for each class (int).
# Googles specified keywords and downloads the resulting images inside a sub-folder inside train-images folder.

    PATH = './chromedriver'
    prefix = 'https://www.google.com/search?q='
    postfix = '&sxsrf=ALeKk021MCrnJ-FOLNJ3T-_MP5mIjFfSig:1614043486063&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjhzo3F7P7uAhXPJDQIHRYJBKUQ_AUoAXoECBcQAw&biw=1440&bih=764'

    # runs brower headlessly and in incognito mode
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(PATH, options=options)

    # makes a directory for training images inside cwd if the path does not exist already
    folder = 'train_images'
    if not os.path.exists(folder):
        os.mkdir(folder)

    # makes a subdirectory for each key inside above directory if the path does not exist already
    for key in data:
        subfolder = folder + '/' + '{}'.format(key)
        n_images = num // len(data[key])
        print(n_images)
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)

        for keyword in data[key]:
            keyword = keyword.replace(' ', '+')
            search_url = prefix + keyword + postfix
            driver.get(search_url)

            # scroll 3 times (to get shit ton of images)
            print("hi")
            count = 0
            print("boob")
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
                            # src = str(src)
                            urllib.request.urlretrieve(src, os.path.join(subfolder, keyword + str(j) + '.jpg'))
    driver.quit()

# Function Call
download_images(data, num)