import funkcje as f

#regula Falsi - regula falszywej prostej
#z tw.Talesa jest wyprowadzany ostateczny wzor na wyznaczanie wartosc x0
#https://eduinf.waw.pl/inf/alg/005_root/0011.php#:~:text=W%20j%C4%99zyku%20%C5%82aci%C5%84skim%20regula%20falsi%20oznacza%20fa%C5%82szyw%C4%85%20prost%C4%85.,prowadz%C4%85c%20lini%C4%99%20prost%C4%85%20%28sieczn%C4%85%29%20z%20punkt%C3%B3w%20kra%C5%84cowych%20przedzia%C5%82u.


#metoda znajdujaca miejsca zerowe funkcji wybranej przez uzytkownika
# za pomoca Zasady Falsi z wykorzystaniem kryterium stopu poprzez osiagniecie zadanej dokladnosci obliczen
def falsiEps(a, b, eps, flag):
# podane krance przedzialu podstawiamy do funkcji wybranej przez uzytkownika
    fa = f.function(a,flag)
    fb = f.function(b,flag)
#zliczamy liczbe wykonanych iteracji na potrzeby sprawodzania
    iter = 0
#sprawdzamy poprawnosc zalozenia o przeciwnych znakach funkcji na krancach badanego przedzialu
    if fa * fb > 0:
        print("Funkcja nie spełnia założeń (fa * fb >0) ")
    else:
        guardian = True
        while guardian is True:
            iter += 1
            x0 = b - (fb * (b - a)) / (fb - fa)
            fx0 = f.function(x0, flag)
            if abs(fx0) < eps:
                return x0, iter
            if fx0 * fb < 0:
                a = x0
                fa = fx0
            else:
                b = x0
                fb = fx0
            if abs(b - a) < eps:
                return (a + b) / 2, iter

def falsiIter(a, b, N, flag):
    fa = f.function(a,flag)
    fb = f.function(b,flag)
    iter = 0
    if fa * fb > 0:
        print("Funkcja nie spełnia założeń (fa * fb >0) ")
    else:
        guardian = True
        while iter < N and guardian is True:
            iter += 1
            x0 = b - (fb * (b - a)) / (fb - fa)
            fx0 = f.function(x0, flag)
            if fx0 == 0:
                return x0
            if fx0 * fb < 0:
                a = x0
                fa = fx0
            else:
                b = x0
                fb = fx0
            if iter == N:
                return x0
    return x0




