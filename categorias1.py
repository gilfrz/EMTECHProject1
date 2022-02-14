from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

#VENTAS
contador1 = dict()
for producto in lifestore_sales:
    venta = producto[0]
    producto_id = producto[1]    
    for prod in lifestore_products:
            id_prod = prod[0]
            nombre = prod[1]
            category = prod[3]
            if producto_id == id_prod:
                contador1[(nombre,category)] = contador1.get((nombre,category),0)+1   
    
###########
lst_categorias=[] #lista de categorías
for i in lifestore_products:
    categoria = i[3]
    if categoria not in lst_categorias:
        lst_categorias.append(categoria)
    else:
        continue
#print(lst_categorias)

procesadores = list()
tarj_vid= list()
tarj_madre= list()
disc_d = list()
memorias= list()
pantallas= list()
bocinas= list()
audifonos= list()


for nom,vent in contador1.items():
    if 'procesadores' in nom:
        procesadores.append((vent,nom))
        procesadores=sorted(procesadores,reverse=False)
    elif 'tarjetas de video'in nom:
        tarj_vid.append((vent,nom))
        tarj_vid=sorted(tarj_vid,reverse=False)
    elif 'tarjetas madre' in nom:
        tarj_madre.append((vent,nom))
        tarj_madre=sorted(tarj_madre,reverse=False)
    elif 'discos duros' in nom:
        disc_d.append((vent,nom))
        disc_d=sorted(disc_d,reverse=False)
    elif 'memorias usb' in nom:
        memorias.append((vent,nom))
        memorias=sorted(memorias,reverse=False)
    elif 'pantallas' in nom:
        pantallas.append((vent,nom))
        pantallas=sorted(pantallas,reverse=False)
    elif 'bocinas' in nom:
        bocinas.append((vent,nom))
        bocinas=sorted(bocinas,reverse=False)
    elif 'audifonos' in nom:
        audifonos.append((vent,nom))
        audifonos=sorted(audifonos,reverse=False)


for j in lst_categorias:
    print(f'\nDe la categoría: {j} los 5 productos menos vendidos fueron: ')
    if j == 'procesadores':
        for m in procesadores[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')

    elif j == 'tarjetas de video':
        for m in tarj_vid[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')
    elif j == 'tarjetas madre':
        for m in tarj_madre[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')
    elif j == 'discos duros':
        for m in disc_d[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')
    elif j == 'memorias usb':
        for m in memorias[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')
    elif j == 'pantallas':
        for m in pantallas[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')
    elif j == 'bocinas':
        for m in bocinas[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas')
    elif j == 'audifonos':
        for m in audifonos[:5]:
            datos = m[1]
            ventxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{ventxU}\tunidades vendidas\n')
