#Write a short program that prints each number from 1 to 100 on a new line.
#For each multiple of 3, print "Fizz" instead of the number.
#For each multiple of 5, print "Buzz" instead of the number.
#For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
#Write a solution (or reduce an existing one) so it has as few characters as possible.

#Scoring
#Your score is: (200 - number of characters in code) / 100
lst = []
fb_lst = []

for n in range(1, 101):
    n = n + 0
    lst.append(n)
    fb_lst.append(n)

# operator % radi to da deli broj sa drugim brojem i ostavlja "ostatak" - 4/5 = 1 ili 3/1 = 2.
# Logika iza i%3 je da nalazi sve brojeve deljive sa 3 iza kojih ostaje 0. if not i%3 je ista logika drugacije formulisana!
# ** trazenje brojeva deljivih sa 3 i zamena za rec Fizz koju ubacujemo u novu listu koristeci index

for i in lst:
    if i%3 == 0:
        i = lst.index(i)
        fizz = "Fizz"
        fb_lst[i] = fizz

for k in lst:
    if not k%5:
        k = lst.index(k)
        buzz = "Buzz"
        fb_lst[k] = buzz

for v in lst:
    if not v%5 and not v%3:
        v = lst.index(v)
        fizzbuzz = "FizzBuzz"
        fb_lst[v] = fizzbuzz

# listanje svih vrednosti u novom redu
for item in fb_lst:
    print(item)


#INTERNET Solution:
#for num in range(1,101):
#   if num % 15 is 0:
#        print("Fizzbuzz")
#    elif num % 3 is 0:
#        print("Fizz")
#    elif num % 5 is 0:
#        print("Buzz")
#    else:
#        print(num)
