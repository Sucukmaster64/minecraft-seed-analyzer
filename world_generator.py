from structures.stronghold import find_strongholds
from structures.ore_distribution import find_diamond_chunks

class WorldGenerator:
    def __init__(self, seed):
        self.seed = seed

    def get_strongholds(self, count=3):
        return [find_strongholds(self.seed, ring=i) for i in range(count)]

    def scan_for_diamonds(self, center_chunk_x, center_chunk_z, radius=10):
        diamonds = []
        for dx in range(-radius, radius):
            for dz in range(-radius, radius):
                chunk_x, chunk_z = center_chunk_x + dx, center_chunk_z + dz
                if pos := find_diamond_chunks(self.seed, chunk_x, chunk_z):
                    diamonds.append(pos)
        return diamonds