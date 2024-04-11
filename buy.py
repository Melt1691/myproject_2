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

private_key = Keypair.from_bytes(base58.b58decode(os.getenv('SOLANA_PRIVATE_KEY')))
async_client = AsyncClient("SOLANA_RPC_ENDPOINT_URL") 

jupiter = Jupiter(
    async_client=async_client,
    keypair=private_key,
    quote_api_url="https://quote-api.jup.ag/v6/quote?",
    swap_api_url="https://quote-api.jup.ag/v6/swap",
    open_order_api_url="https://jup.ag/api/limit/v1/createOrder",
    cancel_orders_api_url="https://jup.ag/api/limit/v1/cancelOrders",
    query_open_orders_api_url="https://jup.ag/api/limit/v1/openOrders?wallet=",
    query_order_history_api_url="https://jup.ag/api/limit/v1/orderHistory",
    query_trade_history_api_url="https://jup.ag/api/limit/v1/tradeHistory"
)

'''
TODO:
listen to new launches in the last 24h
check if any of them fulfill criteria
if fulfill, 
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