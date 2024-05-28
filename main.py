import asyncio

from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair

from fibrouspy.core import FibrousClient
from fibrouspy.utils import build_approve_call


async def main():
    account0 = Account(
        address="your_address_here",
        client=FullNodeClient("https://rpc.starknet.lava.build:443"),
        key_pair=KeyPair(private_key="private_key_here",
                         public_key="your_address_here"),
        chain=StarknetChainId.MAINNET)

    amount = 10**15
    api = FibrousClient()
    data = api.build_transaction(
        amount,
        # eth contract address
        "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
        # USDC contract adddress
        "0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
        0.01,
        "your_address_here")


    apr = build_approve_call(
            token_address="0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
            amount=amount)

    txre = await account0.execute(calls=[apr, data],
                                  max_fee=int(1e16))

    print(f"Transaction hash: {hex(txre.transaction_hash)}")


if __name__ == "__main__":
    asyncio.run(main())
