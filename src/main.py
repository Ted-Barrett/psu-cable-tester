from pprint import pprint

ALLOWED_VALUES = ("0", "1")


def parse_connectors(arr):
    arr.append("+")
    connectors = set()

    active = False
    connector = []
    for line in arr:
        if line[0] == "#":
            continue
        if line[0] == ">":
            active = True
            if connector:
                connectors.add(tuple(connector))
            connector = []
            continue
        if line[0] == "+":
            if connector:
                connectors.add(tuple(connector))
            connector = []
            active = False
            continue

        if active and line.strip() != "":
            connector.append(line.strip())
    if validate_connectors(connectors):
        return connectors
    raise ValueError("Invalid input.")


def name_connector(connector):
    name = ""
    name += str(len(connector)) + "x"
    name += str(len(connector[0])) + "g"
    name += str(int("".join(connector), 2))

    return name


def validate_connectors(s):
    for connector in s:
        first_row_length = len(connector[0])

        for row in connector:
            if len(row) != first_row_length:
                return False

            if not all([c in ALLOWED_VALUES for c in row]):
                return False

    return True


def check_compatible(male, female):
    if len(male) != len(female):
        return False

    male_row_length, female_row_length = len(male[0]), len(female[0])
    for male_offset in range(female_row_length - male_row_length + 1):
        compatible = True
        for row in range(len(male)):
            for i in range(len(male[row])):
                m = male[row][i] == "1"
                f = female[row][i + male_offset] == "1"

                if f and (not m):
                    compatible = False
                    break
            if not compatible:
                break
        if compatible:
            return male_offset

    return -1


if __name__ == "__main__":
    with open("./known_connectors.txt") as f:
        lines = f.readlines()

    connectors = parse_connectors(lines)

    print(len(connectors), "unique connectors detected.")
    print("Checking for incompatibilities.\n")

    for male in connectors:
        female = ("100110011001", "011001100110")
        offest = check_compatible(male, female)

        if offest == -1:
            print(name_connector(male) + ": INCOMPATIBLE")
            for row in male:
                print(" " + row)
        else:
            print(name_connector(male) + ": Compatible")
