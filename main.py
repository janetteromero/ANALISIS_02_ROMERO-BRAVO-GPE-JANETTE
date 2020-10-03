import pandas as pd

Data_set = pd.read_csv("synergy_logistics_database.csv")
x = Data_set.iloc[:, :].values
aire = 0
camino = 0
mar = 0
vias = 0
total = 1
for register_id, direction, origin, destination, year, date1, product, transport_mode, company_name, total_value in x:
    total + total + 1

    if {transport_mode} == "Air":
        aire = 10
    if {transport_mode} == "Road":
        camino += 1
    if {transport_mode} == "Sea":
        mar += 1
    if {transport_mode} == "Rail":
        vias += 1

print(aire, camino, mar, vias)
print(total)
print(x)
