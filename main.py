import pandas as pd
from Create_Dataset import create_dataset_pictures

DRIVER_PATH_PC = 'S:\\geckodriver\\geckodriver.exe'
DRIVER_PATH_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\geckodriver.exe'
# тут в одну папку сохраняем скрины без квадратов наших
PATH_SCREENSHOT_PC = 'S:\\Project\\data\\objects\\images\picture'
PATH_SCREENSHOT_NB = 'C:\\Users\\Admin\\PycharmProjects\\VKR\\data\\objects\\images\\picture'
# тут в одну папку сохраняем скрины c квадратами
PATH_BOXES_PC = 'S:\\Project\\data\\objects\\images_with_boxes\picture'
PATH_BOXES_NB = 'C:\\Users\\Admin\\PycharmProjects\\VKR\\data\\objects\\images_with_boxes\\picture'
# а тут в другую папку сохраняем аннотации с выделением объектов
PATH_ANNOTATION_PC = 'S:\\Project\\data\\objects\\labels\label'
PATH_ANNOTATION_NB = 'C:\\Users\\Admin\\PycharmProjects\\VKR\\data\\objects\\labels\\label'


if __name__ == '__main__':
    # url = "https://developer.mozilla.org/ru/docs/Web/HTML/Element"
    # first_source_of_websites = pd.read_csv("data\\websites.csv", names=["index", "site", "rate"])
    # first_sites_list = first_source_of_websites['site'].to_list()
    second_source_of_websites = pd.read_csv("data\\second_sites.csv", names=["index", "site"])
    second_sites_list = second_source_of_websites['site'].to_list()

    # 72
    pic_id_counter = 112
    picture_with_boxes_path = PATH_BOXES_NB + str(pic_id_counter) + '.png'
    picture_path = PATH_SCREENSHOT_NB + str(pic_id_counter) + '.png'
    annotation_path = PATH_ANNOTATION_NB + str(pic_id_counter) + '.txt'

    for index in range(1000 - pic_id_counter):
        picture_with_boxes_path = PATH_BOXES_NB + str(pic_id_counter) + '.png'
        picture_path = PATH_SCREENSHOT_NB + str(pic_id_counter) + '.png'
        annotation_path = PATH_ANNOTATION_NB + str(pic_id_counter) + '.txt'

        create_dataset_pictures(picture_with_boxes_path, picture_path, annotation_path, second_sites_list[index])

        pic_id_counter = pic_id_counter + 1

