from selenium import webdriver
from PIL import Image
import numpy as np

def lets_try():
    driver = webdriver.Firefox(executable_path='S:\\geckodriver\\geckodriver.exe')
    driver.get("https://ya.ru/")

    driver.save_screenshot('S:\\test.png')
    driver.quit()

    img =  Image.open('S:\\test.png')
    numpy_array = np.array(img)
    print(numpy_array.shape)
    # убрать 4ую размерность ?
    # numpy_array2 = numpy_array[:, :, :-1]
    # print(numpy_array.shape)

    # гит проект
    # - beautiful soap - parsing html