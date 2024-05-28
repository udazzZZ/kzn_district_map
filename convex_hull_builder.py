import pandas as pd


class ConvexHullBuilder:
    def __init__(self, points: pd.DataFrame):
        self.__points = points

    def get_convex_hull(self) -> pd.DataFrame:

        """
        Формат выходного датафрейма:
        - district
            Название района
        - points
            Список точек выпуклой оболочки района
        - center
            Кортеж центра района (lat, lon)
        - color
            Цвет оболочки района
        """
        
        districts_data = {'district': [], 'points': [], 'center': [], 
                'color': ['green', 'blue', 'yellow', 'red', 'pink', 'white', 'black', 'brown']}

        for district_name in self.__points['district'].unique():
            coordinates = self.__points[self.__points['district'] == district_name][['lat', 'lon']].values
            district_coordinates = []

            for i in coordinates:
                district_coordinates.append((i[0], i[1]))

            points = self.minimal_shell(district_coordinates)
            center = self.get_center(district_coordinates)

            districts_data['district'].append(district_name)
            districts_data['center'].append(center)
            districts_data['points'].append(points)
        
        df = pd.DataFrame(districts_data)
        return df
    
    @staticmethod
    def get_center(coordinates):
        
        sum_lat = 0
        sum_lon = 0

        for i in coordinates:
            sum_lat += i[0]
            sum_lon += i[1]
        
        sum_lat /= len(coordinates)
        sum_lon /= len(coordinates)
    
        return (sum_lat, sum_lon)

    @staticmethod
    def rotate(A, B,C ):
        return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])
    
    def minimal_shell(self, points):
        n = len(points)
        numbers = list(range(n))
        
        for i in range(1, n):
            if points[numbers[i]][1] < points[numbers[0]][1]:
                numbers[i], numbers[0] = numbers[0], numbers[i]
        
        for i in range(2, n):
            for j in range(i, 1, -1):
                if self.rotate(points[numbers[0]], points[numbers[j - 1]], points[numbers[j]]) < 0:
                    numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                else:
                    break
        
        stack = [numbers[0], numbers[1]]
        for i in range(2, n):
            while self.rotate(points[stack[-2]], points[stack[-1]], points[numbers[i]]) < 0:
                del stack[-1]

            stack.append(numbers[i])
        
        result = []
        for i in stack:
            result.append(points[i])

        return result





       
