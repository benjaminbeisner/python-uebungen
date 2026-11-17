RHO = 0.8  # Dichte von Alkohol in g/ml

personen = [
    {"geschlecht": "Mann", "masse": 70, "r": 0.7},
    {"geschlecht": "Mann", "masse": 80, "r": 0.7},
    {"geschlecht": "Frau", "masse": 60, "r": 0.6},
    {"geschlecht": "Frau", "masse": 70, "r": 0.6},
]

getraenke = [
    {"name": "Bier", "eps": 0.05, "volumina": [500, 1000]},
    {"name": "Wein", "eps": 0.12, "volumina": [200, 400]},
    {"name": "Scotch", "eps": 0.46, "volumina": [20, 40]},
]


def blutalkohol(m, r, v, eps):
    a = v * eps * RHO  # aufgenommene Alkoholmasse in g
    return a / (m * r)  # Konzentration in g/kg (Promille)


for g in getraenke:
    for p in personen:
        for v in g["volumina"]:
            c = blutalkohol(p["masse"], p["r"], v, g["eps"])
            print(f'{g["name"]:7}{p["geschlecht"]:5}{p["masse"]:3} kg {v:5} ml -> {c:.2f} ‰')