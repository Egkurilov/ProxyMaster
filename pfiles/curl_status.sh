#!/bin/bash
while true
do
    curl -sb -H http://127.0.0.1:8000/check_all_proxy_status/
    sleep 10
done