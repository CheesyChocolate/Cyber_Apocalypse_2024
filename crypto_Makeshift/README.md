# Makeshift

Weak and starved, you struggle to plod on. Food is a commodity at this stage,
but you can’t lose your alertness - to do so would spell death. You realise
that to survive you will need a weapon, both to kill and to hunt, but the field
is bare of stones. As you drop your body to the floor, something sharp sticks
out of the undergrowth and into your thigh. As you grab a hold and pull it out,
you realise it’s a long stick; not the finest of weapons, but once sharpened
could be the difference between dying of hunger and dying with honour in
combat.

## How to Play

The challenge provides a [source.py](challenge/source.py) script that make use
of string reverse and character shift to encode a message the flag. The file
[output.txt](challenge/output.txt) contains the encoded message.

To solve the challenge, we can easily reverse the encoding process to decode
the message and obtain the flag. A example of the decoding is shown in
[solve.py](solve.py).

## Flag

```
HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}
```
