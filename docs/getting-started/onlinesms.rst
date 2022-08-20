How to get account balance?
-------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def get_balance(api_token: str) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            result = await client.get_balance()  # Balance(response='1', balance=0.0, frozen_balance=0.0)


    asyncio.run(get_balance(api_token='my_token'))

How to get available services by country?
------------------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def get_services(api_token: str, country: str) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            country = await client.get_services(country=country)
            for service in country.services:
                print(f'ID: {service.id} | Available Numbers: {service.count} | Service: {service.service} | Price: {service.price}')



    asyncio.run(get_services(api_token='my_token', country='380')) # 380 is Ukraine telephone code

How to order a number?
------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def order_number(api_token: str, service: str, country: int) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            order = await client.order_number(service=service, country=country, number=True)
            print(f'Operation ID: {order.operation_id} | Received number: {order.number}')



    asyncio.run(order_number(api_token='my_token', service='google', country=2)) # 2 is a country id received from get_services method.


How to get order info and SMS-Code?
-----------------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def get_order_info(api_token: str, operation_id: int) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            my_orders = await client.get_order_info(operation_id=operation_id) # Get Orders
            order = my_orders.orders[0] # Get First Order
            print(f'Country: {order.country} | Service: {order.service} | SMS-Code: {order.msg}')



    asyncio.run(get_order_info(api_token='my_token', operation_id=551166) # 551166 is a order.operation_id received from order_number method.

How to finish my order?
------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def finish_order(api_token: str, operation_id: int) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            response = await client.finish_order(operation_id=operation_id)
            print(response)  # OrderManaged(response='1', operation_id=551166)


    asyncio.run(finish_order(api_token='my_token', operation_id=551166) # 551166 is a order.operation_id received from order_number method.


I want to get one more code for this number, how can i do this?
-----------------------------------------------------------------


.. code-block:: python

    import asyncio

    from pyonlinesim import OnlineSMS

    async def revise_order(api_token: str, operation_id: int) -> None:
        async with OnlineSMS(api_token=api_token) as client:
            response = await client.revise_order(operation_id=operation_id)
            print(response)  # OrderManaged(response='1', operation_id=551166)
            # Use get_order_info to get new SMS-Code


    asyncio.run(revise_order(api_token='my_token', operation_id=551166) # 551166 is a order.operation_id received from order_number method.
