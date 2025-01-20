import time
import threading
import os
from datetime import timedelta

class AdvancedCountdownTimer:
    def __init__(self, duration):
        self.original_duration = duration  # Original duration in seconds
        self.remaining_time = duration
        self.running = False
        self.paused = False
        self.lock = threading.Lock()
    
    def start(self):
        self.running = True
        self.paused = False
        self._run_timer()

    def pause(self):
        with self.lock:
            self.paused = True
            print("\nTimer paused. Press 'r' to resume or 'x' to reset.")

    def resume(self):
        with self.lock:
            self.paused = False
            print("\nTimer resumed.")
            self._run_timer()

    def reset(self):
        with self.lock:
            self.running = False
            self.remaining_time = self.original_duration
            print("\nTimer reset. Press 's' to start again.")

    def _run_timer(self):
        while self.remaining_time > 0:
            if not self.running:
                break
            with self.lock:
                if not self.paused:
                    mins, secs = divmod(self.remaining_time, 60)
                    time_display = f"{mins:02}:{secs:02}"
                    print(f"\rRemaining Time: {time_display}", end="")
                    self.remaining_time -= 1
                else:
                    time.sleep(0.5)
                    continue
            time.sleep(1)

        if self.remaining_time == 0 and self.running:
            print("\nTime's up!")
            self._on_completion()

    def _on_completion(self):
        # Advanced action: Print message or trigger a notification
        print("Triggering on-completion event!")
        if os.name == 'posix':  # Linux/Unix/macOS
            os.system('notify-send "Countdown Complete!"')
        elif os.name == 'nt':  # Windows
            from win10toast import ToastNotifier
            notifier = ToastNotifier()
            notifier.show_toast("Countdown Timer", "Countdown Complete!", duration=5)

# Interactive Controls
def interactive_timer(duration):
    timer = AdvancedCountdownTimer(duration)
    print("Countdown Timer initialized. Controls: ")
    print("s: Start | p: Pause | r: Resume | x: Reset | q: Quit")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == 's':
            threading.Thread(target=timer.start, daemon=True).start()
        elif command == 'p':
            timer.pause()
        elif command == 'r':
            timer.resume()
        elif command == 'x':
            timer.reset()
        elif command == 'q':
            timer.running = False
            print("Exiting timer. Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

# Example: Start with a 1-minute countdown
if __name__ == "__main__":
    interactive_timer(60)