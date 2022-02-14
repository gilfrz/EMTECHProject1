from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products
from lifestore_file import lifestore_searches

#50 productos con mayores ventas
contador1 = dict() #diccionario para contener (nombre_producto, no_ventas)
for producto in lifestore_sales:
    venta = producto[0]
    producto_id = producto[1]
    rembolso = producto[4]    
    for prod in lifestore_products:
            id_prod = prod[0]
            nombre = prod[1]
            categoria = prod[3]
            if producto_id == id_prod:
                contador1[nombre] = contador1.get(nombre,0)+1   

#listado mayores ventas
ventas_ordenadas = list()
for n,v in contador1.items():
    ventas_ordenadas.append((v,n))
    ventas_ordenadasUP = sorted(ventas_ordenadas,reverse=True)

print('Los 5 productos con mayores ventas fueron: \n')
for i in ventas_ordenadasUP[:5]:
    sales = i[0]
    name = i[1]
    print(f'El producto:{name}\n tuvo:{sales} ventas\n')    

#PRODUCTOS CON MAYORES BÚSQUEDAS
#las busquedas totales por producto se parean con el nombre del producto
contador2 = dict()
for producto in lifestore_searches:
    venta = producto[0]
    producto_id = producto[1]    
    for prod in lifestore_products:
            id_prod = prod[0]
            nombre = prod[1]
            if producto_id == id_prod:
                contador2[nombre] = contador2.get(nombre,0)+1 

#los productos son ordenados en una lista
busquedas_ordenados = list()
for n,v in contador2.items():
    busquedas_ordenados.append((v,n))
    busquedas_ordenadosUP=sorted(busquedas_ordenados,reverse=True) 
    busquedas_ordenadosDOWN=sorted(busquedas_ordenados,reverse=False)

print('Los 10 productos con mayores búsquedas fueron: \n')
#se imprime la lista de productos mas buscados
for i in busquedas_ordenadosUP[:10]:
    searches = i[0]
    name = i[1]
    print(f'El producto: {name} tuvo: {searches} búsquedas\n')

