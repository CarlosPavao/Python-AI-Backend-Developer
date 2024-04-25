times = ["Atletico MG", "Palmeiras", "São Paulo", "Cruzeiro"]

print(times)

print("append".center(20, "#"))
print(times.append("Coritiba"))

print("copy".center(20, "#"))
time2 = times.copy()
print(time2)

print("count".center(20, "#"))
times.append("Palmeiras")
times.append("Palmeiras")
print(times)
print(times.count("Palmeiras"))

print("extend".center(20, "#"))
print(times)
times.extend(["Santos", "Fortaleza"])
print(times)

print("index".center(20, "#"))
print(times.index("Santos"))

print("pop".center(20, "#"))
print(times)
times.pop()
print(times)

print("remove".center(20, "#"))
print(times)
times.remove("São Paulo")
print(times)

print("reverse".center(20, "#"))

print(times)
times.reverse()
print(times)

print("sort".center(20, "#"))
times.sort()
print(times)

print("len".center(20, "#"))
print(times)
print(len(times))

print("sorted".center(20, "#"))
print(sorted(times, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(times, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print("clear".center(20, "#"))
times.clear()
print(times)

