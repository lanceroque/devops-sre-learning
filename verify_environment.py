import os
import platform
import sys

print("Environment verification")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Operating system: {platform.platform()}")
print(f"APP_ENV: {os.getenv('APP_ENV', 'not set')}")