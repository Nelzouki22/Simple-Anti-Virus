import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class MyHandler(FileSystemEventHandler):
    """
    Event handler for monitoring changes in the file system.
    Logs when files are modified, created, or deleted.
    """
    def on_modified(self, event):
        logging.info(f'File modified: {event.src_path}')

    def on_created(self, event):
        logging.info(f'File created: {event.src_path}')

    def on_deleted(self, event):
        logging.info(f'File deleted: {event.src_path}')

if __name__ == "__main__":
    # Specify the folder you want to monitor (make sure to use double backslashes or raw string)
    path = r"C:\Users\Famliy\source\repos\Replicates Itself VIRUS\Replicates Itself VIRUS"

    # Initialize event handler and observer
    event_handler = MyHandler()
    observer = Observer()
    
    # Schedule observer to monitor the specified path, recursive=True means it will monitor subdirectories as well
    observer.schedule(event_handler, path, recursive=True)

    # Start the observer
    observer.start()
    logging.info(f'Monitoring changes in: {path}')

    try:
        # Keep the script running to monitor changes
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer if the script is interrupted (Ctrl + C)
        logging.info("Monitoring stopped.")
        observer.stop()

    # Wait until the thread is fully stopped
    observer.join()
pip insta