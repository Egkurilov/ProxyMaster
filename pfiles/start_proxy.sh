 #!/bin/bash
proxy http -T tcp -p ":$1" -P "0.0.0.0:$2" --daemon --forever --log $3.log
