#!/bin/bash

export LD_PRELOAD="./libstdc ./libc"
gdbserver 0.0.0.0:1234 ./binary
