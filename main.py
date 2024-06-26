import asyncio
import sys
import logging
from app import main
from db import down, up


if __name__ == "__main__":
    # Uncomment row below this for recreate database
    # down()
    up()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
