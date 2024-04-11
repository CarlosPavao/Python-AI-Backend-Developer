times = { "Palmeiras", "São Paulo", "Corinthians", "ABC", "Sport", "Palmeiras"}
times_2 = { "Internacional", "Gremio", "Santos", "Fortaleza", "Ceara", "Juventude"}

numeros = {1, 2, 3}
numeros_2 = {2, 3, 4}
numeros_3 = {10, 20, 30, 4, 5, 6, 7, 8, 9}
numeros_4 = {2, 3, 4}

print("{}.union ".center(20, "#"))

print(times.union(times_2))

print("{}.intersection ".center(20, "#"))

print(numeros.intersection(numeros_2))

print("{}.difference ".center(20, "#"))

print(numeros.difference(numeros_2))
print(numeros_2.difference(numeros))

print("{}.symmetric_difference ".center(20, "#"))

print(numeros.symmetric_difference(numeros_2))

print("{}.issubset ".center(20, "#"))

print(numeros.issubset(numeros_2))
print(numeros_2.issubset(numeros))

print("{}.issuperset ".center(20, "#"))

print(numeros.issuperset(numeros_2))
print(numeros_2.issuperset(numeros))

print("{}.isdisjoint ".center(20, "#"))

print(numeros.isdisjoint(numeros_2))
print(numeros.isdisjoint(numeros_3))

print("{}.add ".center(20, "#"))
numeros.add(5)
numeros.add(6)
print(numeros)

print("{}.clear ".center(20, "#"))
print(numeros_2)
numeros_2.clear()
print(numeros_2)

print("{}.copy ".center(20, "#"))
numeros_4.copy()
print(numeros_4)
print("{}.discard ".center(20, "#"))

numeros_4.discard(2)
numeros_4.discard(25)
print(numeros_4)

print("{}.pop ".center(20, "#"))

print(times)
times.pop()
times.pop()
print(times)

print("{}.remove ".center(20, "#"))

print(numeros_4)
numeros_4.remove(4)
print(numeros_4)

print("{}.remove ".center(20, "#"))

print(numeros)
print(len(numeros))

print(" in ".center(20, "#"))

print(50 in numeros)
print(1 in numeros)





