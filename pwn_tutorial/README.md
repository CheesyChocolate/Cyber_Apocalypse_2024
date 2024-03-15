# Tutorial

Before we start, practice time!

## How to Play

Connect to the server using the netcat command.

The challenge is simple questions that try to teach the idea behind Integer
Overflow.

### Question 0x1

Is it possible to get a negative result when adding 2 positive numbers in C? (y/n)

_Answer:_ y

### Question 0x2

What's the MAX 32-bit Integer value in C?

_Answer:_ 2147483647

### Question 0x3

What number would you get if you add INT_MAX and 1?

**NOTE:** The `C` file provided in the challenge can assist to add the numbers.

_Answer:_ -2147483648

### Question 0x4

What number would you get if you add INT_MAX and INT_MAX?

_Answer:_ -2

### Question 0x5

What's the name of this bug? (e.g. buffer overflow)

_Answer:_ integer overflow

### Question 0x6

What's the MIN 32-bit Integer value in C?

_Answer:_ -2147483648

### Question 0x7

What's the number you can add to INT_MAX to get the number -2147482312?

_Answer:_ 1337

## Flag

```
HTB{gg_3z_th4nk5_f0r_th3_tut0r14l}
```
