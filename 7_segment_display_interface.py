import RPi.GPIO as GPIO
import time

# ------------------------------------------
#   PIN SETUP (avoiding GPIO 17 & 18)
# ------------------------------------------
SEGMENTS = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 14,
    'E': 15,
    'F': 23,
    'G': 24
    # 'DP': 25   # only if you use decimal point
}

# Digit → segments ON
DIGIT_MAP = {
    0: ['A','B','C','D','E','F'],
    1: ['B','C'],
    2: ['A','B','G','E','D'],
    3: ['A','B','C','D','G'],
    4: ['F','G','B','C'],
    5: ['A','F','G','C','D'],
    6: ['A','F','E','D','C','G'],
    7: ['A','B','C'],
    8: ['A','B','C','D','E','F','G'],
    9: ['A','B','C','D','F','G']
}

# ------------------------------------------
#   FUNCTIONS
# ------------------------------------------
def setup_segments():
    GPIO.setmode(GPIO.BCM)
    for pin in SEGMENTS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def clear_display():
    for pin in SEGMENTS.values():
        GPIO.output(pin, GPIO.LOW)

def display_digit(number):
    """Show a single digit (0–9) on the 7-seg display."""
    clear_display()

    if number not in DIGIT_MAP:
        return

    for seg in DIGIT_MAP[number]:
        GPIO.output(SEGMENTS[seg], GPIO.HIGH)

# ------------------------------------------
#   MAIN PROGRAM (Thonny loop)
# ------------------------------------------
setup_segments()

try:
    while True:
        for i in range(10):
            display_digit(i)
            print(i)
            time.sleep(1)

except KeyboardInterrupt:
    clear_display()
    GPIO.cleanup()
