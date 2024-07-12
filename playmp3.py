import serial
import pygame

# Initialize serial communication with Arduino
arduino_port = "COM8"  # Change this to your Arduino's port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

# Initialize Pygame for playing MP3 files
pygame.mixer.init()

while True:
    # Read data from serial port
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print("Received:", data)
        
        # Check if the Arduino sent the "PLAY_MP3" signal
        if data == "PLAY_MP3":
            print("Playing MP3 file...")
            pygame.mixer.music.load("./jammin.mp3")  # Replace "your_mp3_file.mp3" with the path to your MP3 file
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue  # Wait for the MP3 file to finish playing
