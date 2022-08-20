OnlineRent
===========


How to get account balance?
-------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def get_balance(api_token: str) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            result = await client.get_balance()  # Balance(response='1', balance=0.0, frozen_balance=0.0)


    asyncio.run(get_balance(api_token='my_token'))

How to get available tariffs by country?
------------------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineRent

    async def get_services(api_token: str, country: str) -> None:
        async with OnlineRent(api_token=api_token) as client:
            numbers = await client.get_tariffs(country=country)
            for number in numbers:
                print(f'ID: {number.id} | Country: {number.country_name}')



    asyncio.run(get_services(api_token='my_token', country='380')) # 380 is Ukraine telephone code

How to rent a number?
------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineRent

    async def order_number(api_token: str, service: str, country: int) -> None:
        async with OnlineRent(api_token=api_token) as client:
            order = await client.rent_number(country=country, days=1)
            print(f'Number: {order.number} | Country: {order.country} | Messages: {order.messages}')



    asyncio.run(order_number(api_token='my_token', service='google', country=2)) # 2 is a country id received from get_services method.


How to get order info and SMS-Code?
-----------------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineRent

    async def get_order_info(api_token: str, operation_id: int) -> None:
        async with OnlineRent(api_token=api_token) as client:
            my_orders = await client.get_rent_info(operation_id=operation_id) # Get Orders
             print(f'Number: {order.number} | Country: {order.country} | Messages: {order.messages}')


    asyncio.run(get_order_info(api_token='my_token', operation_id=551166) # 551166 is a order.operation_id received from order_number method.

How to finish my order?
------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineRent

    async def finish_order(api_token: str, operation_id: int) -> None:
        async with OnlineRent(api_token=api_token) as client:
            response = await client.finish_rent(operation_id=operation_id)
            print(response)  # OrderManaged(response='1')


    asyncio.run(finish_order(api_token='my_token', operation_id=551166) # 551166 is a order.operation_id received from order_number method.

How to extend number rent?
------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineRent

    async def extend_rent(api_token: str, operation_id: int) -> None:
        async with OnlineRent(api_token=api_token) as client:
            response = await client.extend_rent(operation_id=operation_id, days=1)
            print(response)


    asyncio.run(extend_rent(api_token='my_token', operation_id=551166) # 551166 is a order.operation_id received from order_number method.
