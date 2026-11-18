"""
Project 114: Countdown Timer & Stopwatch with Split Laps
Concepts: time module, terminal flushing, format strings, delta calculation.
"""
import time
import sys

def run_countdown(seconds):
    print(f"Starting countdown from {seconds} seconds...")
    for s in range(seconds, -1, -1):
        mins, secs = divmod(s, 60)
        sys.stdout.write(f"\rTime Remaining: {mins:02d}:{secs:02d} ")
        sys.stdout.flush()
        if s > 0:
            time.sleep(1)
    print("\n[ALARM] Time is up! Ding ding ding!\n")

def run_stopwatch():
    print("\nStopwatch Mode:")
    print("Press ENTER to record lap / Press 'q' then ENTER to stop.")
    input("Press ENTER to start...")
    start_time = time.time()
    last_lap = start_time
    lap_num = 1

    while True:
        val = input()
        if val.strip().lower() == 'q':
            total = time.time() - start_time
            print(f"Stopwatch stopped. Total Elapsed: {total:.2f} seconds.")
            break
        now = time.time()
        lap_time = now - last_lap
        total_time = now - start_time
        print(f"Lap {lap_num}: +{lap_time:.2f}s (Total: {total_time:.2f}s)")
        last_lap = now
        lap_num += 1

def main():
    while True:
        print("=== TIME TOOL ===")
        print("1. Countdown Timer")
        print("2. Stopwatch & Laps")
        print("3. Exit")
        c = input("Choice (1-3): ").strip()
        if c == "1":
            secs = int(input("Seconds to count down: ") or 10)
            run_countdown(secs)
        elif c == "2":
            run_stopwatch()
        elif c == "3":
            break

if __name__ == "__main__":
    main()
