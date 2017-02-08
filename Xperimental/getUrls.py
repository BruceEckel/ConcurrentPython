import asyncio
import aiohttp

async def fetch_page(url):
    response = await aiohttp.request('GET', "http://" + url)
    assert response.status == 200
    content = await response.read()
    print('URL: {0}:  Content: {1}'.format(url, content))


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(map(fetch_page, [
    'google.com', 'cnn.com', 'twitter.com'
    ])))
loop.close()
