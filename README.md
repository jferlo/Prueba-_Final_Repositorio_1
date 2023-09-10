## **Prueba-\_Final\_Repositorio\_1**

**Elaborado por:** Juan Fernando López

**Fecha de elaboración:** 2023/09/09

## **Indicaciones del Repositorio**

Contiene el código relacionado con la extracción de datos, un archivo requirements.txt con  
las dependencias necesarias y los archivos .py

### **Alcance:**

Hoy por hoy el manejo y almacenamiento de los dato es muy important, ya que es el recurso mas importante dentro de cualquier empresa ya sea publica o privada, y es por que en este trabajo, se muestra una alternativa del uso de las herramientas y librerias de Python, para la extracción de datos, su transformation y su almacenamiento.

### **Objetivos:**

*   Poner en practica todos los conocimientos aprendidos a lo largo del desarrollo de la material de Tratamiento de Datos, de la Maestria en Ciberseguridad en la UIDE.
*   Investigar sore tecnicas de webscraping para la extracción de de datos y su posterior transformation y almacenamiento.
*   Elaborar un codigo en python que nos permita obtener la informacion de una api inmobiliaria, para posteriormente ser almacenados en una base de datos alojada en nube.

### **Metodologia**:

#### Software

Para el desarrollo de este proyecto es importante instalar un IDE para poder trabajar con python, en este caso el IDE elegido es PyCharm, ya que tiene una interfaz muy amigable y es de facil manejo. Tambien es necesario instalara las diferentes librerias necesarias para la ejecucion del codigo y dado que se trabajó con tecnicas de webscraping es importante instalar el web driver del navegador que se utiliza.

Para el almacenamiento de los datos obtenidos se ha credo una cuenca en nube de MongoDB .

#### Desarrollo

Con el objetivo de tener un control de versiones del presente proyecto se ha credo un repositorio en GitHub, el cual ha side conectado con Python de monera que conforme se avanza en el proyecto se van documentando los cambios que ha sufrido nuestro trabajo, lo que nos permit tener una trazabilidad de proceso.

Una vez que se triene el repositorio credo y vinculado a python es recomendable un habilitar el entorno virtual de python para este proyecto. ya que nos permitira restringir la visualización de información sencible como links de acceso, usuarios y contraseñas.

En la siguiente imagen se resume el funcionamiento de este codigo, el cual a traves del uso de selenium, google chrome y su web drive, se ingresar a una API inmobiliaria, en la cual se va a realizar una busqueda determinda, con la información obtenida de la busqueda, se extrae la infomacion en texto y se la almacena en una base de datos.

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/7851ed88bb5b9d5e5c5fc75e206483c58af0278e97273574.png)

 **Fig 1.- Diagrama de funcionamiento del codigo**

Para empezar a construir nuestro codigo es importante crear un archivo llamado **“requirements.txt”** ya que aqui vamos a definir cuales son esos paquetes que requerimos de para trabajar dentro de Python, a continuacion se muestra su contenido.

```python
selenium
pymongo
python-dotenv
```

Se crea un archivo **“main.py”**  el cual va a contener el codigo que realizara la extraccion y almacenamiento de la información 

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://www.remax.com.ec/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#searchbar-input")
search_box.send_keys("Pinar Alto")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#button-search")
search_button.click()

house_cards = driver.find_elements(By.CSS_SELECTOR,"#wrapper")
mongodb = MongoDriver()

for card in house_cards:
    titulo= card.find_element(By.CSS_SELECTOR,"div.mat-ripple.info > div > h2").text
    precio= card.find_element(By.CSS_SELECTOR,"#price-expenses").text
    features= card.find_element(By.CSS_SELECTOR,"div.mat-ripple.info > div > div.features").text
    print (titulo)
    print(f'$ {precio}')
    print(features)
    print("----------------------------------------------------")
    inmueble_anuncio= {
        'titulo':titulo,
        'precio':precio,
        'features':features
    }
    mongodb.insert_record(record=inmueble_anuncio, username="Juan Fernando")

driver.close()
```

Tambien se crea un archivo llamado **"db.py"**, el cual nos permite hacer la conexion de python con MongoDB y definir la funcion que nos permite insertar la información en la base de datos.

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()


class MongoDriver:
    def __init__(self):
        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        hostname = os.getenv('MONGO_HOSTNAME')

        uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"


        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection

    def insert_record(self, record: dict, username: str):
        self.client.get_database('db_prueba_final').get_collection(f'{username}_inmuebles').insert_one(record)

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
```

Ya que hemos elaborado el codigo de tal manera que las contraseñas no queden expuestas, se crea un archivo llamado “.env”, el se añade al directorio venv, el cual no se almacena en github.

```python
MONGO_USER=<username>
MONGO_PASSWORD=<password>
MONGO_HOSTNAME=cluster0.xxxxxx.mongodb.net
```

####  **Pruebas de Funcionamiento**

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/e2d0ca8084d7d1aa912bc04bc87733e8e588bf40e4a602f1.png)

 **Fig 2.- Busqueda exitosa** 

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/9e8d0418a662535a0f156b4965b909b6d6d8fccaef4da475.png)

 **Fig 3.- Datos Extraidos de la pagina ingresada**

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/518570e43d0145a84f4d5c42ec07798b287ae749fcd0f759.png)

 **Fig 4.- Datos Almacenados en Mongo DB**

### **Conclusiones , recomendaciones y puntos de mejora:**

#### **Conclusiones**

*   El conocer tecnicas de webscraping nos permite tener la conciencia de que tipo de seguridad se debe incluir al momento de crear un sitio web, de tal manera que la informarmación que se encuentra ahi no se facilmente vulnerada.
*   Es importante fortalecer los conocimientos en el uso y manejo de la herramienta Python, ya que es un lenguaje de programación de facil comprensión y muy potente, el cual se lo puede usar en un sin numero de aplicaciones.
*   El manejo de las tecnicas de ETL de la información, nos permiten adentrarnos en un sin numero de industrias, ya que todas manejan grandes cantidades de información y todas van a requerir tratar dichos recursos y protegerlos.

 **Recomendaciones y puntos a mejorar**

*   Es importante fortalecer las tecnicas de web scraping, ya que en mi caso tuve un incoveniente al momento de ingresar las palabras de busqueda, en el searchbar de al pagina, esta desplegaba, varias opciones, las cuales se convertian en un punto de geolocalización dentro de la pagina. lo que no me permitia avanzar con la busqueda.
*   Es importante elaborar codigos bien estructurados, de tal manera que sirvan como futuras plantillas para proyectos similares.
*   El adecuado uso de GitHub permite tener alamacenados diferentes proyectos con su respectiva documentacion con un nivel de seguridad adecuado.
