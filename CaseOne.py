class CaseOne:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def filter(self):
        # Solo críticas mayores a 10.
        critics = self.data_frame[self.data_frame['reviews'] > 10]
        # Calificación mayor a cuatro estrellas.
        four_stars = critics[critics['overall_satisfaction'] >= 4]
        # Solo 2 habitaciones.
        final_table = four_stars[four_stars['bedrooms'] == 2]
        return final_table

    def order(self):
        # Se ordena de manera descendente tomando en cuenta las reseñas y críticas.
        sorted_table = self.filter().sort_values(['overall_satisfaction', 'reviews'], ascending=False)
        new_table = sorted_table.reset_index(level=None, drop=True)
        new_table.to_excel('Resultado.xlsx', index=True, header=True)
