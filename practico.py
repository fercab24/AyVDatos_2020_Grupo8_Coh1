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


