import argparse
import time
parser = argparse.ArgumentParser()
parser.add_argument("timeout", help="Run a task for this many seconds",
                    type=int)
parser.add_argument("message", help="Repeat this message",
                    type=str)
args = parser.parse_args()

for i in range(args.timeout):
    time.sleep(1)
    print(f"Been running task for {i} seconds... Repeating message: {args.message}", flush=True)
print("Finished running task!")

