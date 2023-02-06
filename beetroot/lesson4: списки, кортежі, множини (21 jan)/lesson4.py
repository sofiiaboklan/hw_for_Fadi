# LESSON 4
# ТЕМА 6, 7

print("\nLESSON 4\n")

for (ind, val) in enumerate(range(40, 30, -1)):  # це тіпа тюпіл
    print(ind, val)

a = [2, 7, 15]
b = [3, 6, 8]
c = a + b

print(c)  # аби обʼєднати два списки

a = [2, 7, 15]
b = [3, 6, 8]
a.extend(b)  # інший варіант аби обʼєднати два списки

print(a)

a = [2, 7, 15]
b = [3, 6, 8]
c = [a, b]  # просто покаже два окремих списка
d = [*a, *b]  # * розпаковує обʼєкт і робить одним списком

print(c)
print(d)
print(*d)  # розпакує і покаже без рамок
e1, *e6, e7 = d  # * зробить список всередині
print(e1, e6, e7)

# e1, e2, e3, e4, e5, e6 = d  # по одному розпаковує
# print(d[0], d[1], ...)

d = [[1, 2, 3], ['a', 'b', 'c'], [7, 8, 9]]
a = sum(d, [])
print(a)


# тут ще дописати зі скрінів з уроку




# THEORY ТЕМА 6

print("\nTHEORY 6\n")

# СПИСКИ

print("LISTS\n")

browsers = ["Chrome", "Safari", "Firefox", "Edge"]
print("My fav browser is " + browsers[0])  # 0/-4 chrome, 1/-3 safari, 2/-2 firefox, 3/-1 edge
print(browsers[0:3])  # друкує з 0 по 3 браузер, тобто без еджу

browsers.append("Opera")  # додає оперу в кінці
print(browsers)

browsers.extend(["Opera", "Explorer", "Chromium"])  # складає список з двох списків
print(browsers)

browsers.insert(0, "Opera")  # ставить оперу на перше місце
print(browsers)

browsers.pop()
print(browsers)  # видаляє останній елемент

popped_item = browsers.pop()
print(browsers)
print(popped_item)  # повертає видалений елемент та виводиться окремо зі списку

popped_item = browsers.pop(1)
print(browsers)
print(popped_item)  # видаляє другий елемент і виводить його окремо зі списку

del browsers[1]
print(browsers)  # видаляє другий елемент

browsers.remove("Edge")
print(browsers)  # видалило едж

# browsers.sort()
# print(browsers)  # відсортувало список по алфавіту (назавжди)

print(sorted(browsers))  # відсортувало список по алфавіту (назавжди)
print(browsers)  # для перевірки: якщо тикнути після цього прінт, то список повернеться у оригінальний стан

browsers.reverse()  # назавжди змінить порядок списку
print(browsers)
browsers.reverse()  # можна реверснуть назад і повернеться до оригінального виду
print(browsers)


# КОРТЕЖІ

print("\nTUPLES\n")

pos = (100, 200)  # для створення кортежу з одним числом треба записати як (100, ) а не просто (100), бо сприйме як інт
print(pos[0])
pos = (100, 300)
print(pos)

countries = {"Sweden", "Norway", "Denmark"}
print(countries)
print("Norway" in countries)  # True

countries_EU = {"Germany", "Belgium", "Sweden", "Denmark"}
print(countries_EU.intersection(countries))  # показує які країни є і в ЄС і в кантріс
print(countries_EU.difference(countries))  # показує які країни є в ЄС але нема в кантріс
print(countries.difference(countries_EU))  # показує країни є в кантріс але не ма в ЄС
print(countries.union(countries_EU))  # додає ці два кортежі і показує як один

# THEORY ТЕМА 7

print("\nTHEORY 7\n")

countries = ["Ukraine", "Belarus", "France", "Germany",
             "Estonia", "Finland", "Poland", "Serbia"]
for i, country in enumerate(countries):
    countries[i] = (country, i+1)
print(countries)

sevens = []
for i in range(1, 71):
    if i % 7 == 0:
        sevens.append(i)
print(sevens)  # покаже числа від 1 до 71 не включно які діляться на 7

sevenss = []
i = 0
while i <= 70:
    sevenss.append(i)
    i += 7
print(sevenss)

"""
import random
points = 0
while True:
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print('points: ' + str(points))
    answer = input(str(x) + '+' + str(y) + '=? (type q to quit): ')
    if answer == 'q':
        break
    elif int(answer) != x+y:
        print("No points for you!")
        continue
    print("Good job!")
    points += 1
"""

countryy = {'name': 'Sweden', 'capital': 'Stockholm',
            'largest cities': ('Stockholm', 'Gothenburg', 'Malmo')}
print(countryy)
print(countryy['name'])

# countryy['population'] = 10000
# print(countryy)

countryy.update({'population': 10000, 'language': 'Swedish'})
print(countryy)

countryy['capital'] = 'Gothenburg'
print(countryy)

del countryy['largest cities']
print(countryy)

for key, value in countryy.items():
    print(key, ':', value)

empty_dict = {}
empty_set = set()
print(type(empty_set))
print(type(empty_dict))


seven = [i for i in range (0, 71, 7) if i % 5 != 0]
print(seven)

res = {i : i*i for i in range(2,20)}
print(res)

temp = []
for i in range(0, 10):
    if i % 2:
        continue
    temp.append(i)
print(sum(temp))

x = 10
for i in [1,2,3,4,5]:
    if i % 2 == 0:
        break
    x -= i
else:
    x = 10
print(x)