# Colored Squares

In the heart of an ancient forest stands a coloured towering tree, its branches
adorned with countless doors. Each door, when opened, reveals a labyrinth of
branching paths, leading to more doors beyond. As you venture deeper into the
maze, the forest seems to come alive with whispered secrets and shifting
shadows. With each door opened, the maze expands, presenting new choices and
challenges at every turn. Can you understand what's going on and get out of
this maze?

## How to Play

This challenge contains a program written in Folder programming language. This
can be easily transpiled to Python using the `Folder` transpiler.

```bash
$ Folder -l src
```

The program is asking for input and checks if the input satisfies a
multui-equation system.

```python
if (((var_7) - (var_18)) == ((var_8) - (var_9))):
    if (((var_6) + (var_10)) == (((var_16) + (var_20)) + (12))):
        if (((var_8) * (var_14)) == (((var_13) * (var_18)) * (2))):
            if ((var_19) == (var_6)):
                if (((var_9) + (1)) == ((var_17) - (1))):
                    if (((var_11) / ((var_5) + (7))) == (2)):
                        if (((var_5) + ((var_2) / (2))) == (var_1)):
                            if (((var_16) - (9)) == ((var_13) + (4))):
                                if (((var_12) / (3)) == (17)):
                                    if ((((var_4) - (var_5)) + (var_12)) == ((var_14) + (20))):
                                        if ((((var_12) * (var_15)) / (var_14)) == (24)):
                                            if ((var_18) == ((173) - (var_4))):
                                                if ((var_6) == ((63) + (var_5))):
                                                    if (((32) * (var_16)) == ((var_7) * (var_0))):
                                                        if ((125) == (var_21)):
                                                            if (((var_3) - (var_2)) == (57)):
                                                                if (((var_17) - (var_15)) == ((var_18) + (1))):
```

We can make use of the `z3` library to solve the problem. A python
implementation can be found in [solve.py](solve.py).

## Flag

```
HTB{z3r0_byt3_f0ld3rs}
```
