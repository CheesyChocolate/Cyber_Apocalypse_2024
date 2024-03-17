# Rids

Upon reaching the factory door, you physically open the RFID lock and find a
flash memory chip inside. The chip's package has the word W25Q128 written on
it. Your task is to uncover the secret encryption keys stored within so the
team can generate valid credentials to gain access to the facility.

## How to Play

A URL and a python [script](./hardware_rids/client.py) client are provided. The
client is a simple interface for SPI Flash memory. A search in the web for the
chip memory a [instruction
list](https://www.totalphase.com/support/articles/200350146-reading-device-id-from-spi-flash-using-aardvark-adapter-and-control-center/)
is found.

Instead of `9Fh` instruction that is meant for `Read Identification` the
`03h` can be used to `Read Data Bytes`.

```python
data = exchange([0x03], 50)
print("".join([chr(x) for x in data]))
```

## Flag

```
HTB{m3m02135_57023_53c2375_f02_3v32y0n3_70_533!@}
```
