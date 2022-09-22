class SportsNews():
    def __init__(self):
        print("this is sports news channel")
        self.infoSport()

    def infoSport(self):
        self.sport = "Cricket"
        self.category = "Live TV"
        print(" India vs Pakistan match", self.sport, self.category)

class BollyNews():
    def __init__(self):
        print("this is bollywood news channel")
        self.infoBolly()

    def infoBolly(self):
        self.movie = "Hindi"
        self.genre = "Crime"
        print(" India vs Pakistan match", self.movie, self.genre)

class News():

    def __init__(self):
        print("I am main news channel")


    def info(self):
        self.objS = SportsNews()
        self.objB = BollyNews()

objN = News()
objN.info()