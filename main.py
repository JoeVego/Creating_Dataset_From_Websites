from new_version import better_version

PATH_PC = 'S:\\geckodriver\\geckodriver.exe'
PATH_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\geckodriver.exe'
PATH_PIC_PC = 'S:\\test.png'
PATH_PIC_NB = 'C:\\Users\\Admin\\Desktop\\Учебные материалы\\вкр\\test.png'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # url = "https://ya.ru/"
    # url = "https://www.avito.ru/"
    url = "https://developer.mozilla.org/ru/docs/Web/HTML/Element"

    better_version(PATH_NB, PATH_PIC_NB, url)



