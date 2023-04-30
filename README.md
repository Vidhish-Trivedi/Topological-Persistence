# Topological Persistence
- This project was made as part of the course: Basic Computational Topology (SM402) at IIIT-Bangalore.

## Requirements
- This project requires that you have Python (3.8.x) installed, along with pip, which is a package manager for Python.
- Clone the repository and cd into it.

```bash
git clone https://github.com/Vidhish-Trivedi/Topology-Project.git
cd Topology-Project
```
- This directory is the project's root directory.
- Install matplotlib using pip as follows:

```bash
pip install matplotlib
```

## Project Structure
- main.py file is the entry-point of the project.
- The tests/ directory contains text files with sample data to test our project on.
- The MyUtils/ directory contains code files for user-defined classes for representing a Simplex (Simplex.py), an Interval (Interval.py), and a helper class which runs the algorithm described in the paper (Persistence.py).
- The remaining files our standard template files for a Git project.

## Format of Sample Data
* Sample data is available in the tests/ directory.
* Each sample file follows the following structure:
    * Each line corresponds to data for a simplex.
    * The first value denotes the time at which a topological feature was added (discovery time), it is a float value.
    * The second value denotes the dimension of the simplex which is being added, it is an integer value.
    * If the second value is d, then the following d - 1 values corresponds to the indices of vertices which make up the simplex.
    * For example, the line "6.0 2 1 4 7" denotes that a simplex with dimension 2 was discovered at time t = 6.0 and is formed using vertices with indices 1, 4 and 7.

## Running the Project
- Run the following in the project root:

```bash
python main.py
```
- This would output the border matrix, matrix obtained on reducing the border matrix, and the birth time and death time of topological features (simplices) as described in the algorithm.
- In addition to this, the program also generates a persistence diagram for the chosen topological data.
- This diagram is displayed to the user and is also saved in the diagrams/ directory (with filename as the current date-time).

## License

[MIT](https://choosealicense.com/licenses/mit/)
