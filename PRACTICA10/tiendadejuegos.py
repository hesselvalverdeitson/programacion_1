info_tienda=("titulos más jugados,2020")
inventario={
    "Sekiro":{"precio":500, "stock":15},

    "Silksong":{"precio":200, "stock":20},

    "Read_Dead_Redemption_2":{"precio":350, "stock":10},
}

print(inventario["Silksong"]["precio"])
inventario["Silksong"]["stock"] =19
print (inventario)
