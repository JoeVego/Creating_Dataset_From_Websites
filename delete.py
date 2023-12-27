from selenium import webdriver
from PIL import Image
import numpy as np

def lets_try():
    PATH_PC = 'S:\\geckodriver\\geckodriver.exe'
    PATH_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\geckodriver.exe'
    driver = webdriver.Firefox()
    driver.get("https://ya.ru/")

    PATH_PIC_PC = 'S:\\test.png'
    PATH_PIC_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\test.png'
    # driver.get_full_page_screenshot_as_png()
    driver.save_screenshot(PATH_PIC_NB)

    # html = driver.page_source
    # print(html)
    # driver.quit()

    elements = driver.find_elements("xpath", "//button | //input[@type='submit'] | // input[@type='button']")
    print("elements = ", elements)
    for elem in elements:
        print(elem.location)

    driver.quit()

    img = Image.open(PATH_PIC_NB)
    img = img.convert('RGB')
    numpy_array = np.array(img)
    print(numpy_array.shape)

    # - beautiful soap - parsing html