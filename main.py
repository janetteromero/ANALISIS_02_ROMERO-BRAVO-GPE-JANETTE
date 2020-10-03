import pandas as pd

Data_set = pd.read_csv("synergy_logistics_database.csv")
x = Data_set.iloc[:, :].values
aire = 0
camino = 0
mar = 0
vias = 0
total = 1
total_a= 0
total_c= 0
total_m= 0 
total_r= 0


for register_id, direction, origin, destination, year, date1, product, transport_mode, company_name, total_value in x:
      
    total + total + 1
    if direction == "Exports":
      if transport_mode == "Air":
        aire = aire+1
        total_a=total_value+total_a
      if transport_mode == "Road":
        camino = camino+1
        total_c=total_value+total_c
      if transport_mode == "Sea":
        mar = mar+ 1
        total_m = total_value+total_m
      if transport_mode == "Rail":
        vias =  vias+1
        total_r= total_value+total_r
    if direction =="Imports":
      if transport_mode == "Air":
        aire = aire+1
        total_a=total_a-total_value
      if transport_mode == "Road":
        camino = camino+1
        total_c=total_c-total_value
      if transport_mode == "Sea":
        mar = mar+ 1
        total_m=total_m-total_value
      if transport_mode == "Rail":
        vias =  vias+1      
        total_r=total_r-total_value

total_a=total_a/aire
total_c=total_c/camino
total_m=total_m/mar
total_r=total_r/vias

print ("Total de envios por aire:" ,aire)
print(total_a)
print ("Total de envios por camino:", camino)
print(total_c)
print ("Total de envios por riel:",vias)
print(total_r)
print ("Total de envios por mar:", mar)
print(total_m)
print("El generador de menos ingresos es el mar debido a la poca remuneracicon pero es el de mayor demanda")


print(x)
