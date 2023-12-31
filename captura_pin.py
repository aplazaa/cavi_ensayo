#!/usr/bin/python


import time
import picamera2
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
gpio_pin = 4  # Example GPIO pin, replace with your own pin
GPIO.setup(gpio_pin, GPIO.OUT)

# Function to take a picture
def take_picture():
    with picamera2.PiCamera() as camera:
        camera.resolution = (640, 480)  # Set desired resolution
        camera.start_preview()
        time.sleep(2)  # Warm-up time
        filename = 'image_' + time.strftime('%Y%m%d%H%M%S') + '.jpg'  # Generate filename
        camera.capture(filename)
        camera.stop_preview()
        print(f"Picture taken: {filename}")

# Main loop
while True:
    try:
        # Take a picture
        take_picture()

        # Toggle GPIO pin
        GPIO.output(gpio_pin, GPIO.HIGH)  # Example GPIO pin, replace with your own pin
        time.sleep(1)  # Keep the pin high for 1 second
        GPIO.output(gpio_pin, GPIO.LOW)  # Example GPIO pin, replace with your own pin

        # Wait for 5 minutes
        time.sleep(300)
    except KeyboardInterrupt:
        break

# Clean up GPIO
GPIO.cleanup()
