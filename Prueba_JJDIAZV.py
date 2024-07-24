#############################################################################
########                                                             ########
########      PRUEBA ANALISTA DE DATOS ---  FINAGRO.                 ########
########      Código PY. realizado por JHON J DIAZ                   ########
########                                                             ######## 
#############################################################################


############ Análisis de Datos:


## NOTA: Verificar comentario en archivo word, ya que se recibe archivo tipo .xlsb y
##       y el siguiente codigo abre archivos tipo .xlsx.  

## 	a) Cargue las bases de datos de garantías expedidas. 
import pandas as pd

# Ruta de los archivos:
ruta_archivo_a = r'C:\Users\Andres\OneDrive\Escritorio\FINAGRO\Base Año A.xlsx'
ruta_archivo_b = r'C:\Users\Andres\OneDrive\Escritorio\FINAGRO\Base Año B.xlsx'

# cargar los archivos
Año_A = pd.read_excel(ruta_archivo_a)
Año_B = pd.read_excel(ruta_archivo_b)


##   b) Crear variable FECEXP y asignar fecha a cada base:

Año_A['FECEXP'] = 'Año A'
Año_B['FECEXP'] = 'Año B'

# Imprimir los primeros 5 registros de cada base y verificar la creacion de la nueva variable FECEXP
print("Base Año A:")
print(Año_A.head(5))

print("Base Año B:")
print(Año_B.head(5))

##   c) Una las bases de datos de garantías expedidas en una sola 

df_unificada = pd.concat([Año_A, Año_B])

#####   Extra: Realice análisis descriptivo e informativo del archivo de garantias:
print("Análisis descriptivo:")
print(df_unificada.describe())

print("Información de la base de datos:")
print(df_unificada.info())


##   d) Cargue la base de datos de garantías pagadas:

# Ruta del archivo
ruta_archivo_c = r'C:\Users\Andres\OneDrive\Escritorio\FINAGRO\Pagadas.xlsx'
# cargar el archivo
Pagadas = pd.read_excel(ruta_archivo_c)


# Realizar merge con la base de datos unificada
df_merge = pd.merge(df_unificada, Pagadas, on='NROCERT')

##   e) Exporte la base de datos resultante 

ruta_archivo_salida = r'C:\Users\Andres\OneDrive\Escritorio\FINAGRO\Base consolidada de garantías pagadas.xlsx'
df_merge.to_excel(ruta_archivo_salida, index=False)