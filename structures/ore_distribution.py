from java_random import JavaRandom

def find_diamond_chunks(seed, chunk_x, chunk_z, world_height=-64):
    rand = JavaRandom(seed + chunk_x * 341873128712 + chunk_z * 132897987541)
    if rand.next_int(10) < 2:  # 20% Chance für Diamant im Chunk
        diamond_y = world_height + rand.next_int(80)  # Y=-64 bis 16
        return (chunk_x * 16, diamond_y, chunk_z * 16)
    return None