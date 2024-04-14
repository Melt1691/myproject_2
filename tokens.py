from datetime import datetime, timedelta
from solana.publickey import PublicKey

from solana.rpc.api import Client
import os
from dotenv import load_dotenv


load_dotenv()


def get_new_tokens_last_24_hours():
    # Set up Solana RPC client; you may need to select an appropriate endpoint
    client = Client(os.getenv("SOLANA_RPC_ENDPOINT_URL"))

    # Define the current time and the time 24 hours ago
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)

    # The address for the Token Program on Solana - used to identify token transactions
    token_program_id = PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")

    # Fetch recent transaction signatures associated with the Token Program
    signatures = client.get_signatures_for_address(
        token_program_id,
        before=end_time.isoformat(),
        limit=1000
    )

    new_tokens = []
    for signature in signatures['result']:
        # Fetch transaction details
        transaction = client.get_transaction(signature['signature'])
        transaction_time = datetime.fromtimestamp(transaction['blockTime'])

        # Filter transactions within the last 24 hours
        if start_time <= transaction_time <= end_time:
            # Here, you would parse the transaction to find new tokens creation details
            # This part depends heavily on how new token transactions are structured
            new_tokens.append({
                'signature': signature['signature'],
                'time': transaction_time.isoformat(),
                # Additional parsing would be needed here to extract more details
            })

    return new_tokens


# Example usage
new_tokens = get_new_tokens_last_24_hours()
for token in new_tokens:
    print(token)
