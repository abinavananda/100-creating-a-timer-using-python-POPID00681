import time

def countdown_timer(duration):
    while duration > 0:
        print(f"Time left: {duration} seconds")
        time.sleep(1)  
        duration -= 1
    print("Time's up!")
duration = 10  
countdown_timer(duration)
