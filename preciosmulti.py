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
driver.get("https://multiexpressonline.com/index.php")
time.sleep(3)

mail = 'omarszampaca@gmail.com'
contraseña = '15_Chapu'

driver.find_element_by_id("user_name").send_keys(mail)
time.sleep(0.25)
driver.find_element_by_id("user_password").send_keys(contraseña)
time.sleep(0.25)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div[1]/form/button").click()
time.sleep(1)
driver.find_element_by_link_text('Almacen').click()
time.sleep(0.5)
descrip = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc = []
for dato in descrip:
    desc.append(dato.text)
desc
desc = [line.split("\n") for line in desc]
desc

dfdesc = pd.DataFrame(desc)
dfdesc = dfdesc.drop(columns=2)
dfdesc.columns = ['Producto','Precio']
dfdesc['Sector'] = 'Almacen'

fecha = datetime.today()
fecha = str(fecha.strftime('%d/%m/%Y'))

dfdesc['Fecha'] = fecha
dfdesc = dfdesc.reindex(columns=['Fecha','Sector','Producto','Precio'])



driver.find_element_by_link_text('Carnes/Aves').click()
time.sleep(0.5)
descrip1 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc1 = []
for dato in descrip1:
    desc1.append(dato.text)
desc1
desc1 = [line.split("\n") for line in desc1]
desc1

dfdesc1 = pd.DataFrame(desc1)
dfdesc1 = dfdesc1.drop(columns=2)
dfdesc1.columns = ['Producto','Precio']
dfdesc1['Sector'] = 'Carnes/Aves'

dfdesc1['Fecha'] = fecha
dfdesc1 = dfdesc1.reindex(columns=['Fecha','Sector','Producto','Precio'])



driver.find_element_by_link_text('Verdulería').click()
time.sleep(0.5)
descrip2 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc2 = []
for dato in descrip2:
    desc2.append(dato.text)
desc2
desc2 = [line.split("\n") for line in desc2]
desc2

dfdesc2 = pd.DataFrame(desc2)
dfdesc2 = dfdesc2.drop(columns=2)
dfdesc2.columns = ['Producto','Precio']
dfdesc2['Sector'] = 'Verdulería'

dfdesc2['Fecha'] = fecha
dfdesc2 = dfdesc2.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_link_text('Bazar y Hogar').click()
time.sleep(0.5)
descrip3 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc3 = []
for dato in descrip3:
    desc3.append(dato.text)
desc3
desc3 = [line.split("\n") for line in desc3]
desc3

dfdesc3 = pd.DataFrame(desc3)
dfdesc3 = dfdesc3.drop(columns=2)
dfdesc3.columns = ['Producto','Precio']
dfdesc3['Sector'] = 'Bazar y Hogar'

dfdesc3['Fecha'] = fecha
dfdesc3 = dfdesc3.reindex(columns=['Fecha','Sector','Producto','Precio'])

 
driver.find_element_by_link_text('Bebidas').click()
time.sleep(0.5)
descrip4 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc4 = []
for dato in descrip4:
    desc4.append(dato.text)
desc4
desc4 = [line.split("\n") for line in desc4]
desc4

dfdesc4 = pd.DataFrame(desc4)
dfdesc4 = dfdesc4.drop(columns=2)
dfdesc4.columns = ['Producto','Precio']
dfdesc4['Sector'] = 'Bebidas'

dfdesc4['Fecha'] = fecha
dfdesc4 = dfdesc4.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_link_text('Congelados').click()
time.sleep(0.5)
descrip5 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc5 = []
for dato in descrip5:
    desc5.append(dato.text)
desc5
desc5 = [line.split("\n") for line in desc5]
desc5

dfdesc5 = pd.DataFrame(desc5)
dfdesc5 = dfdesc5.drop(columns=2)
dfdesc5.columns = ['Producto','Precio']
dfdesc5['Sector'] = 'Congelados'

dfdesc5['Fecha'] = fecha
dfdesc5 = dfdesc5.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_link_text('Sin Tacc').click()
time.sleep(0.5)
descrip5 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc5 = []
for dato in descrip5:
    desc5.append(dato.text)
desc5
desc5 = [line.split("\n") for line in desc5]
desc5

dfdesc5 = pd.DataFrame(desc5)
dfdesc5 = dfdesc5.drop(columns=2)
dfdesc5.columns = ['Producto','Precio']
dfdesc5['Sector'] = 'Sin Tacc'

dfdesc5['Fecha'] = fecha
dfdesc5 = dfdesc5.reindex(columns=['Fecha','Sector','Producto','Precio'])
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Galletas y Golosinas').click()
time.sleep(0.5)
descrip6 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc6 = []
for dato in descrip6:
    desc6.append(dato.text)
desc6 = [line.split("\n") for line in desc6]
desc6

dfdesc6 = pd.DataFrame(desc6)
dfdesc6 = dfdesc6.drop(columns=2)
dfdesc6.columns = ['Producto','Precio']
dfdesc6['Sector'] = 'Galletas y Golosinas'

dfdesc6['Fecha'] = fecha
dfdesc6 = dfdesc6.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Lácteos').click()
time.sleep(0.5)
descrip7 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc7 = []
for dato in descrip7:
    desc7.append(dato.text)
desc7 = [line.split("\n") for line in desc7]
desc7

dfdesc7 = pd.DataFrame(desc7)
dfdesc7 = dfdesc7.drop(columns=2)
dfdesc7.columns = ['Producto','Precio']
dfdesc7['Sector'] = 'Lácteos'

dfdesc7['Fecha'] = fecha
dfdesc7 = dfdesc7.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Mascotas').click()
time.sleep(0.5)
descrip8 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc8 = []
for dato in descrip8:
    desc8.append(dato.text)
desc8 = [line.split("\n") for line in desc8]
desc8

dfdesc8 = pd.DataFrame(desc8)
dfdesc8 = dfdesc8.drop(columns=2)
dfdesc8.columns = ['Producto','Precio']
dfdesc8['Sector'] = 'Mascotas'

dfdesc8['Fecha'] = fecha
dfdesc8 = dfdesc8.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Gaseosas').click()
time.sleep(0.5)
descrip9 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc9 = []
for dato in descrip9:
    desc9.append(dato.text)
desc9 = [line.split("\n") for line in desc9]
desc9

dfdesc9 = pd.DataFrame(desc9)
dfdesc9 = dfdesc9.drop(columns=2)
dfdesc9.columns = ['Producto','Precio']
dfdesc9['Sector'] = 'Gaseosas'

dfdesc9['Fecha'] = fecha
dfdesc9 = dfdesc9.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Limpieza').click()
time.sleep(0.5)
descrip10 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc10 = []
for dato in descrip10:
    desc10.append(dato.text)
desc10 = [line.split("\n") for line in desc10]
desc10

dfdesc10 = pd.DataFrame(desc10)
dfdesc10 = dfdesc10.drop(columns=2)
dfdesc10.columns = ['Producto','Precio']
dfdesc10['Sector'] = 'Limpieza'

dfdesc10['Fecha'] = fecha
dfdesc10 = dfdesc10.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Lavandería').click()
time.sleep(0.5)
descrip11 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc11 = []
for dato in descrip11:
    desc11.append(dato.text)
desc11 = [line.split("\n") for line in desc11]
desc11

dfdesc11 = pd.DataFrame(desc11)
dfdesc11 = dfdesc11.drop(columns=2)
dfdesc11.columns = ['Producto','Precio']
dfdesc11['Sector'] = 'Lavandería'

dfdesc11['Fecha'] = fecha
dfdesc11 = dfdesc11.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Mama y Bebe').click()
time.sleep(0.5)
descrip12 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc12 = []
for dato in descrip12:
    desc12.append(dato.text)
desc12 = [line.split("\n") for line in desc12]
desc12

dfdesc12 = pd.DataFrame(desc12)
dfdesc12 = dfdesc12.drop(columns=2)
dfdesc12.columns = ['Producto','Precio']
dfdesc12['Sector'] = 'Mama y Bebe'

dfdesc12['Fecha'] = fecha
dfdesc12 = dfdesc12.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Quesos y Dulces').click()
time.sleep(0.5)
descrip13 = driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc13 = []
for dato in descrip13:
    desc13.append(dato.text)
desc13 = [line.split("\n") for line in desc13]
desc13

dfdesc13 = pd.DataFrame(desc13)
dfdesc13 = dfdesc13.drop(columns=2)
dfdesc13.columns = ['Producto','Precio']
dfdesc13['Sector'] = 'Quesos y Dulces'

dfdesc13['Fecha'] = fecha
dfdesc13 = dfdesc13.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Vinos').click()
time.sleep(0.5)
descrip14= driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc14 = []
for dato in descrip14:
    desc14.append(dato.text)
desc14 = [line.split("\n") for line in desc14]
desc14

dfdesc14 = pd.DataFrame(desc14)
dfdesc14 = dfdesc14.drop(columns=2)
dfdesc14.columns = ['Producto','Precio']
dfdesc14['Sector'] = 'Vinos'

dfdesc14['Fecha'] = fecha
dfdesc14 = dfdesc14.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Panadería y Pastas').click()
time.sleep(0.5)
descrip15= driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc15 = []
for dato in descrip15:
    desc15.append(dato.text)
desc15 = [line.split("\n") for line in desc15]
desc15

dfdesc15 = pd.DataFrame(desc15)
dfdesc15 = dfdesc15.drop(columns=2)
dfdesc15.columns = ['Producto','Precio']
dfdesc15['Sector'] = 'Panadería y Pastas'

dfdesc15['Fecha'] = fecha
dfdesc15 = dfdesc15.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Higiene').click()
time.sleep(0.5)
descrip16= driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc16 = []
for dato in descrip16:
    desc16.append(dato.text)
desc16 = [line.split("\n") for line in desc16]
desc16

dfdesc16 = pd.DataFrame(desc16)
dfdesc16 = dfdesc16.drop(columns=2)
dfdesc16.columns = ['Producto','Precio']
dfdesc16['Sector'] = 'Higiene'

dfdesc16['Fecha'] = fecha
dfdesc16 = dfdesc16.reindex(columns=['Fecha','Sector','Producto','Precio'])


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]/span[1]").click()
time.sleep(2)

driver.find_element_by_link_text('Fiambres').click()
time.sleep(0.5)
descrip17= driver.find_elements_by_class_name('boxPrd')
time.sleep(0.5)
desc17 = []
for dato in descrip17:
    desc17.append(dato.text)
desc17 = [line.split("\n") for line in desc17]
desc17

dfdesc17 = pd.DataFrame(desc17)
dfdesc17 = dfdesc17.drop(columns=2)
dfdesc17.columns = ['Producto','Precio']
dfdesc17['Sector'] = 'Fiambres'

dfdesc17['Fecha'] = fecha
dfdesc17 = dfdesc17.reindex(columns=['Fecha','Sector','Producto','Precio'])

driver.quit()

df = pd.concat([dfdesc,dfdesc1,dfdesc2,dfdesc3,dfdesc4,dfdesc5,
                dfdesc6,dfdesc7,dfdesc8,dfdesc9,dfdesc10,
                dfdesc11,dfdesc12,dfdesc13,dfdesc14,dfdesc15,
                dfdesc16,dfdesc17])

df1 = pd.read_excel('E:\Omar\FRONTERA\proyecto python\WebScraping\preciosmulti.xlsx')
df1

df['Precio'] = df['Precio'].squeeze()
df['Precio'] = df['Precio'].map(lambda x: str(x).lstrip('$').rstrip('$')).astype(float)

df2 = pd.concat([df1,df])
df2

df2.to_excel('preciosmulti.xlsx',index=False)