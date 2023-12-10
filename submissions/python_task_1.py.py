# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hLhVhyByIoBI09XgPyxff244R_ubS0BL
"""

import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    df1 = pd.DataFrame(df)
    df1.set_index(['id_1', 'id_2'], inplace=True)
    result_df = df1['car'].unstack(fill_value=0)
    df=result_df
    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    df1 = pd.DataFrame(df)
    bins = [-float('inf'), 15, 25, float('inf')]
    labels = ['low', 'medium', 'high']
    df1['car_type'] = pd.cut(df1['car'], bins=bins, labels=labels, right=False)
    result_dict = dict(sorted(df1['car_type'].value_counts().items()))
    return result_dict

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    df1 = pd.DataFrame(df)
    # Write your logic here
    mean_value = df1['bus'].mean()
    # Identify indices where 'bus' values are greater than twice the mean
    indices_greater_than_twice_mean = df1[df1['bus'] > 2 * mean_value].index.tolist()
    # Sort the indices in ascending order
    list=indices_greater_than_twice_mean
    list.sort()
    return list

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    df1 = pd.DataFrame(df)
    average_truck_by_route = df1.groupby('route')['truck'].mean()
    selected_routes = average_truck_by_route[average_truck_by_route > 7].index.tolist()
    list=selected_routes
    list.sort()
    return list

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    def multiply_values(value):
      if value > 20:
        return value * 0.75
      else:
        return value * 1.25
    df_new = matrix.applymap(multiply_values)
    return matrix

def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()