#Selenium helps you use this executable to automate Chrome
from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from datetime import datetime as dt
from PIL import Image
import time
import os

# Download the driver from chromedriver website for relevant OS i.e. MAC, Windows, Debian, etc.
PATH = "C:\\Users\\hp\\Documents\\uler\\scrapping\\chromedriver\\chromedriver.exe"
wd = webdriver.Chrome(executable_path=PATH)


def get_images_from_google(wd, delay, max_images, url):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = url
	wd.get(url)

	image_urls = set()
	skips = 0
	while len(image_urls) + skips < max_images:
		scroll_down(wd)
		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					##print(f"Found {len(image_urls)}")

	return image_urls


def download_image(down_path, url, file_name, image_type='JPEG',
                   verbose=True):
    try:
        time = dt.now()
        curr_time = time.strftime('%H:%M:%S')
        #Content of the image will be a url
        img_content = requests.get(url).content
        #Get the bytes IO of the image
        img_file = io.BytesIO(img_content)
        #Stores the file in memory and convert to image file using Pillow
        image = Image.open(img_file)
        file_pth = down_path + file_name

        with open(file_pth, 'wb') as file:
            image.save(file, image_type)

        if verbose == True:
            print(f'The image: {file_pth} downloaded successfully at {curr_time}.')
    except Exception as e:
        print(f'Unable to download image from Google Photos due to\n: {str(e)}')



if __name__ == '__main__':
    # Google search URLS
    google_urls = [
          'https://www.google.com/search?rlz=1C1PRFI_enID1024ID1024&q=ayam+bakar+paha&tbm=isch&sa=X&ved=2ahUKEwjyid-Bp7D_AhUa-jgGHbWyB2QQ0pQJegQIChAB&biw=1366&bih=592&dpr=1'
    ]
    
    # Labels for the players
    labels = [
        'ayam_bakar_paha'
    ]

    # Check the length of the lists
    if len(google_urls) != len(labels):
        raise ValueError('The length of the url list does not match the labels list.')

    food_path = 'images/food/'
    # Make the directory if it doesn't exist
    for lbl in labels:
        if not os.path.exists(food_path + lbl):
            print(f'Making directory: {str(lbl)}')
            os.makedirs(food_path+lbl)

    for url_current, lbl in zip(google_urls, labels):
        urls = get_images_from_google(wd, 0, 4, url_current)
        # Once we have added our urls to empty set then 
        for i, url in enumerate(urls):
            download_image(down_path=f'images/food/{lbl}/', 
                        url=url, 
                        file_name=str(i+1)+ '.jpg',
                        verbose=True) 
    wd.quit()