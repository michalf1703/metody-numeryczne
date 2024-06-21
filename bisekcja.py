import funkcje as f

#metoda znajdujaca miejsca zerowe funkcji wybranej przez uzytkownika za pomoca metody bisekcji z wykorzystaniem kryterium stopu poprzez osiagniecie zadanej dokladnosci obliczen
def bisekcjaEps(x_min, x_max, dokladnosc, wyborFunkcja):
#podane krance przedzialu podstawiamy do funkcji wybranej przez uzytkownika
    fa = f.function(x_min,wyborFunkcja)
    fb = f.function(x_max,wyborFunkcja)
#zliczamy liczbe wykonanych iteracji na potrzeby sprawodzania
    iteracja = 0
#sprawdzamy poprawnosc zalozenia o przeciwnych znakach funkcji na krancach badanego przedzialu
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0), na danym przedziale nie ma miejsc zerowych.")
    else:
        guardian = True
        while guardian is True:
            iteracja += 1
#suma krancow przedzialu / 2 , czy wynik tego dzialania bedzie f(x1) =0 ??
            x0 = (x_min + x_max) / 2
            fx0 = f.function(x0, wyborFunkcja)
#warunek zakonczenia; WARIANT A
            if abs(x_max - x_min) < dokladnosc:
                return x0, iteracja
#jesli f(x_max)(czyli f(b) * f(x0) < 0 to do dolnej wartosci f((a)) przedzialu przypisujemy wynik x0 (czyli x_min + x_max /2)
            if fx0 * fb < 0:
                x_min = x0
# jesli f(x_min)(czyli f(a) * f(x0) < 0 to do gornej (f(b)) wartosci przedzialu przypisujemy wynik x0 (czyli x_min + x_max /2)
            else:
                x_max = x0
                fb = fx0


#metoda znajdujaca miejsca zerowe funkcji wybranej przez uzytkownika za pomoca metody biskecji z wykorzystaniem kryterium stopu poprzez wykonanie okreslonej liczby iteracji
def bisekcjaIter(x_min, x_max, iteracja, wyborFunkcja):
# podane krance przedzialu podstawiamy do funkcji wybranej przez uzytkownika
    fa = f.function(x_min,wyborFunkcja)
    fb = f.function(x_max,wyborFunkcja)
# sprawdzamy poprawnosc zalozenia o przeciwnych znakach funkcji na krancach badanego przedzialu
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0) ")
    else:
# algorytm bedzie sie wykonywal do momentu osiagniecia zadanej iteracji
        while iteracja > 0:
# suma krancow przedzialu / 2 , czy wynik tego dzialania bedzie f(x1) =0 ??
            x0 = (x_min + x_max) / 2
            fx0 = f.function(x0, wyborFunkcja)
# jesli wartosc funkcji w punkcie przez nas obliczonym bedzie rowna zero to znalexlismy miejsce zeorwe
            if fx0 == 0:
                return x0
#jesli f(x_max)(czyli f(b) * f(x0) < 0 to do dolnej wartosci f((a)) przedzialu przypisujemy wynik x0 (czyli x_min + x_max /2)
            if fx0 * fb < 0:
                x_min = x0
# jesli f(x_min)(czyli f(a) * f(x0) < 0 to do gornej (f(b)) wartosci przedzialu przypisujemy wynik x0 (czyli x_min + x_max /2)
            else:
                x_max = x0
                fb = fx0
#zadana iteracja sie zmniejsza
            iteracja = iteracja - 1
        return x0