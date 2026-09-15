from machine import Pin
from time import sleep

# -------------------------
# Pins
# -------------------------

entry_button = Pin(18, Pin.IN, Pin.PULL_UP)
exit_button = Pin(19, Pin.IN, Pin.PULL_UP)

green_led = Pin(25, Pin.OUT)
red_led = Pin(26, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
blue_led = Pin(14, Pin.OUT)

# -------------------------
# Garage settings
# -------------------------

car_count = 0
MAX_CARS = 15


# -------------------------
# Update garage LEDs
# -------------------------

def update_garage_status():

    if car_count < MAX_CARS:
        green_led.on()
        red_led.off()
    else:
        green_led.off()
        red_led.on()


# -------------------------
# Start status
# -------------------------

update_garage_status()

print("Smart Garage Started")
print("Cars:", car_count)


# -------------------------
# Main Loop
# -------------------------

while True:

    # Car entering
    if entry_button.value() == 0:

        if car_count < MAX_CARS:
            car_count += 1

            print("Car Entered")
            print("Cars:", car_count)

            # Yellow LED blink
            yellow_led.on()
            sleep(0.5)
            yellow_led.off()

            update_garage_status()

        # Wait until button is released
        while entry_button.value() == 0:
            sleep(0.05)


    # Car exiting
    if exit_button.value() == 0:

        if car_count > 0:
            car_count -= 1

            print("Car Exited")
            print("Cars:", car_count)

            # Blue LED blink
            blue_led.on()
            sleep(0.5)
            blue_led.off()

            update_garage_status()

        # Wait until button is released
        while exit_button.value() == 0:
            sleep(0.05)


    sleep(0.05)