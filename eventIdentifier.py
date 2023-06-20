import sys
import time
import random
import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/aggar/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hey, someone has created,{event.src_path}")
    def on_moved(self,event):
        print(f"Someone has moved the file,{event.src_path} to {event.des_path}")
    def on_deleted(self,event):
        print(f"Alas!Someone deleted,{event.src_path}")
    def on_modified(self, event):
        print(f"Someone modified,{event.src_path}")

        
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()

