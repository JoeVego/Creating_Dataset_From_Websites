from selenium import webdriver
from PIL import Image, ImageDraw
import numpy as np

def lets_try():
    PATH_PC = 'S:\\geckodriver\\geckodriver.exe'
    PATH_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\geckodriver.exe'
    driver = webdriver.Firefox()
    driver.get("https://ya.ru/")

    PATH_PIC_PC = 'S:\\test.png'
    PATH_PIC_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\test.png'
    # driver.get_full_page_screenshot_as_png()
    #
    # Установка размера окна
    # # Setting the window size to 1200 * 800
    driver.set_window_size(1212, 1291)
    driver.save_screenshot(PATH_PIC_NB)

    # html = driver.page_source
    # print(html)
    # driver.quit()

    # разные поиски по классуЦсс, или find_element_by_tag_name
    elements = driver.find_elements("xpath", "//button | "
                                             "//input[@type='submit'] | "
                                             "//input[@type='button'] | "
                                             "//input[@class='submit'] | "
                                             "//input[@class='button'] |  "
                                             "//a[@class='submit']  |"
                                             "//a[@type='button']  |"
                                             "//a[@type='submit']  |"
                                             "//a[@class='button']  |"
                                             "//div[@class='button']   |"
                                             "//div[@type='button']   |"
                                             "//div[@class='submit']   | "
                                             "//li[@class='button'] |"
                                             "//div[@type='submit'] | "
                                             "//li[@type='submit'] |"
                                             "//li[@type='button'] |"
                                             "//li[@class='submit']")
    print("elements = ", elements)
    for elem in elements:
        # dict.get(key, default) - возвращает значение ключа, но если его нет,
        # не бросает исключение, а возвращает default (по умолчанию None).
        print("Loc : \n", "x =", elem.location['x'], ", y =", elem.location['y'])
        width_el = elem.size['width']
        height_el = elem.size['height']
        print("Sizes : \n", "width =", width_el, "height =", height_el, "\n\n")


    driver.quit()

    img = Image.open(PATH_PIC_NB)
    img = img.convert('RGB')
    numpy_array = np.array(img)
    print("after convert to RGB =", numpy_array.shape)

    img_draw = ImageDraw.Draw(img, mode='RGB')
    # img_draw.rectangle([786, 554, 929, 608], outline='green', width= 3)
    img_draw.rectangle([786, 554, 828, 606], outline='green', width=3) - Неверно выбрал нач точку
    # img_draw.rectangle([1115, 1124, 929, 608], outline='green', width=3)
    img.show()

    # - beautiful soap - parsing html