countries = [
{"name":"Poland", "population":38000000},
{"name":"England", "population":50000000},
{"name":"USA", "population":350000000},
{"name":"France", "population":50000000},
{"name":"Germany", "population":40000000}
]

for item in countries:
    print(f'{item['name']} {item['population']}')