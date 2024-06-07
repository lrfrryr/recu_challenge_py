#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## Challenge
# 
# <P> Generar un programa que lea el contenido del archivo socios.csv y
# muestre por pantalla la siguiente información (puede ser a través de la consola):</P>
# <ul>
#   <li>Cantidad total de personas registradas</li>
#   <li>El promedio de edad de los socios de Racing</li>
#   <Li>Un listado con las 100 primeras personas casadas, con estudios
# Universitarios, ordenadas de menor a mayor según su edad. Por cada persona, mostrar: nombre, edad y equipo</li>
#   <Li>Un listado con los 5 nombres más comunes entre los hinchas de River</li>
#   <Li>Un listado, ordenado de mayor a menor según la cantidad de socios, que enumere, junto con cada equipo, 
#       el promedio de edad de sus socios, la menor edad registrada y la mayor edad registrada</Li>
# </ul>
# <P>Asumo que los datos tienen un socio por línea y no se repiten</P>

# In[2]:


path = './'


# In[3]:


socios = pd.read_csv(path + 'socios.csv', encoding='latin1', sep=';', header=None)


# In[4]:


socios.columns = ['Nombre', 'Edad', 'Equipo','Estado Civil', 'Nivel de Estudios']


# In[5]:


socios.info()


# In[6]:


# 1. Cantidad total de personas registradas

print('Existen {:6d} personas registradas'.format(socios.shape[0]))


# In[7]:


# 2. Promedio de edad de los socios de Racing

print('Los socios de Racing tienen {:5.2f} años en promedio'.      format(socios[socios['Equipo'] == 'Racing']['Edad'].mean()))


# In[8]:


# 3. Listado de las primeras 100 personas casadas, con estudios universitarios, ordenadas crecientemente por edad

socios['Nivel de Estudios'].value_counts()


# In[9]:


socios['Estado Civil'].value_counts()


# In[10]:


socios_filtrados = socios[(socios['Estado Civil']=='Casado') & (socios['Nivel de Estudios'] == 'Universitario')]    [['Nombre','Edad','Equipo']].sort_values(by='Edad').head(100)


# In[11]:


bold_start = "\033[1m"
bold_end = "\033[0m"
print(f'{bold_start}{"Nombre":10s} {"Edad":4s} {"Equipo"}{bold_end}')

for i in range(socios_filtrados.shape[0]):
    print('{:10s} {:4d} {:s}'.format(socios_filtrados.iloc[i,:]['Nombre'], socios_filtrados.iloc[i,:]['Edad'], socios_filtrados.iloc[i,:]['Equipo']))


# In[12]:


# 4. Los 5 nombres mas comunes de hinchas de River
print('Los 5 nombres más comunes hinchas de River son:\n',      list(socios[socios['Equipo'] == 'River']['Nombre'].value_counts().head(5).index))


# In[13]:


# 5. Listado de cantidad de socios por equipo, ordenados decrecientemente

socios_agg = socios.groupby('Equipo').agg({'Equipo':'count','Edad': ['mean','min','max']}).    sort_values(('Equipo','count'), ascending=False)

socios_agg.columns = ['cantidad', 'edad promedio', 'edad mínima', 'edad máxima']
socios_agg['edad promedio'] = socios_agg['edad promedio'].round(2)
print(socios_agg)

