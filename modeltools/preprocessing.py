# """"""
# # Módulo con helpers para el el preprocesamiento de datos
# """"""
# import numpy as np

# def get_numerical_features(df):
#     return df.select_dtypes(include=[np.number]).columns

# """

# Este módulo contiene helpers para el preprocesamiento de datos

# """

import numpy as np

def get_numerical_features(df):

    return list(df.select_dtypes(include=[np.number]).columns)