# a = 5
# b = 10
# c = a + b
# my_str = 'py_charm'
# print(c)
# print(my_str)

# name = input('Введите имя: ')
# age = input('Введите Ваш возраст: ')
# print(f'Имя: {name} \nВозраст: {age}')

# start_time = int(input('Введите секунды: '))
# hour = int(start_time / 3600)
# minute = int((start_time % 3600) / 60)
# sec = start_time % 60
# print(f'Время {hour}:{minute}:{sec}')

# count = int(input('Введите число: '))
# answer = count + int(str(count)*2) + int(str(str(count)*3))
# print(answer)

# count = int(input('Введите положительное натуральное число:\n'))
# max_count = count % 10
# count = count//10
# while count > 0:
#     if count % 10 > max_count:
#         max_count = count % 10
#     count = count//10
# print(f'Наибольшее число: {max_count}')

# viruchka = int(input('Введите выручку: \n'))
# izderska = int(input('Введите издержки: \n'))
# pribil = viruchka - izderska
# rentabelnost = pribil/viruchka
# if viruchka > izderska:
#     print('Фирма работает с прибылью!')
#     print(f'Рентабельность {rentabelnost}')
#     employers = int(input('Введите количество сотрудников: '))
#     pribil_na_employee = pribil/employers
#     print(f'Прибыль на сотрудника {pribil_na_employee}')
# elif izderska > viruchka:
#     print('Фирма работает в убыток!')

a = int(input('Введите количество километров за 1-ый день:\n'))
b = int(input('Введите количество километров, которое должен пробежать спортсмен на n-ый день:\n'))
i = 1
while a < b:
    i = i + 1
    a = a + a * 0.1
print(f'На {i} день')
