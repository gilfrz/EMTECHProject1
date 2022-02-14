
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products



# Dividir por meses las ventas
id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
# Para categorizar usamos un diccionario
categorizacion_meses = {}

for par in id_fecha:
    # Tengo ID y Mes
    id = par[0]
    _, mes, _ = par[1].split('/')
    # Si el mes aun no existe como llave, la creamos
    if mes not in categorizacion_meses.keys():
        categorizacion_meses[mes] = []
    categorizacion_meses[mes].append(id)

ingresos=[]
cantidad_ventas=[] #lista de número de ventas por mes
meses_mayoresventas = [] #lista de meses con mayores ventas
print('Para las ventas promedio mensuales se tiene:\n')
for key in categorizacion_meses.keys():
    lista_mes = categorizacion_meses[key]
    suma_venta = 0
    for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        precio = lifestore_products[id_product-1][2]
        suma_venta += precio
    if suma_venta not in ingresos:
        ingresos.append(suma_venta)
        cantidad_ventas.append(len(lista_mes))
    if key =='01': 
        print(f'Enero tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='02': 
        print(f'Febrero tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='03': 
        print(f'Marzo tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='04': 
        print(f'Abril tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='05': 
        print(f'Mayo tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='06': 
        print(f'Junio tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='07': 
        print(f'Julio tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    elif key =='08': 
        print(f'Agosto tuvo ingreso total de: {suma_venta}, ventas totales: {len(lista_mes)}')
    venta_mensual_prom=sum(cantidad_ventas)/len(cantidad_ventas)
    if len(lista_mes)> venta_mensual_prom:
        meses_mayoresventas.append(key)

print(f'\nEl total de ingresos fue: {sum(ingresos)}\n')

print(f'El número de ventas promedio mensual: {venta_mensual_prom}\n')

print('Los meses con mayor número de ventas fueron:')
for i in sorted(meses_mayoresventas):
    if i == '01':
        print('Enero')
    elif i == '02':
        print('Febrero')
    elif i == '03':
        print('Marzo')
    elif i == '04':
        print('Abril')
    elif i == '05':
        print('Mayo')
    elif i == '06':
        print('Junio')
    elif i == '07':
        print('Julio')
    elif i == '08':
        print('Agosto')
    elif i == '09':
        print('Septiembre')
