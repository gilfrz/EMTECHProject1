from lifestore_file import lifestore_products
from lifestore_file import lifestore_searches

contador2 = dict()
for producto in lifestore_searches:
    busqueda = producto[0]
    producto_id = producto[1]    
    for prod in lifestore_products:
            id_prod = prod[0]
            nombre = prod[1]
            category = prod[3]
            if producto_id == id_prod:
                contador2[(nombre,category)] = contador2.get((nombre,category),0)+1

lst_categorias=[] #lista de categorías
for i in lifestore_products:
    categoria = i[3]
    if categoria not in lst_categorias:
        lst_categorias.append(categoria)
    else:
        continue

procesadores = list()
tarj_vid= list()
tarj_madre= list()
disc_d = list()
memorias= list()
pantallas= list()
bocinas= list()
audifonos= list()


for nom,busq in contador2.items():
    if 'procesadores' in nom:
        procesadores.append((busq,nom))
        procesadores=sorted(procesadores,reverse=False)
    elif 'tarjetas de video'in nom:
        tarj_vid.append((busq,nom))
        tarj_vid=sorted(tarj_vid,reverse=False)
    elif 'tarjetas madre' in nom:
        tarj_madre.append((busq,nom))
        tarj_madre=sorted(tarj_madre,reverse=False)
    elif 'discos duros' in nom:
        disc_d.append((busq,nom))
        disc_d=sorted(disc_d,reverse=False)
    elif 'memorias usb' in nom:
        memorias.append((busq,nom))
        memorias=sorted(memorias,reverse=False)
    elif 'pantallas' in nom:
        pantallas.append((busq,nom))
        pantallas=sorted(pantallas,reverse=False)
    elif 'bocinas' in nom:
        bocinas.append((busq,nom))
        bocinas=sorted(bocinas,reverse=False)
    elif 'audifonos' in nom:
        audifonos.append((busq,nom))
        audifonos=sorted(audifonos,reverse=False)


for j in lst_categorias:
    print(f'\nDe la categoría: {j} los 10 productos menos buscados fueron: ')
    if j == 'procesadores':
        for m in procesadores[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\ncon:{busqxU}\tbúsquedas')

    elif j == 'tarjetas de video':
        for m in tarj_vid[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
    elif j == 'tarjetas madre':
        for m in tarj_madre[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
    elif j == 'discos duros':
        for m in disc_d[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
    elif j == 'memorias usb':
        for m in memorias[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
    elif j == 'pantallas':
        for m in pantallas[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
    elif j == 'bocinas':
        for m in bocinas[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
    elif j == 'audifonos':
        for m in audifonos[:10]:
            datos = m[1]
            busqxU=m[0]
            nomb=datos[0]
            print(f'{nomb}\n con:{busqxU}\tbúsquedas')
