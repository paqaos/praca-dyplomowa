from src.Helpers.DistancePointCalculator import DistancePointCalculator

class ShortestPath:
    @staticmethod
    def calculate(board, player, source, target):
        cities = []
        result = []
        found = False
        for city in board.Cities:
            tmpCity = CityTarget(city)
            cities.append(tmpCity)

        for i in cities:
            if i.inner == source:
                i.cost = 0

        while len(cities) > 0:
            minCity = cities[0]
            for city in cities:
                if city.cost < minCity.cost:
                    minCity = city

            cities.remove(minCity)

            if minCity.inner == target:
                found = True
                break

            for conn in minCity.inner.Connections:
                if conn.cities[0].id != minCity.inner.id:
                    otherCity = conn.cities[0]
                else:
                    otherCity = conn.cities[1]

                exists = False
                for city in cities:
                    if city.inner.id == otherCity.id:
                        exists = True

                if not exists:
                    continue

                for x in cities:
                    if x.inner.id == otherCity.id:
                        actual = x

                alt = int(minCity.cost) + int(conn.getCost(player))
                altPoints = int(minCity.points) + int(DistancePointCalculator.calculatePoints(conn.size))
                if (alt < actual.cost) or (alt == actual.cost and altPoints > actual.points):
                    actual.cost = alt
                    actual.previous = minCity
                    actual.conn = conn
                    actual.points = altPoints

        if found and minCity.cost < float("inf"):
            actual = minCity
            while actual is not None and actual.inner is not None:
                result.insert(0, actual)
                actual = actual.previous
            return result

        return None


class CityTarget:
    def __init__(self, inner):
        self.cost = float("inf")
        self.inner = inner
        self.previous = None
        self.conn = None
        self.points = 0
