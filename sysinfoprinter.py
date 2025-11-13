import platform
from datetime import datetime

print(f"Current date and time: {datetime.now()}")

print(f"System: {platform.system()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")