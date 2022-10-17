import pandas as pd
import numpy as np

data_frame = pd.read_csv('resources/airbnb.csv')

# Solo departamentos con habitaciones separadas.
apartment = data_frame[data_frame['room_type'] == "Entire home/apt"]

# Solo críticas mayores a 10.
critics = apartment[apartment['reviews'] > 10]

# Calificación mayor a cuatro estrellas.
four_stars = critics[critics['overall_satisfaction'] >= 4]

# Solo 2 habitaciones.
two_bedrooms = four_stars[four_stars['bedrooms'] == 2]

print(two_bedrooms)
