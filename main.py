class Planet:
    def __init__(self, dist_au, dist_km, size):
        self.dist_au = dist_au
        self.dist_km = dist_km
        self.size = size


mercury = Planet(.39, 57900000, 4879)
venus = Planet(.72, 108200000, 12104)
earth = Planet(1, 149600000, 12756)
mars = Planet(1.52, 227900000, 6792)
jupiter = Planet(5.2, 778600000, 142984)
saturn = Planet(9.54, 1433500000, 120536)
uranus = Planet(19.2, 2872500000, 51118)
neptune = Planet(30.06, 4495100000, 49528)


ex = 0;
while ex == 0:
    print("\n\tROY\'S FUN FACTS!")
    inp = input("\n\tPlease type in undercase the planet you want to learn about \n\tType \"exit\" to exit the program\n\n\tPossible inputs: \"[1] Mercury\" \"[2] Venus\" \"[3] Earth\" \"[4] Mars\" \"[5] Jupiter\" \"[6] Saturn\" \"[7] Uranus\" \"[8] Neptune\" \"[0] Exit\"\n\t")

    match inp:
        case "1":
            print("Mercury Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(mercury.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(mercury.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(mercury.size) + "km")

        case "2":
            print("Venus Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(venus.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(venus.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(venus.size) + "km")

        case "3":
            print("Earth Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(earth.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(earth.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(earth.size) + "km")

        case "4":
            print("Mars Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(mars.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(mars.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(mars.size) + "km")

        case "5":
            print("Jupiter Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(jupiter.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(jupiter.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(jupiter.size) + "km")
        case "6":
            print("Saturn Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(saturn.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(saturn.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(saturn.size) + "km")
        case "7":
            print("Uranus Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(uranus.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(uranus.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(uranus.size) + "km")
        case "8":
            print("Neptune Selected")
            inp2 = input("[1] Distance in au\n[2] Distance in km\n[3] Diameter in km")
            match inp2:
                case '1':
                    print("Distance from Sun in au = " + str(neptune.dist_au) + "au")
                case '2':
                    print("Distance from Sun in km = " + str(neptune.dist_km) + "km")
                case '3':
                    print("Diameter = " + str(neptune.size) + "km")
        case "0":
            ex = 1

