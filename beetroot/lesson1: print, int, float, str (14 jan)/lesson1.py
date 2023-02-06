# 1 tema (2 urok)
# 14/01/23


print("Hello world!")
# This is my program
"""
aaaa
"""
"aaa"

print(123, end="")

quote = 123
quote = (int(quote / 1))
b = 2.0
print(quote)
print(type(quote))

print ("a", "b", "c")
print ("a", "b", "c", sep="-")

quote = 0.1
b = 0.2
c = quote + b
print(f"result = {c}")
print(f"result = {c:.2f}")
print(f"result = {100:0>4}")
print(f"result = {1000}")
print("result = %s" %c)
print("result = %.2f" %c)
print("result = %s // %.1f" %(1.0, c))
print("result = %s" % "hello")
print("result = {first_arg} // {second}". format(first_arg=1.0, second=c))
print("result = {first_arg} // {second:.2f}". format(first_arg=1.0, second=c))

# 2 tema (3 urok)

quote = 0.1
b = 0.2
c = quote + (b ** 2)
# ** це ступінь

#    0123456
quote = "Русня горить"
#показує скільки чисел у фразі (тут 12)
print(len(quote))
#повна фраза
print(quote[0:len(quote):1])
#остання буква, типу з кінця йде
print(quote[-1])
#задом наперед
print(quote[::-1])
#перше слово
print(quote[0:5:1])

quote = 591785439
print(str(quote)[5])

#        Русня Горить, москва Втонула"
quote = "Русня горить, Москва втонула"

mos_index = quote.find("Москва")

first_part = quote[0:mos_index]  #"Русня Горить, "
last_part = quote[mos_index:].title()[1:]  # "Москва втонула"
letter = quote[mos_index].lower()  # "м"
print(first_part + letter + last_part)

