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
for column in parsed_dataset:
    if str(column) in classifier_columns:
        print ('La variable ' + str(column) + ' puede tomar los siguentes valores')
        print ( parsed_dataset[str(column)].unique() )
    else:
        print ('Para la variable ' + str(column) + ' el min es = ' + str(parsed_dataset[str(column)].min()) + ' el max es = ' + str(parsed_dataset[str(column)].max()))
    print('')


# 2)    Para cada país, tenemos varias realizaciones para cada variable pf_identity y hf_score. 
#       Si queremos comparar un país con otro, ¿cuál es la manera adecuada de hacerlo? Por ejemplo, 
#       ¿nos quedamos con un único valor? ¿o comparamos todos los valores? ¿usamos el promedio? ¿usamos la mediana?

#  Aca tenemos dos o tres aproximaciones,
#  Opcion A)    Es tomar el promedio de las promedio de las variables de un pais a lo largo de los anios, y compararlo con el promedio del otro
#               pais que se quiere comparar. El problema de esto, es que que con el promedio con valores transformados a 0, tira el promedio muy para abajo
#               la otra es que no marca la tendencia de un pais con respecto a otro, uno puede tener un promedio mas alto, pero ir en tendencia negativa,
#               mientras que puede ser lo contrario para el otro pais. Con este criterio el que tenga mayor promedio se consideraria mejor

#  Opcion B)    Es comparar los valores de las variables periodo por periodo, esto te marca la tendencia de los paises
#               Se consideraria mejor aquel que marque una tendencia positiva, esto es claro en los casos donde tiene tendencias opuestas
#               Pero si ambos tienen tendias positivas por ejemplo, te tomaria aquel que lo haga con mayor rapidez.
#               O en el caso de las pendientes negativas aquel que decrezca con mayor lentitud

#  Opcion C)    Usar una combinacion de A y B, es decir se consideraria mejor aquel pais que con un promedio mayor y una tendencia positiva.
#               En el caso de que el pais con mayor promedio demuestre un tendencia negativa, y el de menor una positiva, se tiene que evaluar
#               Si la tendencia es lo suficiente, para que con un menor promedio se lo pueda considerar mejor
#               Cada caso de comparacion es particular, y se tendria que examinar desde varios puntos de vista (como opcion a y b) para definirlo.
 
# 3)    Obtener media, mediana y desviación estándar de las variables pf_identity y hf_score en el mundo y compararla con la de Latinoamérica y el caribe. 
#       Usar la respuesta del punto anterior para justificar si la comparación es válida o no.
selected_region               = parsed_dataset[parsed_dataset.region == 'Latin America & the Caribbean']

mean_pf_indentity_latam      = selected_region.pf_identity.mean()
median_pf_indentity_latam    = selected_region.pf_identity.median()
std_dev_pf_indentity_latam   = selected_region.pf_identity.std()

mean_hf_score_latam          = selected_region.hf_score.mean()
median_hf_score_latam        = selected_region.hf_score.median()
std_dev_hf_score_latam       = selected_region.hf_score.std()

selected_region              = parsed_dataset[parsed_dataset.region != 'Latin America & the Caribbean']

mean_pf_indentity_world      = selected_region.pf_identity.mean()
median_pf_indentity_world    = selected_region.pf_identity.median()
std_dev_pf_indentity_world   = selected_region.pf_identity.std()

mean_hf_score_world          = selected_region.hf_score.mean()
median_hf_score_world        = selected_region.hf_score.median()
std_dev_hf_score_world       = selected_region.hf_score.std()

print ('mean_pf_indentity_latam    = ' + str(mean_pf_indentity_latam    ) )
print ('median_pf_indentity_latam  = ' + str(median_pf_indentity_latam  ) )
print ('std_dev_pf_indentity_latam = ' + str(std_dev_pf_indentity_latam ) )
print ('mean_hf_score_latam        = ' + str(mean_hf_score_latam        ) )
print ('median_hf_score_latam      = ' + str(median_hf_score_latam      ) )
print ('std_dev_hf_score_latam     = ' + str(std_dev_hf_score_latam     ) )
print ('mean_pf_indentity_world    = ' + str(mean_pf_indentity_world    ) )
print ('median_pf_indentity_world  = ' + str(median_pf_indentity_world  ) )
print ('std_dev_pf_indentity_world = ' + str(std_dev_pf_indentity_world ) )
print ('mean_hf_score_world        = ' + str(mean_hf_score_world        ) )
print ('median_hf_score_world      = ' + str(median_hf_score_world      ) )
print ('std_dev_hf_score_world     = ' + str(std_dev_hf_score_world     ) )

# 4)    ¿Tiene sentido calcular la moda?
#       No tiene sentido calcular la moda, ya que se trata del valor mas repitido, el analisis de rango de las variables, revelo que tenemos numeros enteros
#       entre 0  y 10, y hasta 2 cifras de decimal, es altamente improbable que emerja un patron de valor repetido. 

# 5)    ¿Cómo pueden sanearse los valores faltantes?
#       Se podria calcular una taza de crecimiento de la variable y aplicar una extrapolacion a los periodos faltantas

# 6)    ¿Encuentra outliers en estas dos variables? ¿Qué método utiliza para detectarlos? Los outliers, ¿son globales o por grupo? ¿Los eliminaría del conjunto de datos?
#       Los datos atipos se toman, en base entre 2 o 3 desviaciones standares, todos los valores de que caen fuera de esa rango los consideramos valores atipicos
#       No se eliminarian del conjunto de datos, por que siguen siendo valores que represantan la realidad de un pais y se lo estaria excluyendo del analisis

# //[FIXME] Esto es con las 2 regiones o por cada grupo..
selected_region            = parsed_dataset[parsed_dataset.region == 'Latin America & the Caribbean']
outliers_pf_identity_latam = selected_region[abs(selected_region.pf_identity - mean_pf_indentity_latam) >= (2 * std_dev_pf_indentity_latam)]
outliers_hf_score_latam    = selected_region[abs(selected_region.hf_score - mean_hf_score_latam) >= (2 * std_dev_hf_score_latam)]

selected_region            = parsed_dataset[parsed_dataset.region != 'Latin America & the Caribbean']
outliers_pf_identity_world = selected_region[abs(selected_region.pf_identity - mean_pf_indentity_latam) >= (2 * std_dev_pf_indentity_latam)]
outliers_hf_score_world    = selected_region[abs(selected_region.hf_score - mean_hf_score_latam) >= (2 * std_dev_hf_score_latam)]

############################
# Agregación de datos
############################
# 1)    Grafiquen la media de la variable pf_identity y hf_score a través de los años.
plt.figure()
plt.title("Mean world value pf_indentity across the years")
seaborn.barplot(data=parsed_dataset, x='year', y='pf_identity')
plt.figure()
plt.title("Mean world value hf_score across the years")
seaborn.barplot(data=parsed_dataset, x='year', y='hf_score')
plt.show()

# 2)    Realicen los mismos gráficos, pero separando por regiones (Cada variable en un gráfico distinto, sino no se ve nada). 
#       ¿La tendencia observada, es la misma que si no dividimos por regiones?
for region in parsed_dataset.region.unique():
# for region in 'Latin America & the Caribbean':
    sub_parsed_dataset = parsed_dataset[parsed_dataset.region == region]
    plt.figure()
    plt.title("Mean "+ region + " value pf_identity across the years")
    seaborn.barplot(data=sub_parsed_dataset, x='year', y='pf_identity')
    plt.figure()
    plt.title("Mean "+ region + " value hf_score across the years")
    seaborn.barplot(data=sub_parsed_dataset, x='year', y='hf_score')

plt.show()


# 3)    Si lo consideran necesario, grafiquen algunos países de Latinoamerica para tratar de explicar la tendencia de la variable pf_identity en la región. 
#       ¿Cómo seleccionarion los países relevantes a esa tendencia?
#       - Se podrian alugnos de arriba en el ranking y otros de mas abajo ?

############################
# Distribuciones
############################
# 1)    Graficar en un mismo histograma la distribución de la variable pf_identity en global, y en Latinoamérica y el caribe. 
#       Repetir para la variable hf_score. 
#       ¿Visualmente, a qué tipo de distribución corresponde cada variable? 
#       ¿Es correcto utilizar todos el conjunto de valores disponibles para esa region en estos gráficos?
latam  = parsed_dataset[parsed_dataset.region == 'Latin America & the Caribbean']
world  = parsed_dataset[parsed_dataset.region != 'Latin America & the Caribbean']
plt.figure()
plt.title("pf_identity in latam and world")
seaborn.distplot(latam.pf_identity.dropna())
seaborn.distplot(world.pf_identity.dropna())

plt.figure()
plt.title("hf_score in latam and world")
seaborn.distplot(latam.hf_score.dropna())
seaborn.distplot(world.hf_score.dropna())

plt.show()

# Ni idea que distribucion tienen
# Habir que sacar los valores atipicos o los que son NaN ?

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





