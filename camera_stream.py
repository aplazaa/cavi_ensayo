import picamera
import socket
import RPi.GPIO as GPIO

# Camera settings
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

# Activate the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO_pin_list = [4]  # Choose the GPIO pins you want to use
for pin in GPIO_pin_list:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Socket settings
server_address = ('localhost', 8000)

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Accept an incoming connection
connection, address = sock.accept()

# Create a picamera.PiCamera object
camera = picamera.PiCamera()

# Start the camera preview
camera.start_preview()

while True:
    # Read a frame from the camera
    frame = camera.read()

    # Send the frame over the socket
    connection.sendall(frame)

    # Sleep for a short period of time to avoid overloading the network
    time.sleep(0.01)

# Stop the camera preview
camera.stop_preview()

# Close the socket
connection.close()

# Deactivate the GPIO pins
for pin in GPIO_pin_list:
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup(pin)
