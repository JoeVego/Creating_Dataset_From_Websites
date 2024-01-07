from Create_Dataset import create_dataset_pictures

DRIVER_PATH_PC = 'S:\\geckodriver\\geckodriver.exe'
DRIVER_PATH_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\geckodriver.exe'
# тут в одну папку сохраняем скрины без квадратов наших
PATH_SCREENSHOT_PC = 'S:\\test'
PATH_SCREENSHOT_NB = 'C:\\Users\\Admin\\PycharmProjects\\VKR\\data\\objects\\images\\aaa'
# тут в одну папку сохраняем скрины c квадратами
PATH_BOXES_PC = 'S:\\test'
PATH_BOXES_NB = 'C:\\Users\\Admin\\PycharmProjects\\VKR\\data\\objects\\images_with_boxes\\aaa'
# а тут в другую папку сохраняем аннотации с выделением объектов
PATH_ANNOTATION_PC = 'S:\\test'
PATH_ANNOTATION_NB = 'C:\\Users\\Admin\\PycharmProjects\\VKR\\data\\objects\\labels\\aaa'


if __name__ == '__main__':
    # url = "https://www.avito.ru/"
    url = "https://developer.mozilla.org/ru/docs/Web/HTML/Element"

    pic_id_counter = 0
    picture_with_boxes_path = PATH_BOXES_NB + str(pic_id_counter) + '.png'
    picture_path = PATH_SCREENSHOT_NB + str(pic_id_counter) + '.png'
    #может быть неверно для тхт файлов делать как для картинок пока так оставляю
    annotation_path = PATH_ANNOTATION_NB + str(pic_id_counter) + '.txt'

    create_dataset_pictures(picture_with_boxes_path, PATH_SCREENSHOT_NB, url)



