import json
import tempfile
import time
import os
from pathlib import Path
from invoke import task


@task
def erase(c, port):
    c.run(f"esptool.py --port {port} erase_flash")

@task
def flash(c, port):
    c.run(f"esptool.py --chip esp32 --port {port} write_flash -z 0x1000 esp32-20220618-v1.19.1.bin")

@task
def upload(c, port): 
    for path in Path('src').rglob('*'):
        dest_path = Path(*path.parts[1:])

        c.run(f"ampy --port {port} put {path} {dest_path}", echo=True)
    print("Done!")

@task 
def update(c, port, lamp): 
    c.run(f"ampy --port {port} put src/lamps/{lamp}.py lamps/{lamp}.py", echo=True)
    print("Done!")  