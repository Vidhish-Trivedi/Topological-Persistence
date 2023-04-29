from MyUtils.Persistence import Persistence

FILE_PATH = "./tests/filtration.txt"


if __name__ == "__main__":
    my_test = Persistence(FILE_PATH=FILE_PATH)

    print("Reducing border matrix...")
    my_test.reduceMatrix()

    # Generating bar-code.
    barCode = my_test.generateBarCodeIntervals()

    for _ in barCode:
        print(_)
