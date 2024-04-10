import base58
import base64
import json
import os

# for loading my env file
from dotenv import load_dotenv

# sol packages
from solders.message import Message  # type: ignore
from solders.pubkey import Pubkey  # type: ignore
from solders.keypair import Keypair  # type: ignore
from solders.transaction import VersionedTransaction  # type: ignore

from solana.rpc.types import TxOpts
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Processed

# jupiter packages
from jupiter_python_sdk.jupiter import Jupiter, Jupiter_DCA

load_dotenv()

private_key_base58 = os.getenv('SOLANA_PRIVATE_KEY')

private_key_bytes = base58.b58decode(private_key_base58)

wallet_keypair = Keypair.from_secret_key(private_key_bytes)

jupiter = Jupiter(wallet=wallet_keypair)


'''
TODO:
copy code block from SDK code snippet
conditions:
mint authority
burnt LP
liquidity
top holder % 

functions:
stop loss
take profit

maybe check if there was initial large purchase? 
'''