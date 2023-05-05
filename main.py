from MyUtils.Persistence import Persistence
import matplotlib.pyplot as plt

FILE_PATH = "./tests/torus.txt"

if __name__ == "__main__":
    my_test = Persistence(FILE_PATH=FILE_PATH)

    print("Reducing border matrix...")
    my_test.reduceMatrix()

    # Generating bar-code.
    barCode = my_test.generateBarCodeIntervals()

    x = []
    y = []
    m = -1
    for _ in barCode:
        print(_)
        x.append(_.start)
        if(_.isFinite == True):
            m = max(m, _.end)
        y.append(_.end)

    for i in range(0, len(y)):
        if(y[i] == None):
            y[i] = m + 10       # Fix for INFINITY?
    plt.rcParams["figure.figsize"] = [7.50, 7.50]
    plt.rcParams["figure.autolayout"] = True

    plt.scatter(x, y, alpha=0.35)
    t = tuple(range(0, int(m + 10)))
    plt.plot(t, "r--")
    plt.xlabel("Birth")
    plt.ylabel("Death")
    plt.title(f"Persistence Diagram")
    plt.xticks([i for i in range(0, 50)])
    plt.yticks([i for i in range(0, 50)])
    plt.show()
