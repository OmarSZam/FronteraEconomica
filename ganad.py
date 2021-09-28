from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
import datetime
from datetime import datetime, timedelta
import pandas as pd
from selenium.webdriver.support.ui import Select
import numpy as np

driver = webdriver.Chrome(executable_path=r"E:/Omar/FRONTERA/proyecto python/WebScraping/ChromeDriver/chromedriver.exe")
driver.get("https://www.decampoacampo.com/__dcac/")
time.sleep(3)

mail = 'omarszampaca@gmail.com'
contraseña = '15_Chapu'


driver.find_element_by_id("btn_login").click()
time.sleep(0.25)
driver.find_element_by_id("maillog").send_keys(mail)
time.sleep(0.25)
driver.find_element_by_id("password").send_keys(contraseña)
time.sleep(0.25)
driver.find_element_by_id("ingresar_login").click()
time.sleep(3)
driver.find_element_by_link_text('Ver más').click()
time.sleep(0.25)
datclase = driver.find_elements_by_xpath("//td[@class='td_precios categoria_precios']")
time.sleep(2)
dataclas = []
for dato in datclase:
    dataclas.append(dato.text)

dfclas = pd.DataFrame(dataclas)
dfclas.columns=['Clase']
dfclas
datprec = driver.find_elements_by_xpath("//span[@class='entero_y_coma']")
time.sleep(4)
datprecio = []
for dato in datprec:
    datprecio.append(dato.text)

dfprecio = pd.DataFrame(datprecio)

n = dfprecio.index
par = n % 2 == 0
impar = n % 2 != 0

# precioanter = []

# for n in dfprecio:
#     precioant = dfprecio.iloc[impar]
#     precioanter.append(precioant)
# precioanterior = pd.DataFrame(np.row_stack(precioanter))
# precioanterior.columns = ['Precio_anterior']
# precioanterior

precionuev = []
for n in dfprecio:
    precionu = dfprecio.iloc[par]
    precionuev.append(precionu)
precionuevo = pd.DataFrame(np.row_stack(precionuev))
precionuevo.columns = ['Precio_nuevo']
precionuevo
datcan1 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios']")
time.sleep(2)
datcant1 = []

for dato in datcan1:
    datcant1.append(dato.text)

cantidadnu = pd.DataFrame(datcant1)
cantidadnu.columns=['Cantidad_nueva']
cantidadnu

# datcan2 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios_2columna']")
# time.sleep(3)
# datcant2 = []
# for dato in datcan2:
#     datcant2.append(dato.text)

# cantidadan = pd.DataFrame(datcant2)
# cantidadan.columns=['Cantidad_anterior']
# cantidadan

driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div[2]/div[1]/form/div[1]/button[2]').click()
time.sleep(2)
datclase1 = driver.find_elements_by_xpath("//td[@class='td_precios categoria_precios']")
time.sleep(2)

dataclas1 = []
for dato in datclase1:
    dataclas1.append(dato.text)

dfclas1 = pd.DataFrame(dataclas1)
dfclas1.columns=['Clase']

datprec1 = driver.find_elements_by_xpath("//span[@class='entero_y_coma']")
time.sleep(4)
datprecio1 = []
for dato in datprec1:
    datprecio1.append(dato.text)

dfprecio1 = pd.DataFrame(datprecio1)

# precioanter1 = []

# for n in dfprecio1:
#     precioant1 = dfprecio1.iloc[impar]
#     precioanter1.append(precioant1)
# precioanterior1 = pd.DataFrame(np.row_stack(precioanter1))
# precioanterior1.columns = ['Precio_anterior']
# precioanterior1

precionuev1 = []
for n in dfprecio1:
    precionu1 = dfprecio1.iloc[par]
    precionuev1.append(precionu1)
precionuevo1 = pd.DataFrame(np.row_stack(precionuev1))
precionuevo1.columns = ['Precio_nuevo']
precionuevo1

datcan11 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios']")
time.sleep(2)
datcant11 = []
for dato in datcan11:
    datcant11.append(dato.text)

cantidadnu1 = pd.DataFrame(datcant11)
cantidadnu1.columns=['Cantidad_nueva']
cantidadnu1

# datcan22 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios_2columna']")
# time.sleep(2)
# datcant22 = []
# for dato in datcan22:
#     datcant22.append(dato.text)

# cantidadan1 = pd.DataFrame(datcant22)
# cantidadan1.columns=['Cantidad_anterior']
# cantidadan1

time.sleep(3)
driver.quit()

arch = pd.read_excel('E:\Omar\FRONTERA\proyecto python\WebScraping\invernada-datosdecampoacampo.xlsx')
# arch = arch.apply(lambda x: x.str.replace(',','.'))
# arch

datos = dfclas.merge(precionuevo,right_index=True,left_index=True)
datos = datos.merge(cantidadnu1,right_index=True,left_index=True)
datos

datoss = dfclas1.merge(precionuevo1,right_index=True,left_index=True)
datoss = datoss.merge(cantidadnu1,right_index=True,left_index=True)
datoss

# fecha_inicio = datetime.today() - timedelta(days=8)
# fecha_inicio = str(fecha_inicio.strftime('%d/%m/%Y'))
# fecha_inicio
fecha_nueva = datetime.today()
fecha_nueva = str(fecha_nueva.strftime('%d/%m/%Y'))

datos['Sexo'] = 'Machos'
datoss['Sexo'] = 'Hembras'
datos['Fecha'] = fecha_nueva
datos
datoss['Fecha'] = fecha_nueva
datos = datos.reindex(columns=['Fecha','Clase','Sexo','Precio_nuevo','Cantidad_nueva'])
datoss = datoss.reindex(columns=['Fecha','Clase','Sexo','Precio_nuevo','Cantidad_nueva'])
datos = datos.rename(columns={'Precio_nuevo':'Precio_prom_sem','Cantidad_nueva':'Cantidad_acum_sem'})
datoss = datoss.rename(columns={'Precio_nuevo':'Precio_prom_sem','Cantidad_nueva':'Cantidad_acum_sem'})

datoss1 = pd.concat([datos,datoss])
datoss1 = datoss1.apply(lambda x: x.str.replace(',','.'))
datoss1


datos2 = pd.concat([arch,datoss1])
datos2 = datos2.replace('-',0)
datos2['Precio_prom_sem'] = datos2['Precio_prom_sem'].astype(float)
datos2['Cantidad_acum_sem'] = datos2['Cantidad_acum_sem'].astype(float)
datos2

datos2.to_excel('invernada-datosdecampoacampo.xlsx',sheet_name='Invernada',index=False)

