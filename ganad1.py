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


driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div[1]/div/button[2]').click()
time.sleep(2)

datclase2 = driver.find_elements_by_xpath("//td[@class='td_precios categoria_precios']")
time.sleep(2)
dataclas2 = []
for dato in datclase2:
    dataclas2.append(dato.text)

dfclas2 = pd.DataFrame(dataclas2)
dfclas2.columns=['Clase']

datprec2 = driver.find_elements_by_xpath("//span[@class='entero_y_coma']")
time.sleep(4)
datprecio2 = []
for dato in datprec2:
    datprecio2.append(dato.text)

dfprecio2 = pd.DataFrame(datprecio2)

n = dfprecio2.index
par = n % 2 == 0
impar = n % 2 != 0

# precioanter2 = []

# for n in dfprecio2:
#     precioant2 = dfprecio2.iloc[impar]
#     precioanter2.append(precioant2)
# precioanterior2 = pd.DataFrame(np.row_stack(precioanter2))
# precioanterior2.columns = ['Precio_anterior']
# precioanterior2

precionuev2 = []
for n in dfprecio2:
    precionu2 = dfprecio2.iloc[par]
    precionuev2.append(precionu2)
precionuevo2 = pd.DataFrame(np.row_stack(precionuev2))
precionuevo2.columns = ['Precio_nuevo']
precionuevo2

datcan12 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios']")
time.sleep(2)
datcant12 = []
for dato in datcan12:
    datcant12.append(dato.text)

cantidadnu2 = pd.DataFrame(datcant12)
cantidadnu2.columns=['Cantidad_nueva']
cantidadnu2

# datcan222 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios_2columna']")
# time.sleep(2)
# datcant222 = []
# for dato in datcan222:
#     datcant222.append(dato.text)

# cantidadan2 = pd.DataFrame(datcant222)
# cantidadan2.columns=['Cantidad_anterior']
# cantidadan2
time.sleep(3)
driver.quit()

arch1 = pd.read_excel('faena-datosdecampoacampo.xlsx')
# arch1['Precio_prom_sem'] = arch1['Precio_prom_sem'].squeeze()
# arch1['Precio_prom_sem'] = arch1['Precio_prom_sem'].map(lambda x: str(x).replace(',','.')).astype(float)
# arch1['Cantidad_acum_sem'] = arch1['Cantidad_acum_sem'].astype(float)
# arch1

datosss = dfclas2.merge(precionuevo2,right_index=True,left_index=True)
datosss = datosss.merge(cantidadnu2,right_index=True,left_index=True)
datosss

# fecha_inicio = datetime.today() - timedelta(days=8)
# fecha_inicio = str(fecha_inicio.strftime('%d/%m/%Y'))
# fecha_inicio
fecha_nueva = datetime.today()
fecha_nueva = str(fecha_nueva.strftime('%d/%m/%Y'))

datosss['Fecha'] = fecha_nueva
datosss = datosss.reindex(columns=['Fecha','Clase','Precio_nuevo','Cantidad_nueva'])
datosss = datosss.rename(columns={'Precio_nuevo':'Precio_prom_sem','Cantidad_nueva':'Cantidad_acum_sem'})
datosss

datosss['Precio_prom_sem'] = datosss['Precio_prom_sem'].squeeze()
datosss['Precio_prom_sem'] = datosss['Precio_prom_sem'].map(lambda x: str(x).replace(',','.')).astype(float)
datosss['Cantidad_acum_sem'] = datosss['Cantidad_acum_sem'].astype(float)
datosss

datoss2 = pd.concat([arch1,datosss])
datoss2

datoss2.to_excel('faena-datosdecampoacampo.xlsx',sheet_name='Faena',index=False)


