### Installation
**Prerequisites:**
- Python 3.10+
- PIP 22.3.1+

**Instructions:**
1) Firstly you need to set up a python virtual environment, make sure you are in the `ecm2423_ca` directory and run

Linux / MacOS
``` shell
python3 -m venv env
```

Windows
``` shell
python -m venv env
```

2) Now you need to activate the virtual environment:

Linux/MacOS
```shell
source env/bin/activate
```

Windows:
```
# cmd.exe
env\Scripts\activate.bat 

# powershell.exe
env\Scripts\Activate.ps1
```

You know the virtual environment is activated if you have a `(env)` at the start of your prompt.

3) Finally, you can install the requirements for the project by using pip

``` shell
pip install -r requirements.txt
```

This is not required to run the program but good to know:
- To deactivate and exit your python virtual environment you can type `deactivate` in your terminal instance.

### Running the Program
The main python file to run the maze solving algorithms is `mazes.py` and this takes command line arguments.

To run the program (in an activated virtual environment):
```shell
python mazes.py <filename> <algorithm>
```

Where `filename` is the location of the maze file you are using, I have included the maze files in the `ecm2423_ca` folder so you can just type the name of the file.

`algorithm` is either `dfs` or `a-star` to run a depth-first search of a-star search on the inputted maze.

Further point, you can run `python mazes.py -h` to get help on the inputs.

An example given here runs the a-star search algorithm on the large maze:
```shell
python mazes.py maze-Large.txt a-star
```

