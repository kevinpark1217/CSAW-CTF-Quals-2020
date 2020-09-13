#!/usr/bin/env python3
from base64 import b64decode
import blacklist  # you don't get to see this :p

"""
Don't worry, if you break out of this fd, we have another fd underneath so that you won't
wreak any havoc!
"""

def main():
    print("EduPy 3.8.2")
    while True:
        try:
            command = input(">>> ")
            if any([x in command for x in blacklist.BLACKLIST]):
                raise Exception("not allowed!!")

            final_cmd = """
fd = open("sandbox.py", "r")
one = int(((54 * 8) / 16) * (1/3) - 8)
first_line = fd.readlines()[one].strip().split(" ")
str_base64 = first_line[one]
str_b64decode = first_line[-one]
fd.close()
func_b64decode = getattr(__import__(str_base64), str_b64decode)
numpy = __builtins__.__dict__[func_b64decode(b'X19pbXBvcnRfXw==').decode('utf-8')](func_b64decode(b'bnVtcHk=').decode('utf-8'))\n""" + command
            exec(final_cmd)

            # func_b64decode(b'X19pbXBvcnRfXw==').decode('utf-8')
            # '__import__'

            # func_b64decode(b'bnVtcHk=').decode('utf-8')
            # 'numpy'

            # __builtins__.__dict__['__import__']('numpy')
            # numpy module

            # 
            # ['__builtins__', '__import__', 'eval', 'exec', 'import', 'from', 'os', 'sys', 'system', 'timeit', 'base64commands', 'subprocess', 'pty', 'platform', 'open', 'read', 'write', 'dir', 'type']

        except (KeyboardInterrupt, EOFError):
            return 0
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    exit(main())
