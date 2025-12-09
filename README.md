# **7 Segment Display Interface with Raspberry Pi 4B**

This project demonstrates how to interface a **single 7-segment LED display** with a **Raspberry Pi 4B** using Python and GPIO.
The script cycles through digits **0 to 9**, displaying each value for 1 second.

This is a great starter project for learning:

* How 7-segment displays work
* GPIO output control using Python
* Mapping number patterns to LED segments
* Clean hardware initialization & cleanup

The repo includes one Python script that handles the entire display logic.

---

## **1. Project Overview**

The Raspberry Pi controls each LED segment (A–G) of the 7-segment display directly.
To display any digit (0–9), the script activates only the required segments.

The program:

1. Initializes all GPIO pins for output
2. Defines segment mappings for all digits
3. Loops from **0 → 9**
4. Displays each digit for 1 second
5. Clears the display safely on exit

This is a clean, minimal implementation designed for learning and experimentation.

---

## **2. Hardware Requirements**

* Raspberry Pi 4B
* 1× Common Cathode 7-Segment Display
* 7× 220Ω–330Ω current-limiting resistors
* Breadboard + jumper wires

---

## **3. Wiring Guide**

### **3.1 Segment-to-GPIO Mapping (BCM mode)**

| Segment | GPIO |
| ------- | ---- |
| A       | 2    |
| B       | 3    |
| C       | 4    |
| D       | 14   |
| E       | 15   |
| F       | 23   |
| G       | 24   |

*(Decimal point “DP” can be added if needed.)*

**Common cathode pins → GND**
Each segment pin → resistor → GPIO pin

No buttons or inputs are used in this script.

---

## **4. How the Code Works**

### **4.1 Segment Setup**

```python
def setup_segments():
    GPIO.setmode(GPIO.BCM)
    for pin in SEGMENTS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
```

* Sets the Pi to BCM pin numbering
* Configures each segment pin as output
* Starts with display OFF

---

### **4.2 Digit Mapping**

Each number is represented by a list of segments to turn ON:

```python
DIGIT_MAP = {
    0: ['A','B','C','D','E','F'],
    1: ['B','C'],
    ...
    9: ['A','B','C','D','F','G']
}
```

For example:

* **'8'** uses all segments
* **'1'** uses only **B** and **C**

---

### **4.3 Displaying a Digit**

```python
def display_digit(number):
    clear_display()
    if number not in DIGIT_MAP:
        return
    for seg in DIGIT_MAP[number]:
        GPIO.output(SEGMENTS[seg], GPIO.HIGH)
```

Process:

1. Turn OFF all segments
2. Select digit pattern
3. Turn ON only required segments

---

### **4.4 Main Loop**

```python
while True:
    for i in range(10):
        display_digit(i)
        print(i)
        time.sleep(1)
```

* Cycles from **0 → 9**
* Displays each number for 1 second
* Prints value to console for debugging

On **Ctrl + C**, cleanup is handled:

```python
except KeyboardInterrupt:
    clear_display()
    GPIO.cleanup()
```

---

## **5. Running the Project**

### **Install dependencies**

```bash
sudo apt update
sudo apt install python3-rpi.gpio
```

### **Run the script**

```bash
sudo python3 7_segment_display_interface.py
```

You’ll see:

* Display cycling from **0 → 9**
* Each digit visible for one second

---

## **6. Optional Enhancements**

Future improvements you can add:

* Decimal point blinking
* Faster slideshow
* Button-controlled digit switching
* PWM dimming (brightness control)
* Multi-digit multiplexed display
* gpiozero rewrite for cleaner code

---

## **7. License**

This project is released under the **MIT License**.

---
