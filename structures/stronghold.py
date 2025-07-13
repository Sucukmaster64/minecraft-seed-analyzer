from java_random import JavaRandom

def find_strongholds(seed, ring=1):
    rand = JavaRandom(seed)
    angle = rand.next_int(360)  # Zufälliger Startwinkel
    distance = 1400 + rand.next_int(800)  # Entfernung vom Ursprung

    # Polar- zu kartesischen Koordinaten
    x = int(distance * math.cos(math.radians(angle)))
    z = int(distance * math.sin(math.radians(angle)))

    return x, z