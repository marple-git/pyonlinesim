from pyonlinesim import OnlineSim


async def main():
    api_key = '8d84jdNu658Qek1-s1x7VRj9-fPwk264u-R4RNnUwU-62xguYA7cSt25A3'
    client = OnlineSim(api_key=api_key)
    # balance = await client.get_balance()
    # print(balance)
    # country = await client.get_services('371')
    # for service in country.services:
    #     if service.slug != 'whatsapp':
    #         continue
    #     else:
    #         print(service)
    # print(country)
    number = await client.order_number('viber', country=371)
    print('Got Number')
    result = await client.get_order_info(number.operation_id)
    print(result)

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
