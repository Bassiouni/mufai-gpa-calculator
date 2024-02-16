degrees = {}
hours = 0


with open('./degrees.txt', 'r') as f:
    for line in f.read().split('\n'):
        code, degree, hour = line.split(' ')

        degree = int(degree)
        hour = int(hour)

        if not degrees.get(code):
            hours += hour

        degrees[code] = (degree if degree >= 50 else 0, hour)


gpa = sum(map(lambda x: ((x[0] * x[1]) / 25) / hours, degrees.values()))

print(f'{gpa=} {hours=}')
