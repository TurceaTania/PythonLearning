'''
Flow control - if else
evalueaza conditii si bifurca codul in functie de rezultat
'''


# if
piesa_faina = True

print('Pornim radio')
if piesa_faina == True:
    print('Dam mai tare')
    print('Fredonam')
print('Oprim radio')


# if else
# daca nr este par printam acest lucru
# altfel printam impar
nr = 4
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 3 == 0:     # daca restul impartirii nr la 2 este 0
    print('numar par')
else:
    print('numar impar')

# este un nr pozitiv?
if nr > 0 :
    print('nr pozitiv')
else:
    print('nr nu este pozitiv')

# daca o persoana are sub 18 ani nu poate paria
varsta = 21
if varsta >= 18:
    print('Bine ati venit la casa de pariuri!' )
else:
    print('Nu puteti paria')

# daca ai luat sau nu bacul
nota_bac = 8
if nota_bac >= 6:
    print('Admis')
else:
    print('Respins')



# if, else if, else
# cum ne saluta un robotel in functie de ora?

# laum date de la tastatura
# ne asiguram ca sunt transformate din str in int
ora = int(input('Introdu ora'))
if ora < 0:
    print('Ora invalida.Ora negativa')
elif ora <= 11:
    print('Buna dimineata')
elif ora <= 18:
    print('Buna ziua')
elif ora <= 21:
    print('Buna seara')
elif ora <= 24:
    print('Noapte buna')
else:
    print('Ora invalida.Ora mai mare decat 24')

# CTRL + / => comenteaza sectiunea selectata

# viteza unei masini
# luam date de la tastatura
viteza = int(input('km/h'))
if viteza < 0:
    print('Viteza invalida')
elif viteza == 0:
    print('Masina stationeaza')
elif viteza <= 50:
    print('Masina se deplaseaza in localitate')
elif viteza <= 90:
    print('Masina se deplaseaza pe drum judetean')
else:
    print('Masina se deplaseaza pe autostrada')

# taxa postala pt scrisori in functie de greutate
# luam date de la tastatura
greutate = int(input('Introduceti greutatea'))
if greutate <= 1:
    print('Livrare gratuita')
elif greutate <= 25:
    print('Taxa de 10 bani')
elif greutate <= 50:
    print('Taxa de 25 bani')
elif greutate <= 75:
    print('Taxa de 50 bani')
elif greutate <= 100:
    print('Taxa de 1 leu')
elif greutate <= 200:
    print('Taxa de 2 lei')
else:
    print('Greutatea se incadreaza in alta categorie')









