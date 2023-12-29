from selenium import webdriver
from PIL import Image, ImageDraw
import numpy as np


def create_dataset_pictures(pic_path, url):
    """Возможно поверху будет цикл пробегающийся по урлам,
    поэтому тут внутри работаем с 1 картинкой

    Возвращает картинку с найденными элементами и метки к ней.
    В формате json или двумерная таблица
        изображения:
            "file_name"- имя файла в каталоге изображений
            url
            id - файла
        категории
            id - Каждая категория имеет уникальный "id", и они должны находиться в диапазоне [1, количество категорий]
        аннотации
                "segmentation": список пикселей маски сегментации;
                    это сплющенный список пар, поэтому вы должны взять первое и второе значение (x и y на картинке),
                    затем третье, четвертое и т. д., чтобы получить координаты; обратите внимание,
                    что это не индексы изображений, поскольку они являются плавающими числами -
                    они создаются и сжимаются такими инструментами, как COCO-annotator, из необработанных координат пикселей
                "area": количество пикселей внутри маски сегментации
                "image_id": поле id из словаря изображений; предупреждение:
                    это значение следует использовать для перекрестной ссылки на изображение с другими словарями, а не с полем "id"!
                "bbox": ограничивающая рамка, т. е. координаты (верхний левый x, верхний левый y, ширина, высота)
                    прямоугольника вокруг объекта; очень полезно извлекать отдельные объекты из изображений,
                    поскольку во многих языках, таких как Python, это можно сделать, обратившись к массиву изображений,
                    например cropped_object = image[bbox[0]:bbox[0] + bbox[2], bbox[1]:bbox[1] + bbox[3]]
                "category_id": класс объекта, соответствующий полю "id" в "categories"
                "id": уникальный идентификатор аннотации; предупреждение:
                    это только идентификатор аннотации, он не указывает на конкретное изображение в других словарях!

    """

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
    # кнопка, меню, надпись, окно, поле ввода, лист, таблица
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
        xpath_query = "//" + element_name

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
                                   outline='orange',
                                   width=3)
            else:
                img_draw.rectangle([start_x, start_y, start_x + width, start_y + height],
                                   outline='green',
                                   width=3)

            img.save(pic_path)
        img.show()
    #     ДОБАВИТЬ КАРТИНКУ И ПОДПИСИ НЕ ТОЛЬКО ФОРМИРОВАНИЕ КАРТИНОК НО И ТХТ МЕТОК НУЖЕН
    driver.quit()
