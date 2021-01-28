import random
import string

from PIL import Image


def gen_name():
    """
        Функция генерации случайной последовательности букв для формирования уникального имени изображений
        Возвращает строку вида: '_aBcDeF'
    """
    res = '_' + ''.join(random.choice(string.ascii_letters) for x in range(5)) + '.'
    return res


def get_path(raw_path):
    """
        Функция получения пути, имени и расширения для конкретного файла
        Получает строку вида: '/media/googlelogo.png'
        Возвращает строку вида: 'media\googlelogo_FEJjl.png'
    """
    res = raw_path.split('.')[0] + gen_name() + raw_path.split('.')[1]
    return res.replace("/", "\\")[1:len(res)]


def reformat_image(img_path, path, *args):
    """
        Функция скалирует изображение на указанное число пикселей, сохраняя пропорции, потом сохраняет его
        Входные данные:
        img_path -- путь к изображению
        path -- путь для сохранения изображения
        args -- ширина и длина
        Возвращает 'OK' в случае успеха и None в случае неверно введённых данных
    """
    img = Image.open(img_path)

    try:
        width = int(args[0])
    except Exception as e:
        print(e)
        width = img.width
    try:
        height = int(args[1])
    except Exception as e:
        print(e)
        height = img.height

    if height != img.height and width != img.width:
        if height/width != img.height/img.width:
            return None

    transposed = False
    if args[1]:
        img = img.transpose(Image.ROTATE_90)
        width = height
        transposed = True

    wpercent = (width / float(img.width))
    hsize = int((float(img.height) * float(wpercent)))
    img = img.resize((width, hsize))

    if transposed:
        img = img.transpose(Image.ROTATE_270)

    img.save(path)
    return 'OK'
