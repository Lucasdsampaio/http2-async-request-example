import asyncio
import logging
import time
import requests
import httpx
import time


async def teste1(queries):
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(query) for query in queries]
        responses = await asyncio.gather(*tasks)
    results = (response.json() for response in responses)   
    print(time.time() - start)
    return results

def teste2(query):
    start = time.time()
    results = []
    for url in query:
        response = requests.get(url)
        results.append(response.json())
    print(time.time() - start, "--2")
    return results


def run():
    queries = [
        "http://localhost:8000/teste1",
        "http://localhost:8000/teste2"
    ]
    asyncio.run(teste1(queries))
    teste2(queries)


run()
