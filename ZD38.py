class MyException1(Exception):
    pass
class MyException2(Exception):
    pass
class MyException3(Exception):
    pass
def cat_registration():
    print('---Регистрация котов на соревнование---')
    cat_name = str(input('Введите имя: '))
    try:
        if cat_name == 'Бобик':
            raise MyException1("Очень странное имя для кота.")
    except MyException1 as exc1:
        print(f'Ошибка: {exc1}')
        raise
    else:
        print(f'{cat_name} - прекрасное имя!')
    cat_age = int(input('Введите возраст: '))
    try:
        if cat_age <= 1:
            raise MyException2("Ты ещё слишком молод для нашего соревнования.")
    except MyException2 as exc2:
        print(f'Ошибка: {exc2}')
        raise
    else:
        print("Ты в самом расцвете сил!")
    cat_color = str(input('Введите цвет: '))
    try:
        if cat_color == 'чёрный':
            raise MyException3("Ты нам не очень нравишься, мы суеверные.")
    except MyException3 as exc3:
        print(f'Ошибка: {exc3}')
        raise
    else:
        print("Наш любимый цвет!")
    finally:
        print(f'Спасибо, {cat_name}! Ты ответил на все вопросы!')
cat_registration()