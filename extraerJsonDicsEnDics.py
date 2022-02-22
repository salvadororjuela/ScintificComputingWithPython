import urllib.request, urllib.parse, urllib.error, json, ssl
# Libreria para tabular los resultados
from tabulate import tabulate

# ignorar errores de certificados SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

# Abre el json de la pagina web
input = "https://agentechatdevmgt.smartsoft.com.co:3000/"
# Abre el json desde un archivo
postman = open("endpointsList.json")

# retorna un string con el contenido del json
url = urllib.request.urlopen(input, context=ctx).read().decode()

# cargar el json de la url y del archivo
js = json.loads(url)
file = json.load(postman)

# Obtener los values de los path
paths = js.get("modules")

cuentaRutas = 0
# lista de listas para guardar cada controlador/endpoint y método
pathMethod = list()
# Lista de listas para guardar los datos de el documento file
postmanData = list()

# itera sobre paths para sacar los objetos routes y los objetos path
for p in range(len(paths)):
    # almacena el objeto routes de cada diccionario 
    ruta = paths[p]["routes"]
    # almacena el objeto path 
    moduloPath = paths[p]["path"]
    # itera sobre cada variable ruta y obtiene el path interno y el metodo de cada uno
    for camino in range(len(ruta)):
        caminos = ruta[camino]["path"]
        metodo = ruta[camino]["method"]
        # Se almacenan el controlador, el path y el metodo para cada endpoint
        pathMethod.append([moduloPath, caminos, metodo])
        cuentaRutas += 1

# loop para extraer cada una de las listas del archivo file y ponerlas en una nueva variable de listas
for list in file:
    postmanData.append(list)
    
pathMethod.sort()
postmanData.sort()

# imprime tabla con el contenido de pathMethod, le coloca headers y pone formato de tabla
table = tabulate(pathMethod, headers=["Controlador", "Endpoint", "Método"], tablefmt="orgtbl")
print(table)
print("---------------------------------------------------------------------------------------------")
print(f"Total Endpoints: {cuentaRutas}")
print("#############################################################################################\n\n")

# Imprime la tabla creada con los mismos datos anteriores, pero del archivo cargado
tablepostman = tabulate(postmanData, headers=["Controlador", "Endpoint", "Método"], tablefmt="orgtbl")
print(tablepostman)
print("---------------------------------------------------------------------------------------------")
print(f"Total Endpoints: {len(postmanData)}")
print("#############################################################################################\n\n")