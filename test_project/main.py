from pyonlinesim import OnlineSim

API_KEY = '8d84jdNu658Qek1-s1x7VRj9-fPwk264u-R4RNnUwU-62xguYA7cSt25A3'


async def get_balance():
    async with OnlineSim(API_KEY) as client:
        balance = await client.get_balance()
        print(balance)  # Balance(response='1', balance=0.0, frozen_balance=0.0)


if __name__ == '__main__':
    import asyncio

    asyncio.run(get_balance())
