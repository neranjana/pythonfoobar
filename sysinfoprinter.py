import math
import os
import platform
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")


# Get general system information
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")