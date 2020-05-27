import matplotlib.pyplot    as plt
import numpy                 
import pandas               
import seaborn              

print ("La version de seaborn es la " +  str(seaborn.__version__) )

#############################################
# Reading the Dataset available from the web
#############################################
full_dataset  = pandas.read_csv('https://object.cato.org/sites/cato.org/files/human-freedom-index-files/human-freedom-index-2019.csv')

print ("El dataset tiene " + str(full_dataset.shape[0]) + " filas")
print ("El dataset tiene " + str(full_dataset.shape[1]) + " columnas")

#########################################################
# Parse the dataset so only the important columns remains
#########################################################
# 1st all the columns related to the personal freedom indentity
identity_cols      =    []
for column in full_dataset:
    if 'pf_identity' in column:
        identity_cols.append(str(column))

# Some other important cols
score_columns      =    identity_cols   +\
                        ['pf_score'     ,
                        'pf_rank'       ,
                        'ef_score'      ,
                        'ef_rank'       ,
                        'hf_score'      ,
                        'hf_rank'       ]

# And cols to be able to classify the data later
classifier_columns =    ['year'         ,
                        'ISO_code'      ,
                        'countries'     , 
                        'region'        ]

columns_to_parse = classifier_columns + score_columns

parsed_dataset = full_dataset[columns_to_parse]
print ("Dataset types before replacing")
print (parsed_dataset.dtypes)

#############################################
# Replace posible blank strings for NaN types
#############################################
parsed_dataset = parsed_dataset.replace('-', numpy.nan)
for column in parsed_dataset:
    if column in score_columns:
        parsed_dataset[str(column)] = pandas.to_numeric(parsed_dataset[str(column)])

print ("Dataset types after replacing nan")
print (parsed_dataset.dtypes)
print ("Ahora el shape es")
print (parsed_dataset.shape)

############################
# Estadisticos Descriptivos 
############################
# 1)    Para comenzar con un pantallazo de los datos, calcular el rango de las variables.

# 2)    Para cada país, tenemos varias realizaciones para cada variable pf_identity y hf_score. 
#       Si queremos comparar un país con otro, ¿cuál es la manera adecuada de hacerlo? Por ejemplo, 
#       ¿nos quedamos con un único valor? ¿o comparamos todos los valores? ¿usamos el promedio? ¿usamos la mediana?

# 3)    Obtener media, mediana y desviación estándar de las variables pf_identity y hf_score en el mundo y compararla con la de Latinoamérica y el caribe. 
#       Usar la respuesta del punto anterior para justificar si la comparación es válida o no.

# 4)    ¿Tiene sentido calcular la moda?

# 5)    ¿Cómo pueden sanearse los valores faltantes?

# 6)    ¿Encuentra outliers en estas dos variables? ¿Qué método utiliza para detectarlos? Los outliers, ¿son globales o por grupo? ¿Los eliminaría del conjunto de datos?


############################
# Agregación de datos
############################
# 1)    Grafiquen la media de la variable pf_identity y hf_score a través de los años.

# 2)    Realicen los mismos gráficos, pero separando por regiones (Cada variable en un gráfico distinto, sino no se ve nada). 
#       ¿La tendencia observada, es la misma que si no dividimos por regiones?

# 3)    Si lo consideran necesario, grafiquen algunos países de Latinoamerica para tratar de explicar la tendencia de la variable pf_identity en la región. 
#       ¿Cómo seleccionarion los países relevantes a esa tendencia?

############################
# Distribuciones
############################
# 1)    Graficar en un mismo histograma la distribución de la variable pf_identity en global, y en Latinoamérica y el caribe. 
#       Repetir para la variable hf_score. 
#       ¿Visualmente, a qué tipo de distribución corresponde cada variable? 
#       ¿Es correcto utilizar todos el conjunto de valores disponibles para esa region en estos gráficos?


############################
# Correlaciones y Relaciones
############################
#       En este ejercicio queremos responder a las preguntas
#       Las libertades personales y económicas, ¿van siempre de la mano?
#       ¿Cómo se relacionan ambas con las libertades respectivas a las relaciones personales?
#       Para ello, analizaremos las correlaciones entre las variables pf_identity, pf_score y ef_score.
#       Como pf_indentity contribuye al cálculo de pf_score esperamos hallar algún grado de correlación. Lo contrario podría ocurrir con ef_score.

# 1)    ¿Qué conclusiones puede sacar de un gráfico pairplot de estas tres variables? ¿Es adecuado para los valores de pf_identity? ¿Por qué?

# 2)    Graficar la correlación (visual) entre pf_identity y pf_score; y entre pf_identity y ef_score. Analizar el resultado, 
#       ¿se pueden sacar conclusiones? Tengan en cuenta que como pf_identity es el resultado de un promedio, sólo toma algunos valores. 
#       Es, en la práctica, discreta, y eso afecta al tipo de gráfico que podemos usar.

# 3)    Convertir estas variables en categóricas, es decir, a partir de pf_indentity generar otra variable pf_identity_segment que tome los valores high, medium y low. 
#       Pueden hacerlo con una función escrita por ustedes, o usando alguna función de pandas como pandas.cut o pandas.dcut. Repetir para ef_score y pf_score. 
#       El criterio para decidir qué intervalos de valores corresponden a cada categoría tienen que decidirlo ustedes, pueden usar los estadísticos mediana y los cuartiles.

# 4)    Graficar la correlación (visual) entre estas tres variables categoricas usando gráficos de calor (heatmaps).
#       Note: van a necesitar 3 gráficos distintos, porque en cada uno podemos incluir sólo 2 variables.





