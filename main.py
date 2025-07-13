import argparse
from world_generator import WorldGenerator

def main():
    parser = argparse.ArgumentParser(description="Minecraft Seed Analyzer")
    parser.add_argument("--seed", type=int, required=True, help="Minecraft Seed")
    args = parser.parse_args()

    world = WorldGenerator(args.seed)

    print("=== Strongholds ===")
    for i, (x, z) in enumerate(world.get_strongholds(3)):
        print(f"Stronghold {i+1}: X={x}, Z={z}")

    print("\n=== Diamonds near (0,0) ===")
    diamonds = world.scan_for_diamonds(0, 0, radius=5)
    for x, y, z in diamonds:
        print(f"Diamond at X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    main()