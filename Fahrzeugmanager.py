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

    def gibFahrzeugnamen(self) -> Array:
        for fahrzeug in sorted(self.collection.keys()):

            print(fahrzeug)

    def gibFahrzeugnamen(self, ausgewählterStandort: str) -> Array:
        for fahrzeug, standort in self.collection.items():
            if ausgewählterStandort in standort:
                print(fahrzeug)

    def bucheFahrzeug(self, name, start, ende) -> bool:
        fahrzeugWurdeNochNieGebucht = len(self.collection[name]) != 3

        if fahrzeugWurdeNochNieGebucht:
            standort = self.collection[name][0]
            self.collection[name] = [standort, start, ende]
            print(f"Ihr Fahrzeug wurde von {start} bis {ende} gebucht ")

            return True

        currentStart = self.collection[name][1]
        currentEnde = self.collection[name][2]
        currentStartDate = datetime.strptime(currentStart, "%Y/%m/%d %H:%M")
        currentEndeDate = datetime.strptime(currentEnde, "%Y/%m/%d %H:%M")
        newStartDate = datetime.strptime(start, "%Y/%m/%d %H:%M")
        newEndeDate = datetime.strptime(ende, "%Y/%m/%d %H:%M")
        buchungKreuztAndereBuchungFall1 = (
            currentStartDate <= newStartDate < currentEndeDate
        )
        buchungKreuztAndereBuchungFall2 = (
            currentStartDate < newEndeDate <= currentEndeDate
        )

        if buchungKreuztAndereBuchungFall1:
            print(
                f"Das Fahrzeug ist von {currentStart} bis {currentEnde} nicht verfügbar!"
            )

            return False

        if buchungKreuztAndereBuchungFall2:
            print(
                f"Das Fahrzeug ist von {currentStart} bis {currentEnde} nicht verfügbar!"
            )

            return False

        standort = self.collection[name][0]
        self.collection[name] = [standort, start, ende]
        print(f"Ihr Fahrzeug wurde von {start} bis {ende} gebucht ")

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
                newStartDate = datetime.strptime(start, "%Y/%m/%d %H:%M")
                newEndeDate = datetime.strptime(ende, "%Y/%m/%d %H:%M")
                currentStart = self.verfuegbareFahrzeuge[car][1]
                currentEnde = self.verfuegbareFahrzeuge[car][2]
                currentStartDate = datetime.strptime(currentStart, "%Y/%m/%d %H:%M")
                currentEndeDate = datetime.strptime(currentEnde, "%Y/%m/%d %H:%M")
                buchungKreuztAndereBuchungFall1 = (
                    currentStartDate <= newStartDate < currentEndeDate
                    or currentStartDate < newEndeDate < currentEndeDate
                )

                if not buchungKreuztAndereBuchungFall1:
                    print(car)
