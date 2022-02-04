class Town:
    longi=0; lati=0
    def __init__(self,name):
        self.townName=name
    def set_latitude(self,latitude):
        self.lati = latitude
    def set_longitude(self,longitude):
        self.longi = longitude
    def __repr__(self):
        return f"Town: {self.townName} | Latitude: {self.lati} | Longitude: {self.longi}"

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
