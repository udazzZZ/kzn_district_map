import pandas as pd
from ipyleaflet import Map, Marker, Polygon, FullScreenControl, LegendControl
from ipywidgets import Layout


class MapRenderer:
    def __init__(self, district_data: pd.DataFrame, points_data: pd.DataFrame):
        self.__points_data = points_data
        self.__district_data = district_data

    def get_map(self) -> Map:

        """
        TODO:
        - Создать карту с центром в центре города (с медианой lat и медианой lon)
        - Для каждого района нарисовать Polygon с цветом района
        - Для каждого района нарисовать неперемещаемый Marker в центре района с title=<название_района>
        - Для каждого района добавить в LegendControl цвет с соответствующим именем района
        - Добавить FullScreenControl в карту
        - Использовать в карте Layout(width='100%', height='800px')
        """
        
        layout = Layout(width='100%', height='800px')

        center = (55.796127, 49.106414)

        m = Map(
            center=center,
            zoom=11,
            layout=layout
        )

        for index, row in self.__district_data.iterrows():
            color = row['color']

            points = row['points'][2:-2]
            points = points.replace(')', '')
            points = points.replace('(', '')
            points = points.split(',')
            points_for_polygon = []
            for i in range(0, len(points), 2):
                points_for_polygon.append((float(points[i]), float(points[i + 1])))

            polygon = Polygon(
                locations=points_for_polygon,
                color=color,
                fill_color=color
            )

            district_center = row['center'][1:-1]
            district_center = district_center.split(',')
            res_disctrict_center = []
            for i in range(0, len(district_center), 2):
                res_disctrict_center.append((float(district_center[i]), float(district_center[i + 1])))

            marker = Marker(
                location=res_disctrict_center[0],
                draggable=False,
                title=row['district']
            )

            legend = LegendControl(
                {'': color},
                title=row['district']
            )

            m.add(polygon)
            m.add(marker)
            m.add(FullScreenControl())
            m.add(legend)

        return m

