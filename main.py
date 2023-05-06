from MyUtils.Persistence import Persistence
import matplotlib.pyplot as plt
from math import ceil

FILE_PATH = "./tests/GNUsphere5_out.txt"

if __name__ == "__main__":
    my_test = Persistence(FILE_PATH=FILE_PATH)

    print("Reducing border matrix...")
    my_test.reduceMatrix()

    # Generating bar-code.
    print("Generating bar code intervals\n")
    barCode = my_test.generateBarCodeIntervals()

    # Generating Persistence Diagram.
    print("Generating Persistence Diagram\n")
    x = []
    y = []
    x_betti = []
    y_betti = []
    m = -1
    for _ in barCode:
        print(_)
        x.append(_.start)
        if(_.isFinite == True):
            m = max(m, _.end)
        y.append(_.end)

    for i in range(0, len(y)):
        if(y[i] == None):
            y[i] = 2*ceil(0.7*m) + 2
            y_betti.append(2*ceil(0.7*m) + 2)
            x_betti.append(x[i])
    plt.rcParams["figure.figsize"] = [7.50, 7.50]
    plt.rcParams["figure.autolayout"] = True


    plt.scatter(x, y, alpha=0.35)
    plt.scatter(x_betti, y_betti, color='r')
    t = tuple(range(0, int(m + 10)))
    plt.plot(t, "r--")
    plt.xlabel("Birth")
    plt.ylabel("Death")
    plt.title(f"Persistence Diagram for " + FILE_PATH.split("tests/")[1].replace(".txt", ""))
    plt.xticks([2*i for i in range(0, ceil(0.7*m))])
    plt.yticks([2*i for i in range(0, ceil(0.7*m))])
    img_path = "./plots/persistence_diagrams" + FILE_PATH.split("tests")[1].replace("txt", "png")
    
    # Save non-interactive png file.
    plt.savefig(img_path, bbox_inches='tight')
    print("\nPersistence Diagram saved.\n")
    # Display interactive matplotlib window.
    print("\nPersistence Diagram display is being rendered.\n")
    plt.show()
