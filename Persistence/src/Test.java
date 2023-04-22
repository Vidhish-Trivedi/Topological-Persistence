import java.io.FileNotFoundException;

public class Test {

    public static void main(String[] args) throws FileNotFoundException {

        persistence p = new persistence("../tests/filtration.txt");
        // sparse_persistence p = new sparse_persistence("../tests/filtration.txt");

        p.reduction();
        p.computeBarCode();
    }
}
