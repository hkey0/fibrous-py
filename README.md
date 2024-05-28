# Fibrous Finance Router Client for Python

Python client for Fibrous Router. It makes it easy to get the tokens and protocols supported by Fibrous, choose the best route for your swap from the Fibrous API and build those swap transactions. Compatible with Starknetpy.

## Installation
You can install fibrouspy via Pip.
```bash
pip install fibrouspy
```
Or
```bash
git clone https://github.com/hkey0/fibrous-py
cd fibrous-py
pip install .
```

## Usage

Create Fibrous client:
```python
from fibrouspy import FibrousClient

client = FibrousClient()

# or you can specify custom rpc url (you probably you won't need this)
client = FibrousClient(route_url="https://api.fibrous.finance",
                       graph_url="https://graph.fibrous.finance",
                       router_address="0x00f6f4CF62E3C010E0aC2451cC7807b5eEc19a40b0FaaCd00CCA3914280FDf5a")
```

Get supported tokens by Fibrous.
```python
tokens = client.supported_tokens()
tokens["eth"]

# expected output:
Token(
    address='0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7',
    name='Ether',
    symbol='eth',
    decimals=18,
    price='3841.3',
    imageUrl='https://assets.coingecko.com/coins/images/279/small/ethereum.png?1696501628',
    valuable=True,
    verified=True,
    category=None
)
```

Get best route:
```python
tokens = client.supported_tokens()
route = client.get_best_route(amount=10**12,
                        token_in_address=tokens["eth"].address,
                        token_out_address=tokens["usdc"].address)
route

# expected output:
RouteSuccess(
    success=True,
    inputToken=Token(...),
    inputAmount='1000000000000',
    outputToken=Token(...),
    outputAmount='4117',
    route=[Route...],
    estimatedGasUsed='8975364622720',
    bestQuotesByProtocols=['3821', '3876', '3815', '3878', '3838', '4117', '3883', '0', '3838', '5467'],
    time=1.354,
    initial=True
)
```


