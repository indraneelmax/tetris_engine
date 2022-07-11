
# tetris_engine

**How to Install**

```
git clone https://github.com/indraneelmax/tetris_engine

cd tetris_engine

pip install .

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
**Example Runs**
```
tetris_engine input.txt output.txt
```

# Input Shapes

An Input shape for example an inverted L shape below occupies coordinates -
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
input grid position coordinate.  
```
[(2,1) (1,1) (0,0) (0,1)] = InvLShape.get_coordinates((2,0))
```
