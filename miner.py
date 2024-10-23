import json
import time
from web3 import Web3

# 连接到以太坊节点
w3 = Web3(Web3.HTTPProvider('https://rpc.testnet.soniclabs.com'))

# 读取私钥
with open('secretkey.txt', 'r') as f:
    private_key = f.read().strip()

# 从私钥获取账户地址
account = w3.eth.account.from_key(private_key)
address = account.address
print("address:", address)

# 合约地址（替换为你的合约地址）
old_contract_address = "0xed27dae583ad40006c7ecfcc56282d0167d35067"
contract_address = Web3.to_checksum_address(old_contract_address)
# 合约 ABI（替换为你的合约 ABI）
contract_abi = json.loads('''[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "allowance",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "needed",
				"type": "uint256"
			}
		],
		"name": "ERC20InsufficientAllowance",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "balance",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "needed",
				"type": "uint256"
			}
		],
		"name": "ERC20InsufficientBalance",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "approver",
				"type": "address"
			}
		],
		"name": "ERC20InvalidApprover",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			}
		],
		"name": "ERC20InvalidReceiver",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			}
		],
		"name": "ERC20InvalidSender",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "ERC20InvalidSpender",
		"type": "error"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "miner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "reward",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "bytes32",
				"name": "nonce",
				"type": "bytes32"
			},
			{
				"indexed": false,
				"internalType": "bytes32",
				"name": "hash",
				"type": "bytes32"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "difficulty",
				"type": "uint256"
			}
		],
		"name": "Mined",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "MAX_SUPPLY",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "REWARD_PER_MINE",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "miner",
				"type": "address"
			}
		],
		"name": "addMiner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "currentDifficulty",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "currentReward",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "currentTargetHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "bytes32",
				"name": "nonce",
				"type": "bytes32"
			}
		],
		"name": "mine",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "miners",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')

# 创建合约对象
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# 检查矿工是否注册
def is_miner_registered(miner_address):
    return contract.functions.miners(miner_address).call()

# 添加矿工
def add_miner(miner_address):
    if is_miner_registered(miner_address):
        print("已注册矿工")  # 已注册矿工
        return
    
    print("未注册矿工，即将注册...")  # 未注册矿工，准备注册
    nonce = w3.eth.get_transaction_count(address)
    print("nonce:", nonce)

    # 获取当前 gas 价格并加价10%
    current_gas_price = w3.eth.gas_price
    adjusted_gas_price = int(current_gas_price * 1.1)  # 加价10%
    
    txn = contract.functions.addMiner(miner_address).build_transaction({
        'chainId': 64165,
        'gas': 2000000,
        'gasPrice': adjusted_gas_price,
        'nonce': nonce,
    })
    
    signed_txn = w3.eth.account.sign_transaction(txn, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"Transaction sent: {tx_hash.hex()}")
    print("注册成功")  # 注册成功

# 挖矿函数
def mine():
    target_address = address  # 挖矿奖励的目标地址
    nonce = 0  # 初始化 nonce

    # 获取当前难度和目标哈希
    difficulty = contract.functions.currentDifficulty().call()
    target_hash = contract.functions.currentTargetHash().call()

    # 打印当前难度和目标哈希
    print(f"difficulty: {hex(difficulty)}")
    print(f"target_hash: {target_hash.hex()}")  # 假设 target_hash 是 bytes32 格式
    
    while True:
        # 将 nonce 转换为 bytes32
        nonce_bytes = Web3.to_bytes(nonce).rjust(32, b'\0')  # 确保是 bytes32 格式

        # 计算哈希
        hash_result = w3.keccak(nonce_bytes + target_hash)

        # 在同一行显示当前哈希
        print(f"\r当前哈希值: {hash_result.hex()}", end='')  # 使用 \r 来覆盖这一行

        if int(hash_result.hex(), 16) < difficulty:
            print("\nHash meets difficulty, proceeding to mine...")
            adjusted_gas_price = int(w3.eth.gas_price * 1.1)  # 加价10%

            # 获取最新 nonce
            nonce_for_tx = w3.eth.get_transaction_count(address)

            txn = contract.functions.mine(target_address, nonce_bytes).build_transaction({
                'chainId': 64165,
                'gas': 2000000,
                'gasPrice': adjusted_gas_price,
                'nonce': nonce_for_tx,
            })

            signed_txn = w3.eth.account.sign_transaction(txn, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            print(f"\nMining transaction sent: {tx_hash.hex()}")
            time.sleep(0.5)  # 挖矿成功后休息0.5秒
            break  # 发送交易后停止挖矿

        nonce += 1  # 增加 nonce
        
# 示例：添加矿工并挖矿
if __name__ == "__main__":
    # 将当前账户添加为矿工
    add_miner(address)
    
    # 开始挖矿
    mine()
