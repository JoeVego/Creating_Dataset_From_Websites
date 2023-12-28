from selenium import webdriver
from PIL import Image, ImageDraw
import numpy as np


def better_version(driver_path, pic_path, url):
    """Возможно поверху будет цикл пробегающийся по урлам,
    поэтому тут внутри работаем с 1 картинкой"""

    driver = webdriver.Firefox()
    driver.get(url)
    # Установка размера окна
    driver.set_window_size(1212, 1291)
    # driver.get_full_page_screenshot_as_png()
    driver.save_screenshot(pic_path)

    # html = driver.page_source
    # print(html)
    # driver.quit()
    # Существуют разные поиски по классуЦсс, find_element_by_tag_name и тп.
    list_of_elements_name = ["button", "text"]

    for element_name in list_of_elements_name:
        if (element_name == "button"):
            xpath_query = ("//button | "
                           "//input[@type='submit'] | "
                           "//input[@type='button'] | "
                           "//input[@class='submit'] | "
                           "//input[@class='button'] | "
                           "//a[@class='submit'] |"
                           "//a[@type='button'] |"
                           "//a[@type='submit'] |"
                           "//a[@class='button'] |"
                           "//div[@class='button'] |"
                           "//div[@type='button'] |"
                           "//div[@class='submit'] | "
                           "//li[@class='button'] |"
                           "//div[@type='submit'] | "
                           "//li[@type='submit'] | "
                           "//li[@type='button'] | "
                           "//li[@class='submit']")
        else:
            xpath_query = ("//" + element_name + " | "
                                                 "//input[@type='" + element_name + "'] | "
                                                                                    "//input[@class='" + element_name + "'] | "
                                                                                                                        "//a[@type='" + element_name + "']  | "
                                                                                                                                                       "//a[@class='" + element_name + "']  | "
                                                                                                                                                                                       "//div[@class='" + element_name + "']   | "
                                                                                                                                                                                                                         "//div[@type='" + element_name + "']   | "
                                                                                                                                                                                                                                                          "//li[@class='" + element_name + "'] | "
                                                                                                                                                                                                                                                                                           "//li[@type='" + element_name + "']")

        print("xpath =", xpath_query)
        xpath_query_result = driver.find_elements("xpath", xpath_query)
        print(element_name, " =", xpath_query_result, "\n")

        img = Image.open(pic_path)
        # цвет может раньше конвертировать а не тут - потом убирем отсюда
        img = img.convert('RGB')
        img_draw = ImageDraw.Draw(img, mode='RGB')
        # приведение к массиву
        # numpy_array = np.array(img)
        # print("after convert to RGB =", numpy_array.shape)

        for web_element in xpath_query_result:
            print(" here !")
            print(web_element)
            start_x = web_element.location['x']
            start_y = web_element.location['y']
            width = web_element.size['width']
            height = web_element.size['height']
            print(" here ! !")
            print("Loc : \n", "x =", start_x, ", y =", start_y)
            print("Sizes : \n", "width =", width, "height =", height, "\n\n")

            if element_name == "button":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='red',
                                   width=3)
            else:
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='green',
                                   width=3)

        img.show()
        driver.quit()
