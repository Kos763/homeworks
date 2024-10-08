def test_function():

    def inner_function():
        a = "Я в области видимости функции test_function"
        print(a)

    inner_fuction() # Ничего не возвращает


inner_function() # Ошибка
