from selenium import webdriver
from PIL import Image, ImageDraw
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException


# Возможно поверху будет цикл пробегающийся по урлам и айдишникам
# поэтому внутри работаем с 1 картинкой
def create_dataset_pictures(picture_with_boxes_path, screenshot_path, text_file_path, url):
    """Возвращает картинку с найденными элементами и метки к ней"""

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver = webdriver.Firefox()
    try:
        driver.get(url)
    except WebDriverException:
        print("Exc by url =", url)
        return
    

    # Установка размера окна - чтобы на выходе получить 1200 на 1200
    driver.set_window_size(1212, 1291)
    # driver.get_full_page_screenshot_as_png()
    # сохранили скрин страницы
    driver.save_screenshot(screenshot_path)

    # Существуют разные поиски по классу: Цсс, find_element_by_tag_name и тп.
    # Текущий поиск: кнопка, меню, надпись, окно, поле ввода, лист, таблица
    list_of_elements_name = ["button", "menu", "label", "dialog", "input", "list", "table"]
    # открываем картинку для дальнейшего рисования - обводка элементов не обязательная больше для своего интереса делаю
    img = Image.open(screenshot_path)
    text_file = open(file=text_file_path, mode='w')

    for element_name in list_of_elements_name:
        # запрос просто по элемент хтмл
        xpath_query = "//" + element_name
        print("xpath =", xpath_query)

        xpath_query_result = driver.find_elements("xpath", xpath_query)
        print(element_name, " =", xpath_query_result, "\n")

        # img = Image.open(screenshot_path)
        # цвет может раньше конвертировать а не тут - потом убирем отсюда лишнюю строку
        img = img.convert('RGB')
        img_draw = ImageDraw.Draw(img, mode='RGB')

        # приведение к массиву
        # numpy_array = np.array(img)
        # print("after convert to RGB =", numpy_array.shape)

        for web_element in xpath_query_result:

            start_x = web_element.location['x']
            start_y = web_element.location['y']
            width = int(web_element.size['width'])
            height = int(web_element.size['height'])

            # убираем нулевые элементы
            if width == 0 and height == 0:
                print("deleted element by zeros tag_name = ", web_element.tag_name)
                continue

            # убираем элементы вне видимого окна скрина
            if start_y > 1200:
                print("deleted element by size tag_name = ", web_element.tag_name)
                continue

            print("tag_name = ", web_element.tag_name)
            print("Loc : \n", "x =", start_x, ", y =", start_y)
            print("Sizes : \n", "width =", width, "height =", height)

            center_x, center_y = find_center_of_element(width, height)
            full_coordinates_x, full_coordinates_y = get_full_coordinates(start_x, start_y, center_x, center_y)
            # print("full_coordinates_x =", full_coordinates_x, '\n', "full_coordinates_y =", full_coordinates_y)

            normalized_center_x = normalization(full_coordinates_x)
            normalized_center_y = normalization(full_coordinates_y)
            print("Normalized : \n", "x =", normalized_center_x, "y =", normalized_center_y)
            # print("normalized x =", normalized_center_x, '\n', "normalized y =", normalized_center_y)

            normalized_width = normalization(width)
            normalized_height = normalization(height)
            print("width =", normalized_width, "height =", normalized_height, '\n\n')

            if element_name == "button":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("0 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            elif element_name == "menu":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("1 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            elif element_name == "label":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("2 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            elif element_name == "dialog":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("3 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            elif element_name == "input":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("4 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            elif element_name == "list":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("5 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            elif element_name == "table":
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='orange',
                                   width=2)
                text_file.write("6 " + str(normalized_center_x) +
                                " " + str(normalized_center_y) +
                                " " + str(normalized_width) +
                                " " + str(normalized_height) + "\n")
            # else:
            #     img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
            #                        outline='green',
            #                        width=2)
            #     text_file.write("2 " + str(normalized_center_x) +
            #                     " " + str(normalized_center_y) +
            #                     " " + str(normalized_width) +
            #                     " " + str(normalized_height) + "\n")

    img.save(picture_with_boxes_path)
    img.show()
    text_file.close()
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
