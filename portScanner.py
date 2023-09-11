import socket
import sys
from datetime import datetime as dt

target = "127.0.0.1"
if (len(sys.argv) == 2):
  target = socket.gethostbyname(sys.argv[1])
else:
  print("Invalid Arguement")
  print("python3 portScanner.py <IP>")
  sys.exit()

print("-" * 50)
print(f"Target: {target}")
print(f"Starting Port Scanner At Time: {dt.now()}")
print("-" * 50)
count = 0

try:
  for port in range(50, 85):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if(result == 0):
      print(f"CONNECTION ON PORT: {port}")
      count += 1
    else:
      s.close()

except KeyboardInterrupt:
  print("\nExiting Program")
  sys.exit()

except socket.gaierror:
  print("\nHost Name could not be resolved, try again")
  sys.exit()

except socket.error:
  print("\nCannot Connect to Address")
  sys.exit()

print(f"Port Scan Complete, {count} port found open")