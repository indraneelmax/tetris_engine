
# tetris_engine

**How to Install**

```bash
git clone https://github.com/indraneelmax/tetris_engine

cd tetris_engine

python -m venv testenv

source testenv/bin/activate

pip install .

which tetris_engine

```
**How to Run**

```
tetris_engine --help

Welcome to Simple Tetris Engine - 0.1.0
usage: tetris_engine [-h] input_file [output_file]

A Simple Tetris Engine.

positional arguments:
  input_file   Path to input file
  output_file  Path to output file

optional arguments:
  -h, --help   show this help message and exit

```
**Example Run**
```
# Create the input file
(testenv) bash-4.2$ cat > bin/input2.txt
I0,I4,Q8
T1,Z3,I4
Q0,I2,I6,I0,I6,I6,Q2,Q4

# Run the script
(testenv) bash-4.2$ tetris_engine bin/input2.txt output.txt

Welcome to Simple Tetris Engine - 0.1.0
app - INFO - Input File: bin/input2.txt
app - INFO - Output File: output.txt
tetris_engine.engine - INFO - Initializing Engine...
app - INFO - Processing Input InShape-I0
tetris_engine.engine - INFO - Placed InShape-I0 at Coordinate(0,0)
app - INFO - Processing Input InShape-I4
tetris_engine.engine - INFO - Placed InShape-I4 at Coordinate(0,4)
app - INFO - Processing Input InShape-Q8
tetris_engine.engine - INFO - Placed InShape-Q8 at Coordinate(1,8)
tetris_engine.engine - INFO - Row - 0 to be removed
app - INFO - Max Height - 1
tetris_engine.engine - INFO - Initializing Engine...
app - INFO - Processing Input InShape-T1
tetris_engine.engine - INFO - Placed InShape-T1 at Coordinate(1,1)
app - INFO - Processing Input InShape-Z3
tetris_engine.engine - INFO - Placed InShape-Z3 at Coordinate(2,3)
app - INFO - Processing Input InShape-I4
tetris_engine.engine - INFO - Placed InShape-I4 at Coordinate(3,4)
app - INFO - Max Height - 4
tetris_engine.engine - INFO - Initializing Engine...
app - INFO - Processing Input InShape-Q0
tetris_engine.engine - INFO - Placed InShape-Q0 at Coordinate(1,0)
app - INFO - Processing Input InShape-I2
tetris_engine.engine - INFO - Placed InShape-I2 at Coordinate(0,2)
app - INFO - Processing Input InShape-I6
tetris_engine.engine - INFO - Placed InShape-I6 at Coordinate(0,6)
tetris_engine.engine - INFO - Row - 0 to be removed
app - INFO - Processing Input InShape-I0
tetris_engine.engine - INFO - Placed InShape-I0 at Coordinate(1,0)
app - INFO - Processing Input InShape-I6
tetris_engine.engine - INFO - Placed InShape-I6 at Coordinate(0,6)
app - INFO - Processing Input InShape-I6
tetris_engine.engine - INFO - Placed InShape-I6 at Coordinate(1,6)
app - INFO - Processing Input InShape-Q2
tetris_engine.engine - INFO - Placed InShape-Q2 at Coordinate(3,2)
app - INFO - Processing Input InShape-Q4
tetris_engine.engine - INFO - Placed InShape-Q4 at Coordinate(1,4)
tetris_engine.engine - INFO - Row - 1 to be removed
app - INFO - Max Height - 3
app - INFO - Wrote - output.txt

# Check the output file content
(testenv) bash-4.2$ cat output.txt 
1
4
3

```

# Input Shapes

An Input shape as for example an inverted L shape below occupies coordinates -
(2,1) (1,1) (0,0) (0,1)
These coordinates are in order from top to bottom and left to right order.

```
  |----|----|----|----|
 2        X
  |----|----|----|----|
 1        X
  |----|----|----|----|
 0   X    X
  |----|----|----|----|
     0    1    2    3

```
For positioning in the grid, we use the top left bounding box coordinate for the shape.
(2,0) will be the placement position for the above shape.
The `InShape` interface has `get_coordinates(pos)` call to return the occupied coodinates based on the
input grid position coordinate. Ideally one would create a new class implementing above shape as e.g here InvLShape).
```
[(2,1) (1,1) (0,0) (0,1)] = InvLShape.get_coordinates((2,0))
```
