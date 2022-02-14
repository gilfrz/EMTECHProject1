from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

#50 productos con mayores ventas
#puntuacion_prom=[]
prod_evaluados = {}
prod_ranked={}
best_prod=[]

for par in lifestore_sales:
    # Tengo ID y review
    id = par[1]
    review = par[2]
    if id not in prod_evaluados.keys():
        prod_evaluados[id] = []
    prod_evaluados[id].append(review) #RESEÑAS CATEGORIZADAS POR PRODUCTOS
#print(prod_evaluados)

#LISTA DE (ID_PRODUCTOS,calif_prom) 
for i,j in prod_evaluados.items():
        prom = sum(j)/len(j)
        if i not in prod_ranked.keys():
                prod_ranked[i]=[]
        prod_ranked[i].append(prom)

#listas de productos mejor y peor rankeados 
for j,v in prod_ranked.items():
        best_prod.append((v,j))
        orderedUP=sorted(best_prod,reverse=True)
        orderedDOWN=sorted(best_prod)
#print(orderedUP)

print('\nLos 5 productos con mejor reseña fueron: \n')
#impresion de lista de mejores prod rankeados
for i in orderedUP[:5]:
        for product in lifestore_products:
            id_producto = product[0]
            nombre = product[1]
            if id_producto==i[1]:
                print(f'El producto {nombre} de ID {id_producto}, tiene una reseña promedio de {i[0]}')

print('\nLos 5 productos con peor reseña fueron: \n')
#impresión de lista de peores prod rankeados
for i in orderedDOWN[:5]:
        for product in lifestore_products:
            id_producto = product[0]
            nombre = product[1]
            if id_producto==i[1]:
                print(f'El producto {nombre} de ID {id_producto}, tiene una reseña promedio de {i[0]} ')
