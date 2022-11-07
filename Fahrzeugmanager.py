from ctypes import Array
from unicodedata import name
from datetime import datetime


class Fahrzeugmanager:
    def __init__(self) -> None:
        self.collection: dict = {}

    def fuegeFahrzeugHinzu(self, name: str, standort: str) -> str:
        if name not in self.collection:
            self.collection[name] = [standort]
        else:
            print("Dieses Fahrzeug existiert bereits")

    def gibFahrzeugnamen(self) -> list:
        fahrzeugliste: list = []
        for fahrzeug in sorted(self.collection.keys()):
            fahrzeugliste.append(fahrzeug)

        return fahrzeugliste

    def gibFahrzeugnamen(self, ausgewählterStandort: str) -> list:
        fahrzeugliste: list = []
        for fahrzeug, standort in self.collection.items():
            if ausgewählterStandort in standort:
                fahrzeugliste.append(fahrzeug)

        return fahrzeugliste

    def bucheFahrzeug(self, name, start, ende) -> bool:
        fahrzeugWurdeNochNieGebucht = len(self.collection[name]) != 3

        if fahrzeugWurdeNochNieGebucht:
            standort = self.collection[name][0]
            self.collection[name] = [standort, start, ende]

            return True

        if not self.istFahrzeugVerfügbar(start, ende, name):
            return False

        standort = self.collection[name][0]
        self.collection[name] = [standort, start, ende]

        return True

    def gibVerfuegbareFahrzeuge(self, standort, start, ende) -> Array:
        self.verfuegbareFahrzeuge = {}

        for collection in self.collection.items():
            if standort in collection[1]:
                self.verfuegbareFahrzeuge[collection[0]] = collection[1]

        for car in self.verfuegbareFahrzeuge:
            fahrzeugWurdeNochNieGebucht = len(self.verfuegbareFahrzeuge[car]) != 3
            if fahrzeugWurdeNochNieGebucht:
                print(car)

            else:
                if self.istFahrzeugVerfügbar(start, ende, car):
                    print(car)

    def istFahrzeugVerfügbar(self, start, ende, name) -> bool:
        currentStart = self.collection[name][1]
        currentEnd = self.collection[name][2]
        currentStartDate = datetime.strptime(currentStart, "%Y/%m/%d %H:%M")
        currentEndDate = datetime.strptime(currentEnd, "%Y/%m/%d %H:%M")
        newStartDate = datetime.strptime(start, "%Y/%m/%d %H:%M")
        newEndDate = datetime.strptime(ende, "%Y/%m/%d %H:%M")
        buchungKreuztAndereBuchungFall1 = (
            currentStartDate <= newStartDate < currentEndDate
        )
        buchungKreuztAndereBuchungFall2 = (
            currentStartDate < newEndDate <= currentEndDate
        )

        if not buchungKreuztAndereBuchungFall1 and not buchungKreuztAndereBuchungFall2:
            return True

        return False
