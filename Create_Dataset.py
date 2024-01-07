from selenium import webdriver
from PIL import Image, ImageDraw
import numpy as np


# Возможно поверху будет цикл пробегающийся по урлам и айдишникам
# поэтому внутри работаем с 1 картинкой
def create_dataset_pictures(picture_with_objects_path, screenshot_path, url):
    """Возвращает картинку с найденными элементами и метки к ней"""

    driver = webdriver.Firefox()
    driver.get(url)
    # Установка размера окна - чтобы на выходе получить 1200 на 1200
    driver.set_window_size(1212, 1291)
    # driver.get_full_page_screenshot_as_png()
    driver.save_screenshot(picture_with_objects_path)

    # получить хтмл страницы
    # html = driver.page_source
    # print(html)

    # Существуют разные поиски по классу: Цсс, find_element_by_tag_name и тп.
    # Текущий поиск: кнопка, меню, надпись, окно, поле ввода, лист, таблица
    list_of_elements_name = ["button", "menu", "label", "dialog", "input", "list", "table"]

    for element_name in list_of_elements_name:
        # if (element_name == "button"):
        #     # xpath_query = ("//button | "
        #     #                "//input[@type='submit'] | "
        #     #                "//input[@type='button'] | "
        #     #                "//input[@class='submit'] | "
        #     #                "//input[@class='button'] | "
        #     #                "//a[@class='submit'] |"
        #     #                "//a[@type='button'] |"
        #     #                "//a[@type='submit'] |"
        #     #                "//a[@class='button'] |"
        #     #                "//div[@class='button'] |"
        #     #                "//div[@type='button'] |"
        #     #                "//div[@class='submit'] | "
        #     #                "//li[@class='button'] |"
        #     #                "//div[@type='submit'] | "
        #     #                "//li[@type='submit'] | "
        #     #                "//li[@type='button'] | "
        #     #                "//li[@class='submit'] | "
        #     #                "//span[@type='submit'] | "
        #     #                "//span[@class='submit'] | "
        #     #                "//span[@class='button'] | "
        #     #                "//span[@type='button']")
        #     xpath_query = "//button"
        # else:
        #     xpath_query = ("//" + element_name + " | " +
        #                    "//input[@type='" + element_name + "'] | " +
        #                    "//input[@class='" + element_name + "'] | " +
        #                    "//a[@type='" + element_name + "']  | " +
        #                    "//a[@class='" + element_name + "']  | " +
        #                    "//div[@class='" + element_name + "']   | " +
        #                    "//div[@type='" + element_name + "']   | " +
        #                    "//li[@class='" + element_name + "'] | " +
        #                    "//li[@type='" + element_name + "']")

        # запрос просто по элемент хтмл
        xpath_query = "//" + element_name
        print("xpath =", xpath_query)

        xpath_query_result = driver.find_elements("xpath", xpath_query)
        print(element_name, " =", xpath_query_result, "\n")

        img = Image.open(picture_with_objects_path)
        # цвет может раньше конвертировать а не тут - потом убирем отсюда лишнюю строку
        img = img.convert('RGB')
        img_draw = ImageDraw.Draw(img, mode='RGB')

        # приведение к массиву
        # numpy_array = np.array(img)
        # print("after convert to RGB =", numpy_array.shape)

        for web_element in xpath_query_result:
            print("tag_name = ", web_element.tag_name)

            start_x = web_element.location['x']
            start_y = web_element.location['y']
            width = int(web_element.size['width'])
            height = int(web_element.size['height'])

            print("Loc : \n", "x =", start_x, ", y =", start_y)
            print("Sizes : \n", "width =", width, "height =", height, '\n')

            center_x, center_y = find_center_of_element(width, height)
            full_coordinates_x, full_coordinates_y = get_full_coordinates(start_x, start_y, center_x, center_y)
            # print("full_coordinates_x =", full_coordinates_x, '\n', "full_coordinates_y =", full_coordinates_y)

            normalized_center_x = normalization(full_coordinates_x)
            normalized_center_y = normalization(full_coordinates_y)
            print("normalized x =", normalized_center_x, '\n', "normalized y =", normalized_center_y)

            normalized_width = normalization(width)
            normalized_height = normalization(height)
            print("normalized width =", normalized_width, '\n', "normalized height =", normalized_height, '\n\n')

            # Обработку нулей в элементах сделать !!!

            if element_name == "button":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=3)
            else:
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='green',
                                   width=3)

            img.save(picture_with_objects_path)
        img.show()
    #     ДОБАВИТЬ КАРТИНКУ И ПОДПИСИ НЕ ТОЛЬКО ФОРМИРОВАНИЕ КАРТИНОК НО И ТХТ МЕТОК НУЖЕН
    driver.quit()


def find_center_of_element(width, height):
    if width % 2 != 0:
        center_x = width // 2
        center_x = center_x + 1
    else:
        center_x = width // 2

    if height % 2 != 0:
        center_y = height // 2
        center_y = center_y + 1
    else:
        center_y = height // 2

    return center_x, center_y


def get_full_coordinates(start_x, start_y, center_x, center_y):
    return start_x + center_x, start_y + center_y


def normalization(value):
    max_value = 1200
    min_value = 0
    # first = value - min_value
    # second = max_value - min_value

    # print("first =", first, " second =", second)

    return round((value - min_value) / (max_value - min_value), 6)
