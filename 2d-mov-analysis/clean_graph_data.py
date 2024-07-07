
filename = "val_1.txt"  # Nombre del archivo a analizar

times = []
posx = []
posy = []

if __name__ == '__main__':
    with open(filename, "r") as file:
        data = file.read().split()

    counter = 1
    for d in data:
        if counter == 1:
            times.append(d)
        elif counter == 2:
            posx.append(d)
        elif counter == 3:
            posy.append(d)
            counter = 0
        counter += 1

    print(times)
    print(posx)
    print(posy)
