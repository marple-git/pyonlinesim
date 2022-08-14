from pyonlinesim import OnlineSim


async def main():
    api_key = '8d84jdNu658Qek1-s1x7VRj9-fPwk264u-R4RNnUwU-62xguYA7cSt25A3'
    async with OnlineSim(api_key=api_key) as client:
        balance = await client.get_balance()
        print(balance)
        services = await client.get_services()
        print(services)

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
