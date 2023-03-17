from module import *

hallgatok:list[Hallgato] = []
file = open(file='course.txt', mode='r', encoding='utf-8')
for s in file: hallgatok.append(Hallgato(s))

print(f'hallgatók száma: {len(hallgatok)} fő')

beo:int = 0
for h in hallgatok:
    beo += h.eredmenyek['backend']
print(f'backend modul átlaga: {beo / len(hallgatok)}%')

ljti:int = 0
for i in range(1, len(hallgatok)):
    if hallgatok[i].atlag > hallgatok[ljti].atlag:
        ljti = i
print(f'legjobb tanuló: {hallgatok[ljti].nev}')

print('akik már befizették a teljes összget:')
for h in hallgatok:
    if h.befizetes == 2600:
        print(f'\t- {h.nev}')

kn:str = input('írd be egy hallgató nevét: ')

for h in hallgatok:
    if h.nev == kn:
        if h.van_bukas:
            print('\taz alábbi tantárgyakból kell ismétlővizsgát tenni:')
            for k, v in h.eredmenyek.items():
                if v < 51: print(f'\t\t- {k} ({v}%-os eredmény)')
        else: print('\ta hallgatónak nem kell javítóvizsgát tennie')
        break
else: print(f'\tnincs ilyen nevű hallgató')