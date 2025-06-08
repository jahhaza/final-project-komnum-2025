import sympy as sp

class FaktorisasiPolinom:
    def __init__(self, expr):
        self.x = sp.symbols('x')
        self.expr = expr
        self.faktor = None
        self.akars = []
    
    def faktorisasi(self):
        self.faktor = sp.factor(self.expr)
        self.akars = sp.solve(self.expr, self.x)
    
    def tampilkan_hasil(self):
        print(f"Fungsi f(x) = {self.expr}")
        print(f"Hasil Faktorisasi: {self.faktor}")
        
        print("\nAkar-akar f(x):")
        for i, akar in enumerate(self.akars, 1):
            print(f"x{i} = {round(float(akar), 2)}")

        koef = sp.Poly(self.expr).all_coeffs()
        a0 = koef[-1]
        a1 = koef[-2]
        b0 = koef[-3]
        print(f"\na0 = {a0}, a1 = {a1}, b0 = {b0}")

f_expr = sp.sympify("x**3 + 4*x**2 - 59*x - 126")

faktor = FaktorisasiPolinom(f_expr)
faktor.faktorisasi()
faktor.tampilkan_hasil()
