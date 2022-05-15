print('Wybierz: papier / kamien / nozyczki')

#import getpass

gracz1_wynik = 0
gracz2_wynik = 0

opcje = ['papier', 'kamien', 'nozyczki']

def pobierz_wybor(gracz):
    while True:
        wybor_gracza = input(f'{gracz} podaj swoj wybor : ')
        if wybor_gracza in opcje:
            return wybor_gracza

while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracza1 = pobierz_wybor('Gracz1')
    wybor_gracza2 = pobierz_wybor('Gracz2')
      
    if wybor_gracza1 == 'papier' and wybor_gracza2 == 'kamien' \
    or wybor_gracza1 == 'kamien' and wybor_gracza2 == 'nozyczki' \
    or wybor_gracza1 == 'nozyczki' and wybor_gracza2 == 'papier':
      print ('Gracz1 wygrywa')
      gracz1_wynik += 1
    elif wybor_gracza1 == wybor_gracza2:
      print('Remis')
    else:
      print('Gracz2 wygral')
      gracz2_wynik += 1
    
if gracz1_wynik > gracz2_wynik:
  print('Cala gre wygral GRACZ 1')
else:
  print('Cala gre wygral GRACZ 2')
