# -*- coding: utf-8 -*-
"""Delivery3 mineria.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L2J0iuMisSVIQgdu3vh7r3ET73_Drgz9
"""

import pandas as pd

import google.oauth2.service_account as service_account
import pandas_gbq
from google.cloud import bigquery

# Re-load the CSV file to explore its contents
url = 'data.csv'
data = pd.read_csv(url)

# Display the first few rows of the dataset to understand its structure
data.head()

"""#Datos en crudo"""

# Credenciales de la cuenta de servicio
credentials = service_account.Credentials.from_service_account_file('/content/loan-defaulter-d5d15db8dcb8.json') #Este json me lo dan y lo importo

# Parámetros generales
project = 'loan-defaulter' #Me lo dan
dataset = 'loan_defaulter_data' #Me lo dan

# Nombre de la tabla basado en el número de grupo y el ejercicio
table_name = f'data'

# DataFrame que se va a guardar en BigQuery (reemplazar 'df_' con el DataFrame que se quiera guardar)
df_ = data  # Aquí va tu DataFrame generado en el ejercicio

# Guardar en BigQuery
pandas_gbq.to_gbq(df_, f'{dataset}.{table_name}', project_id=project, if_exists='replace', credentials=credentials)

"""Logistic Regresion

#Arreglar las variables categoricas
"""

string_type_variables = ['NAME_CONTRACT_TYPE', 'CODE_GENDER', 'FLAG_OWN_CAR',
       'FLAG_OWN_REALTY','NAME_INCOME_TYPE',
       'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE','ORGANIZATION_TYPE']

for i in string_type_variables:
  print(data[i].unique())

data['CODE_GENDER'] = data['CODE_GENDER'].map({'F': 1, 'M': 0})
data['FLAG_OWN_CAR'] = data['FLAG_OWN_CAR'].map({'Y': 1, 'N': 0})
data['FLAG_OWN_REALTY'] = data['FLAG_OWN_REALTY'].map({'Y': 1, 'N': 0})

df_binarizado = pd.get_dummies(data, columns=['NAME_CONTRACT_TYPE'], drop_first=True)
# Convertir solo las columnas que fueron creadas por get_dummies() a enteros
columnas_binarizadas = df_binarizado.filter(like='NAME_CONTRACT_TYPE_').columns
df_binarizado[columnas_binarizadas] = df_binarizado[columnas_binarizadas].astype(int)
df_binarizado.rename(columns={'NAME_CONTRACT_TYPE_Revolving loans': 'NAME_CONTRACT_TYPE'}, inplace=True)

df_binarizado = pd.get_dummies(df_binarizado, columns=['NAME_INCOME_TYPE'], drop_first=True)
# Convertir solo las columnas que fueron creadas por get_dummies() a enteros
columnas_binarizadas = df_binarizado.filter(like='NAME_INCOME_TYPE').columns
df_binarizado[columnas_binarizadas] = df_binarizado[columnas_binarizadas].astype(int)

df_binarizado = pd.get_dummies(df_binarizado, columns=['NAME_EDUCATION_TYPE'], drop_first=True)
# Convertir solo las columnas que fueron creadas por get_dummies() a enteros
columnas_binarizadas = df_binarizado.filter(like='NAME_EDUCATION_TYPE').columns
df_binarizado[columnas_binarizadas] = df_binarizado[columnas_binarizadas].astype(int)

df_binarizado = pd.get_dummies(df_binarizado, columns=['NAME_FAMILY_STATUS'], drop_first=True)
# Convertir solo las columnas que fueron creadas por get_dummies() a enteros
columnas_binarizadas = df_binarizado.filter(like='NAME_FAMILY_STATUS').columns
df_binarizado[columnas_binarizadas] = df_binarizado[columnas_binarizadas].astype(int)

df_binarizado = pd.get_dummies(df_binarizado, columns=['NAME_HOUSING_TYPE'], drop_first=True)
# Convertir solo las columnas que fueron creadas por get_dummies() a enteros
columnas_binarizadas = df_binarizado.filter(like='NAME_HOUSING_TYPE').columns
df_binarizado[columnas_binarizadas] = df_binarizado[columnas_binarizadas].astype(int)

df_binarizado = pd.get_dummies(df_binarizado, columns=['ORGANIZATION_TYPE'], drop_first=True)
# Convertir solo las columnas que fueron creadas por get_dummies() a enteros
columnas_binarizadas = df_binarizado.filter(like='ORGANIZATION_TYPE').columns
df_binarizado[columnas_binarizadas] = df_binarizado[columnas_binarizadas].astype(int)

df_binarizado

data = df_binarizado

data

"""#Eliminación de nulos"""

data.dropna(inplace=True)

"""#Enviar los datos arreglados"""

data.columns = [col.replace(' ', '') for col in data.columns]
data.columns = [col.replace('/', '') for col in data.columns]

# Credenciales de la cuenta de servicio
credentials = service_account.Credentials.from_service_account_file('/content/loan-defaulter-d5d15db8dcb8.json') #Este json me lo dan y lo importo

# Parámetros generales
project = 'loan-defaulter' #Me lo dan
dataset = 'loan_defaulter_clean' #Me lo dan

# Nombre de la tabla basado en el número de grupo y el ejercicio
table_name = f'data'

# DataFrame que se va a guardar en BigQuery (reemplazar 'df_' con el DataFrame que se quiera guardar)
df_ = data  # Aquí va tu DataFrame generado en el ejercicio

# Guardar en BigQuery
pandas_gbq.to_gbq(df_, f'{dataset}.{table_name}', project_id=project, if_exists='replace', credentials=credentials)

"""#Inputs y output"""

inputs=['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY',
       'CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY',
       'AMT_GOODS_PRICE', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'NAME_CONTRACT_TYPE',
       'NAME_INCOME_TYPE_Pensioner', 'NAME_INCOME_TYPE_Stateservant',
       'NAME_INCOME_TYPE_Student', 'NAME_INCOME_TYPE_Unemployed',
       'NAME_INCOME_TYPE_Working', 'NAME_EDUCATION_TYPE_Highereducation',
       'NAME_EDUCATION_TYPE_Incompletehigher',
       'NAME_EDUCATION_TYPE_Lowersecondary',
       'NAME_EDUCATION_TYPE_Secondaryseco',
       'NAME_EDUCATION_TYPE_Secondarysecondaryspecial',
       'NAME_FAMILY_STATUS_Married', 'NAME_FAMILY_STATUS_Separated',
       'NAME_FAMILY_STATUS_Singlenotmarried', 'NAME_FAMILY_STATUS_Widow',
       'NAME_HOUSING_TYPE_Houseapartment',
       'NAME_HOUSING_TYPE_Municipalapartment',
       'NAME_HOUSING_TYPE_Officeapartment',
       'NAME_HOUSING_TYPE_Rentedapartment', 'NAME_HOUSING_TYPE_Withparents',
       'ORGANIZATION_TYPE_Agriculture', 'ORGANIZATION_TYPE_Bank',
       'ORGANIZATION_TYPE_BusinessEntityType1',
       'ORGANIZATION_TYPE_BusinessEntityType2',
       'ORGANIZATION_TYPE_BusinessEntityType3', 'ORGANIZATION_TYPE_Cleaning',
       'ORGANIZATION_TYPE_Construction', 'ORGANIZATION_TYPE_Culture',
       'ORGANIZATION_TYPE_Electricity', 'ORGANIZATION_TYPE_Emergency',
       'ORGANIZATION_TYPE_Government', 'ORGANIZATION_TYPE_Hotel',
       'ORGANIZATION_TYPE_Housing', 'ORGANIZATION_TYPE_Industry:type1',
       'ORGANIZATION_TYPE_Industry:type10',
       'ORGANIZATION_TYPE_Industry:type11',
       'ORGANIZATION_TYPE_Industry:type12',
       'ORGANIZATION_TYPE_Industry:type13', 'ORGANIZATION_TYPE_Industry:type2',
       'ORGANIZATION_TYPE_Industry:type3', 'ORGANIZATION_TYPE_Industry:type4',
       'ORGANIZATION_TYPE_Industry:type5', 'ORGANIZATION_TYPE_Industry:type6',
       'ORGANIZATION_TYPE_Industry:type7', 'ORGANIZATION_TYPE_Industry:type8',
       'ORGANIZATION_TYPE_Industry:type9', 'ORGANIZATION_TYPE_Insurance',
       'ORGANIZATION_TYPE_Kindergarten', 'ORGANIZATION_TYPE_LegalServices',
       'ORGANIZATION_TYPE_Medicine', 'ORGANIZATION_TYPE_Military',
       'ORGANIZATION_TYPE_Mobile', 'ORGANIZATION_TYPE_Other',
       'ORGANIZATION_TYPE_Police', 'ORGANIZATION_TYPE_Postal',
       'ORGANIZATION_TYPE_Realtor', 'ORGANIZATION_TYPE_Religion',
       'ORGANIZATION_TYPE_Restaurant', 'ORGANIZATION_TYPE_School',
       'ORGANIZATION_TYPE_Security', 'ORGANIZATION_TYPE_SecurityMinistries',
       'ORGANIZATION_TYPE_Self-employed', 'ORGANIZATION_TYPE_Services',
       'ORGANIZATION_TYPE_Telecom', 'ORGANIZATION_TYPE_Trade:type1',
       'ORGANIZATION_TYPE_Trade:type2', 'ORGANIZATION_TYPE_Trade:type3',
       'ORGANIZATION_TYPE_Trade:type4', 'ORGANIZATION_TYPE_Trade:type5',
       'ORGANIZATION_TYPE_Trade:type6', 'ORGANIZATION_TYPE_Trade:type7',
       'ORGANIZATION_TYPE_Transport:type1',
       'ORGANIZATION_TYPE_Transport:type2',
       'ORGANIZATION_TYPE_Transport:type3',
       'ORGANIZATION_TYPE_Transport:type4', 'ORGANIZATION_TYPE_University',
       'ORGANIZATION_TYPE_XNA']
output = ['TARGET']

"""#Regresión logistica con datos desbalanceados"""

import matplotlib.pyplot as plt

data['TARGET'].value_counts().plot.pie(autopct=lambda p: f'{int(p * data.shape[0] / 100)}', startangle=90)
plt.title('Distribución de TARGET')
plt.ylabel('')  # Eliminar la etiqueta del eje y
plt.show()

from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(data, test_size=0.3, random_state=10)

from sklearn.linear_model import LogisticRegression

log_ = LogisticRegression()
log_.fit(df_train[inputs], df_train[output])

log_.score(df_test[inputs], df_test[output])

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

M = confusion_matrix(df_test[output], log_.predict(df_test[inputs]))

sns.heatmap(M, annot=True,)

from sklearn.metrics import confusion_matrix

M = confusion_matrix(df_test[output], log_.predict(df_test[inputs]), normalize='all')

sns.heatmap(M, annot=True,)

from sklearn.metrics import confusion_matrix

M = confusion_matrix(df_test[output], log_.predict(df_test[inputs]), normalize='true')

sns.heatmap(M, annot=True,)

from sklearn.metrics import accuracy_score

accuracy_score(df_test[output], log_.predict(df_test[inputs]))

from sklearn.metrics import precision_score

precision_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0)

from sklearn.metrics import recall_score

recall_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0)

from sklearn.metrics import f1_score

f1_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0)

"""#Balanceo de clases a partir de SMOTE

SMOTE es particularmente efectivo en situaciones donde deseas mejorar la representación de la clase minoritaria sin simplemente replicar ejemplos existentes. Al generar ejemplos sintéticos, SMOTE ayuda a que el modelo generalice mejor y reduzca el riesgo de sobreajuste.
"""

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Dividir el conjunto de datos en entrenamiento y prueba
df_train, df_test = train_test_split(data, test_size=0.3, random_state=10)

# Separar características y variable objetivo para el conjunto de entrenamiento
X_train = df_train.drop('TARGET', axis=1)
y_train = df_train['TARGET']

# Separar características y variable objetivo para el conjunto de prueba
X_test = df_test.drop('TARGET', axis=1)
y_test = df_test['TARGET']

# Aplicar SMOTE solo al conjunto de entrenamiento
smote = SMOTE(random_state=10)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

# Combinar las características y la variable objetivo en un nuevo DataFrame si es necesario
df_train_balanced = pd.DataFrame(X_train_balanced, columns=X_train.columns)
df_train_balanced['TARGET'] = y_train_balanced

df_train_balanced

"""#Enviar los datos balanceados"""

# Credenciales de la cuenta de servicio
credentials = service_account.Credentials.from_service_account_file('/content/loan-defaulter-d5d15db8dcb8.json') #Este json me lo dan y lo importo

# Parámetros generales
project = 'loan-defaulter' #Me lo dan
dataset = 'loan_defaulter_balanced' #Me lo dan

# Nombre de la tabla basado en el número de grupo y el ejercicio
table_name = f'data'

# DataFrame que se va a guardar en BigQuery (reemplazar 'df_' con el DataFrame que se quiera guardar)
df_ = df_train_balanced  # Aquí va tu DataFrame generado en el ejercicio

# Guardar en BigQuery
pandas_gbq.to_gbq(df_, f'{dataset}.{table_name}', project_id=project, if_exists='replace', credentials=credentials)

"""#Modelo de regresión logistica con las clases balanceadas Preliminar"""

import matplotlib.pyplot as plt

df_train_balanced['TARGET'].value_counts().plot.pie(autopct=lambda p: f'{int(p * data.shape[0] / 100)}', startangle=90)
plt.title('Distribución de TARGET')
plt.ylabel('')  # Eliminar la etiqueta del eje y
plt.show()

df_train_balanced['TARGET'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('TARGET Distribution')
plt.ylabel('')  # Eliminar la etiqueta del eje y
plt.show()

from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df_train_balanced, test_size=0.3, random_state=10)

from sklearn.linear_model import LogisticRegression

log_ = LogisticRegression()
log_.fit(df_train[inputs], df_train[output])

log_.score(df_test[inputs], df_test[output])

from sklearn.metrics import confusion_matrix

M = confusion_matrix(df_test[output], log_.predict(df_test[inputs]))

sns.heatmap(M, annot=True,)

from sklearn.metrics import confusion_matrix

M = confusion_matrix(df_test[output], log_.predict(df_test[inputs]), normalize='all')

sns.heatmap(M, annot=True,)

from sklearn.metrics import accuracy_score

accuracy_score(df_test[output], log_.predict(df_test[inputs]))

from sklearn.metrics import precision_score

precision_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0)

from sklearn.metrics import recall_score

recall_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0)

from sklearn.metrics import f1_score

f1_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0)

"""#Validación cruzada"""

scores =[]
accuracies=[]
precisions=[]
recalls=[]
f1s=[]
for i in range(1000):
  df_train, df_test = train_test_split(df_train_balanced, test_size=0.3)
  log_ = LogisticRegression()
  log_.fit(df_train[inputs], df_train[output])
  scores.append(log_.score(df_test[inputs], df_test[output]))
  accuracies.append(accuracy_score(df_test[output], log_.predict(df_test[inputs])))
  precisions.append(precision_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0))
  recalls.append(recall_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0))
  f1s.append(f1_score(df_test[output], log_.predict(df_test[inputs]), pos_label=0))

import matplotlib.pyplot as plt
import seaborn as sns

# Crear una cuadrícula de subgráficas
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

sns.kdeplot(ax=axs[0, 0], x=accuracies, fill=True)
axs[0, 0].set_title('Accuracies')

sns.kdeplot(ax=axs[0, 1], x=precisions, fill=True)
axs[0, 1].set_title('Precisions')

sns.kdeplot(ax=axs[1, 0], x=recalls, fill=True)
axs[1, 0].set_title('Recalls')

sns.kdeplot(ax=axs[1, 1], x=f1s, fill=True)
axs[1, 1].set_title('F1 Scores')


# Ajustar el diseño
plt.tight_layout()
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

# Asumiendo que 'inputs' es la lista de nombres de las variables de entrada
# y 'output' es el nombre de la variable a predecir
X = df_train_balanced[inputs]
y = df_train_balanced[output]

# Dividir en conjunto de entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
model = keras.Sequential([
    layers.Dense(5, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(10, activation='relu'),
    layers.Dense(5, activation='relu'),
    layers.Dense(5, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Ajustar para un problema binario
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_val, y_val))

# Evaluar el modelo
score = model.evaluate(X_val, y_val)
print(f'Score: {score}')