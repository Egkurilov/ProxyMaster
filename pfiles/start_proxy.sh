#!/bin/bash
./proxy tcp -P "$1" -p ":$2" -T tcp --kcp-mode=fast3 --kcp-nocomp --daemon