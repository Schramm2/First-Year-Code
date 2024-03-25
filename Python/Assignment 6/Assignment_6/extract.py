#Converting a scrabled code into a readable location on the map
#2022/03/23
#Matthew Schramm
def location(block):
    loc = block[block.find("END")-2:block.find("S",5):-1]
    loc = loc.lower()
    loc = loc.title()
    return loc


def temperature(block):
    temp = block[block.find("N",3)+2:block.find("_")]
    temp = float(temp)
    return temp
    


def x_coordinate(block):
    x = block[block.find(":")+1:block.find(",")]
    return x


def y_coordinate(block):
    y = block[block.find(",")+1:block.find(" ",block.find(","))]
    return y
              


def pressure(block):
    pres = block[block.find("_")+1:block.find(":")]
    pres = float(pres)
    return pres  


def get_block(data):
    b = data[data.find("BEGIN"):data.find("END")+3]
    return b


def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
