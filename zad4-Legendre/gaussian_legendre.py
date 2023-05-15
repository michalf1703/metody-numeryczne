import functions as f

# Definiujemy węzły oraz wagi dla kwadratury Gaussa-Legendre'a dla wielomianów Legendre'a
# Odpowiednie wartości zostały już obliczone i zapisane w liście legendre_polynomials_solutions i gaussian_legendre_factors
legendre_polynomials_solutions = [
    [-0.577350269189625764509, 0.577350269189625764509],
    [-0.774596669241483377036, 0.000000000000000000000, 0.774596669241483377036],
    [-0.861136311594052575224, -0.339981043584856264803,
     0.339981043584856264803, 0.861136311594052575224],
    [-0.906179845938663992798, -0.538469310105683091036, 0.000000000000000000000,
     0.538469310105683091036, 0.906179845938663992798]
]

gaussian_legendre_factors = [
    [1.000000000000000000000, 1.000000000000000000000],
    [0.555555555555555555556, 0.888888888888888888889, 0.555555555555555555556],
    [0.347854845137453857373, 0.652145154862546142627, 0.652145154862546142627, 0.347854845137453857373],
    [0.236926885056189087514, 0.478628670499366468041, 0.568888888888888888889,
     0.478628670499366468041, 0.236926885056189087514]
]

# Funkcja do obliczania całki za pomocą kwadratury Gaussa-Legendre'a
def gaussian_legendre_quadrature(a: float, b: float, flag: str, node_count: int) -> float:
    result = 0.
    for i in range(node_count):
        # Obliczamy punkt t na podstawie węzła z tablicy legendre_polynomials_solutions
        t = ((a + b) / 2) + ((b - a) / 2) * legendre_polynomials_solutions[node_count - 2][i]
        # Dodajemy wartość składnika do wyniku całkowania
        result += ((b - a) / 2) * gaussian_legendre_factors[node_count - 2][i] * f.function_value(t, flag)
    # Zwracamy wynik całkowania
    return result
