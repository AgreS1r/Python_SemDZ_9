# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd
# Считываем данные из файла california_housing_train.csv в DataFrame
df = pd.read_csv("sample_data/california_housing_train.csv")

# Отбираем строки, где значение столбца "population" находится в диапазоне от 0 до 500
subset = df[(df["population"] >= 0) & (df["population"] <= 500)]

# Вычисляем среднее значение столбца "median_house_value" в отфильтрованном DataFrame
mean_house_value = subset["median_house_value"].mean()

print(f"Средняя стоимость дома с населением от 0 до 500: {mean_house_value:.2f}")

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd
# Считываем данные из файла california_housing_train.csv в DataFrame
df = pd.read_csv("california_housing_train.csv")

# Находим минимальное значение столбца "population"
min_population = df["population"].min()

# Отбираем строки, где значение столбца "population" равно минимальному
subset = df[df["population"] == min_population]

# Находим максимальное значение столбца "households" в отфильтрованном DataFrame
max_households = subset["households"].max()

print(f"Максимальное значение households в зоне минимального значения population: {max_households}")