from tabulate import tabulate

def funcion(x):
	return -25_182*x - 90*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5

def bisec(f, a, b, tol, n):
	"""Usa el método de la bisección para el cálculo de las raices en una función
	
	Parametros:
	:f. Es la función a la cual se le quiere calcular la raiz
	:a. Es el valor inicial del intervalo
	:b. Es el valor final del intervalo
	:tol. Es la tolerancia máxima que puede soportar el programa, es decir, el error máximo
	:n. Número de iteraciones

	La función retorna el valor de la raíz, o en caso de no encontrarlo retorna None
	"""

	table = [
		['a', 'c', 'b', 'f(a)', 'f(c)', 'f(b)', 'e']
	]

	anterior = 0
	i = 1
	while i <= n:
		c = (a+b) / 2
		fc = f(c)

		if i == 1:
			error = 1
		else:
			error = abs((c - anterior) / c)

		table.append([a, c, b, f(a), f(c), f(b), f'{error:%}'])

		if abs(fc) <= 1e-15 or error < tol:
			return c, tabulate(table, headers='firstrow', tablefmt='fancy_grid')

		if fc*f(a) > 0:
			a = c
		else:
			b = c

		anterior = c
		i += 1
	
	return None, tabulate(table, headers='firstrow', tablefmt='fancy_grid')

if __name__ == '__main__':
	i1 = -11
	f1 = -10

	c1, table1 = bisec(funcion, i1, f1, 2e-3, 100)
	print(table1)
	print(f'{c1 = }\n\n')


	i2: int = -1
	f2: int = 1

	c2, table2 = bisec(funcion, i2, f2, 2e-3, 100)
	print(table2)
	print(f'{c2 = }\n\n')


	i3: int = 16
	f3: int = 17

	c3, table3 = bisec(funcion, i3, f3, 2e-3, 100)
	print(table3)
	print(f'{c3 = }')
	