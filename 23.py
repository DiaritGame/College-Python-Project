def greet(name: str, age: int) -> None:
    print(f'Привет {name}, тебе {age}')

imya = input('Введи своё имя: ')
vozrast = int(input('Введи свой возраст: '))
greet(imya, vozrast)