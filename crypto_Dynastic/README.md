# Dynastic

You find yourself trapped inside a sealed gas chamber, and suddenly, the air is
pierced by the sound of a distorted voice played through a pre-recorded tape.
Through this eerie transmission, you discover that within the next 15 minutes,
this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s
message concludes, a sudden mechanical whirring fills the chamber, followed by
the ominous ticking of a clock. You realise that each beat is one step closer
to death. Darkness envelops you, your right hand restrained by handcuffs, and
the exit door is locked. Your situation deteriorates as you realise that both
the door and the handcuffs demand the same passcode to unlock. Panic is a
luxury you cannot afford; swift action is imperative. As you explore your
surroundings, your trembling fingers encounter a torch. Instantly, upon
flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic
letters etched into the walls and a disturbing image of a Roman emperor drawn
in blood. Decrypting the letters will provide you the key required to unlock
the locks. Use the torch wisely as its battery is almost drained out!

## How to Play

In this challenge there's a [source.py](crypto_dynastic/source.py) file that
has a encrypt function. The function is ran on on the flag and the result is
stored in the [output.txt](crypto_dynastic/output.txt) file. To decrypt the
flag, we can easily write a decrypt function that does the reverse of the
encrypt function. The [solve.py](solve.py) is an example of how to do this.

## Flag

```
HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}
```
