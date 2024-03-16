# Russian Roulette

Welcome to The Fray. This is a warm-up to test if you have what it takes to
tackle the challenges of the realm. Are you brave enough?

## How to Play

Two URL are provided, One is netcat server and the other is the ethereum
contract.

Two files are provided, `Setup.sol` and `RussianRoulette.sol`. The goal is in
the `Setup.sol` file.

```solidity
constructor() payable {
    TARGET = new RussianRoulette{value: 10 ether}();
}

function isSolved() public view returns (bool) {
    return address(TARGET).balance == 0;
}
```

To solve the challenge, the `isSolved` function must return `true`. This happens
when the `RussianRoulette` contract has a balance of `0`.

As we can see in the `RussianRoulette` contract,

```solidity
if (uint256(blockhash(block.number - 1)) % 10 == 7) {
    selfdestruct(payable(msg.sender)); // 💀
```

The `RussianRoulette` contract will self-destruct if the last digit of the
previous block hash is `7`. The goal is to make the `RussianRoulette` contract
self-destruct. and by runnung the function in average 10 times, the contract
will self-destruct.

A [python script](./solve.py)


## Flag
