# remote_shell
The idea of this project is to make a single executable that can when run will open a remote shell up to another server.

## Compile 

pyinstaller can be used to compile a python file to an exe, but it needs a few DLLs and other files, so this isn't quite what we want.

```
# compile the client to an executable
# look in the dist/client folder for the exe
pyinstaller -y client.py
```
