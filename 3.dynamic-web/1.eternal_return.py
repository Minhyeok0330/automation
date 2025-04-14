from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

URL = 'https://dak.gg/er/statistics'
driver.get(URL)

tier_build = []
# subject_info = driver.find_elements(By.CSS_SELECTOR, 'a.keep-all')

# print(len(subject_info))

for i in range(3):
    subject_info = driver.find_elements(By.CSS_SELECTOR, 'a.keep-all')
    driver.get(subject_info[i].get_attribute('href')) #클릭 안 하고 링크 직접 받아왔음
    
    # weapon = driver.find_element(By.CSS_SELECTOR, 'content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-i78jj1 > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name').text
    # clothes = driver.find_element(By.CSS_SELECTOR, 'content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-pbd6xe > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name').text
    # head = driver.find_element(By.CSS_SELECTOR, 'content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-1nqodlm > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name').text
    # arm = driver.find_element(By.CSS_SELECTOR, 'content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-1yl1w33 > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name').text
    # shoes = driver.find_element(By.CSS_SELECTOR, 'content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-1qyqq5q > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name').text
#무기 content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-i78jj1 > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name
#옷 content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-pbd6xe > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name
#머리 content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-1nqodlm > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name
#팔 content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-1yl1w33 > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name
#신발 content-container > main > div.contents > div.main-content > div > section:nth-child(5) > div.css-137y4f0 > div.css-1qyqq5q > table > tbody > tr:nth-child(1) > td.item.css-1vxu0ws > div > div.item-name
    name = driver.find_element(By.CSS_SELECTOR, 'h3').text
    tactical = driver.find_element(By.CSS_SELECTOR, 'td.tactical-skill > * span').text
    augment = driver.find_element(By.CSS_SELECTOR, 'div.core-augment-info-name:nth-of-type(1)').text
    # subject_info[number].click() - 클릭은 작동을 안 함 아마 자바스크립트 이슈인듯?
    time.sleep(2)
    tier_build.append([name, tactical, augment])
    driver.back()     

local_file_path = '/home/ubuntu/damf2/data/er/'

def save_to_csv(song_list):

    with open(local_file_path + 'eternal-return-tier-build.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(tier_build)

save_to_csv(tier_build)
    

