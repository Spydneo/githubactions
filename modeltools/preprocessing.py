"""
Este módulo contiene helpers para el preprocesamiento de datos
"""
import numpy as np

def get_numerical_features(df):
    """get_numerical features devuelve una lista
    con el nombre de las columnas que contienen datos
    de tipo numérico
    
    :df: dataframe
    :type: pandas.DataFrame
    :return: Una lista con los nombre de las columnas numericas del dataframe
    
    Ejemplos
    ========
    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a":[1]})
    >>> get_numerical_features(df)
    ['a']
    """
    return list(df.select_dtypes(include=[np.number]).columns)


def test_funtion_to_autoapi_rtd(x, y):
    """
    Prueba de documentación con autoapi

    :x: primer número
    :type: int
    :y: segudo número
    :type: int
    :return: La suma de un valor entero
    """
    return x+y