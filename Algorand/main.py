import time

from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams
)

algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
# print(dispenser)

creator = algorand.account.random()
# print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender = dispenser.address,
        receiver = creator.address,
        amount = 50_000_000
    )
)

# print(algorand.account.get_information(creator.address))

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=1337,
        asset_name="Buildh3r - Asset",
        unit_name="HER"
    )
)

asset_id = sent_txn["confirmation"]["asset-index"]
# print(asset_id)

receivers_acct = [algorand.account.random(), algorand.account.random(), algorand.account.random()]

for receiver_acct in receivers_acct:
    algorand.send.payment(
        PayParams(
            sender = dispenser.address,
            receiver = receiver_acct.address,
            amount = 10_000_000
        )
    )

    algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=receiver_acct.address,
            asset_id=asset_id
        )
    )

    asset_transfer = algorand.send.asset_transfer(
        AssetTransferParams(
            sender=creator.address,
            receiver=receiver_acct.address,
            asset_id=asset_id,
            amount=5
        )
    )

    print(algorand.account.get_information(receiver_acct.address))
    time.sleep(1)
