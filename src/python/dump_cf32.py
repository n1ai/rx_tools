import struct
import sys

while True:
    nbytes = sys.stdin.buffer.read(16)
    if len(nbytes) < 16:
        break
    f1, f2, f3, f4 = struct.unpack('ffff', nbytes)
    print("(%10.6f, %10.6f) (%10.6f, %10.6f)" % (f1,f2,f3,f4))

