import sys

PLATES = [45, 35, 25, 10, 5, 2.5]
BAR = 45
UOM = "lb"


def calc_weight(target_weight: int) -> dict:
    remainder = (target_weight - BAR) / 2
    plates_needed = dict.fromkeys(PLATES, 0)

    for plate in PLATES:
        while (remainder // plate) > 0:
            plates_needed[plate] += 1
            remainder -= plate

    if remainder > 0:
        print("")
        print(f"Plate inventry does not work with Target Weight. Subracting {remainder * 2} {UOM}")
        print(f"New Target Weight: {target_weight - (remainder * 2)} {UOM}")

    return plates_needed

def print_results(results: dict):
    print("")
    print(f"Plates Needed ({BAR} {UOM} bar)")
    print("-------------------------")

    for key, value in results.items():
        if value != 0:
            print(f"{key:3} {UOM} plates: {value} pair(s)")


if __name__ == "__main__":
    target_weight = float(sys.argv[1])
    print(f'Target Weight: {target_weight} {UOM}')

    results = calc_weight(target_weight)
    print_results(results)
