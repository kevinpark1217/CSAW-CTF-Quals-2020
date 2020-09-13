#!/bin/bash

export LD_PRELOAD="./libc"
gdbserver 0.0.0.0:1234 ./binary
