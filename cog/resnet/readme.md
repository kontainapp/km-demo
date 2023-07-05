# issues
- runs in docker
- issue running in kontain
    - Temporary failure in name resolution when downloading model

```bash
...
File "/usr/local/lib/python3.8/http/client.py", line 1251, in endheaders
self._send_output(message_body, encode_chunked=encode_chunked)
File "/usr/local/lib/python3.8/http/client.py", line 1011, in _send_output
self.send(msg)
File "/usr/local/lib/python3.8/http/client.py", line 951, in send
self.connect()
File "/usr/local/lib/python3.8/http/client.py", line 1418, in connect
super().connect()
File "/usr/local/lib/python3.8/http/client.py", line 922, in connect
self.sock = self._create_connection(
File "/usr/local/lib/python3.8/socket.py", line 787, in create_connection
for res in getaddrinfo(host, port, 0, SOCK_STREAM):
File "/usr/local/lib/python3.8/socket.py", line 918, in getaddrinfo
for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution
During handling of the above exception, another exception occurred:
```


# ref
https://github.com/replicate/cog
and to code predict.py
https://github.com/replicate/cog/blob/main/docs/getting-started-own-model.md

# run
```bash
wget https://github.com/replicate/cog/releases/download/v0.7.2/cog_Linux_x86_64
mv cog_Linux_x86_64 cog
sudo mv cog /usr/local/bin/
```

# resnet18 setup
```
wget https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json
```

# as cog
```bash
cog predict -i @cup.jpg
cup
```

# as docker
```bash
cog build -t resnet18

docker run --rm -p 5000:5000 resnet18

curl  -X POST     -H 'Content-Type: application/json'  http://localhost:5000/predictions   -d '{"input": {"image":"https://dm0qx8t0i9gc9.cloudfront.net/watermarks/image/rDtN98Qoishumwih/tea-cup-drawing_z1mUGhnu_SB_PM.jpg"}}'

{...{"cup" ...}..}
```
