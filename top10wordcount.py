name = input('Enter file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
#encoding="utf8" se koristi kada izbaci encoding error, dva najcesca su utf-8 i Latin-1
fhand = open(name, encoding="utf8")
counts = dict()
# analizira file, razdvaja na redove, onda na reci i konacno
# pravi count za recnik/dodaje nove reci-vrednosti *retrieve-create-update

for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# pravi listu, u listi menja redosled vrednosti i kljuca, dodaje tuple u listu,
# sortira naopacke (reverse) list is printuje prvih 10

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)
    lst = sorted(lst, reverse = True)
for val, key in lst[:10] :
    print(key,val)


# napravi analizu i promeniti kod da svi predlozi, recce,
# spojnici i sl. koji obicno prave top 20 reci budu izbaceni


#BONUS:
# kraca verzija
# print(sorted [(v,k) for k,v in counts.items()]) - menja sve od reda 16-22
