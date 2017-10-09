import logging;


import aiomysql

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from  aiohttp import web

def index(request):
    return web.Response(body=b"<h3> Awesome </h3>")

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('Get', '/', index)
    srv = yield from  loop.create_server(app.make_handler(), '127.0.0.1', 9001)
    logging.info(msg='server started at http://127.0.0.1:9001...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', '192.168.99.12'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

