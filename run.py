#! /usr/bin/env python3

import asyncio
import os
import sys
import signal

# configuration
host_ip = '0.0.0.0'
host_port = '8000'

# restart time (in minutes)
duration = 5

# main code

restart_time = duration * 60

class Timer:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        self._task.cancel()

async def run_uvicorn():
    print("Running FastAPI ...")
    os.system("uvicorn main:app --host=" + host_ip +" --port=" + host_port +" &")

async def main():
    timer = Timer(0, run_uvicorn)
    await asyncio.sleep(restart_time)
    signal.signal(signal.SIGINT, signal_handler)
    os.system("pkill uvicorn")
    os.execv(__file__, sys.argv)

async def signal_handler(sig, frame):
    sys.exit(0)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    signal.signal(signal.SIGINT, signal_handler)
    print('Terminating service ...')
    os.system("pkill uvicorn")
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
    


    