# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import uvicorn

from apps.bin.start import create_app
from apps.conf.secure import (
    HOST, PORT, DEBUG
)

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app="main:app", host=HOST, port=PORT, reload=True, debug=DEBUG)
