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
    client = FibrousClient()

    tokens = client.supported_tokens()

    swap_call = client.build_transaction(
        amount,
        tokens["eth"].address,
        tokens["usdc"].address,
        0.01,
        "your_address_here")


    approve_call = build_approve_call(
            token_address=tokens["eth"].address,
            amount=amount)

    txre = await account0.execute(calls=[approve_call,
                                         swap_call],
                                  max_fee=int(1e16))

    print(f"Transaction hash: {hex(txre.transaction_hash)}")


if __name__ == "__main__":
    asyncio.run(main())
