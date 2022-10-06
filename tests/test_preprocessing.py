import pandas as pd
from modeltools.preprocessing import get_numerical_features

def test_get_numerical_features_simple():
    """
    Se va a probar que logra distinguir entre cadenas de texto y números enteros
    assert es “como un if” pero que falla si la condicion
    es falsa. Esto es ideal para los tests.
    """
    df = pd.DataFrame({
    "numerica": [5],
    "categorica": ["rojo"]
    })
    print("Valor que devuelve la funciòn: --------------")
    print(get_numerical_features(df))
    assert get_numerical_features(df) == ['numerica']


def test_get_numerical_features_empty():

    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num."""

    # EJERCICIO
    df = pd.DataFrame({
    "categorica": ["rojo"]
    })

    assert get_numerical_features(df) == []


def test_get_numerical_features_zero_columns():

    """Este test comprueba que se devuelve una lista vacía si el dataframe no tiene ninguna columna."""

    assert get_numerical_features(pd.DataFrame()) == []


def test_get_numerical_features_zero_rows():

    """Este test comprueba que se devuelve una con una variable si el DF

    tiene una variable numérica pero NINGUNA FILA."""

    # Filas sin valores del tipo int
    df = pd.DataFrame( {
            "numerica": pd.Series(dtype=int)
        })

    assert get_numerical_features(df) == ['numerica']



# def test_get_numerical_features_int_and_float():

#     """Este test comprueba que funciona correctamente

#     cuando hay una columna integer y una flotante"""

#     # EJERCICIO


# def test_get_numerical_features_complex():

#     """Este test comprueba que funciona correctamente con número complejos."""

#     # EJERCICIO


def test_fail():

    """Test pytest --f."""

    
    assert 1 == 2
