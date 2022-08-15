from pyonlinesim import OnlineRent
from pyonlinesim.clients import OnlineSMS


async def main():
    async with OnlineRent('2MDT6StrLXFgj12-5hdnM91X-K8FVsf9g-CLS75X9m-NpS7F8wJDHbSr2Z') as client:
        tariffs = await client.get_tariffs()
        for tariff in tariffs:
            # One Day Price & Amount
            print(f'One Day Price: {tariff.numbers.one_day.price}, Amount: {tariff.numbers.one_day.amount}')



if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
