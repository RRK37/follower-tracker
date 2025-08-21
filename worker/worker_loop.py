# worker/worker_loop.py
import time
import subprocess
import os
import signal
import sys

SLEEP_SECONDS = 6 * 3600  # 6 hours

def run_once():
    # call your script directly; ensure Python path points to interpreter in container
    subprocess.run([sys.executable, "/app/get-followers.py"], check=False)

def main():
    while True:
        try:
            run_once()

        except Exception as e:
            print("Error running get-followers.py:", e)
        
        # sleep in small increments so container can respond to termination signals
        for _ in range(int(SLEEP_SECONDS/5)):
            time.sleep(5)

if __name__ == "__main__":
    main()
