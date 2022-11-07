from unicodedata import name
from Fahrzeugmanager import Fahrzeugmanager


def main() -> None:
    manager = Fahrzeugmanager()
    manager.fuegeFahrzeugHinzu("Rathaus 1", "Rathaus")
    manager.fuegeFahrzeugHinzu("Bahnhof 1", "Bahnhof")
    manager.fuegeFahrzeugHinzu("Bahnhof 2", "Bahnhof")
    manager.fuegeFahrzeugHinzu("Bahnhof 3", "Bahnhof")
    manager.bucheFahrzeug("Bahnhof 1", "2005/04/14 20:00", "2005/04/15 08:00")
    manager.bucheFahrzeug("Bahnhof 1", "2005/04/15 18:00", "2005/04/16 00:00")
    manager.bucheFahrzeug("Bahnhof 2", "2005/04/14 11:00", "2005/04/15 12:00")
    manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 10:00", "2005/04/15 19:00")

    # print(manager.gibFahrzeugnamen("Bahnhof"))
    # print(manager.gibFahrzeugnamen("Rathaus"))

    # manager.gibVerfuegbareFahrzeuge("Bahnhof", "2005/04/15 11:30", "2005/04/15 19:00")
    # manager.gibVerfuegbareFahrzeuge("Bahnhof", "2005/04/15 12:00", "2005/04/15 18:00")
    # manager.gibVerfuegbareFahrzeuge("Bahnhof", "2005/04/15 19:15", "2005/04/15 23:00")

    # print(manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 09:00", "2005/04/15 10:00"))
    # print(manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 09:00", "2005/04/15 11:00"))
    # print(manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 11:00", "2005/04/15 18:00"))
    # print(manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 18:00", "2005/04/15 20:00"))
    # print(manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 19:00", "2005/04/15 20:00"))
    # print(manager.bucheFahrzeug("Bahnhof 3", "2005/04/15 09:00", "2005/04/15 20:00"))


if __name__ == "__main__":
    main()
