#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Author: JuanD Valenciano, jvalenciano@unal.edu.co
Date of creation: 2 Agust 2024
Project: ------------------
Target: ------------------
Compatibility:  ---------------------------

Comments:
    
"""

# #################################################################
# # Initialize serial communication with Arduino
# arduino_port = "COM8"  # Change this to your Arduino's port
# baud_rate = 9600
# ser = serial.Serial(arduino_port, baud_rate)

# # Initialize Pygame for playing MP3 files
# pygame.mixer.init()

# while True:
#     # Read data from serial port
#     if ser.in_waiting > 0:
#         data = ser.readline().decode().strip()
#         print("Received:", data)
        
#         # Check if the Arduino sent the "PLAY_MP3" signal
#         if data == "PLAY_MP3":
#             print("Playing MP3 file...")
#             pygame.mixer.music.load("./jammin.mp3")  # Replace "your_mp3_file.mp3" with the path to your MP3 file  | ##Jamming.mp3
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 continue  # Wait for the MP3 file to finish playing
# #################################################################

import serial
import pygame
import sys

def main():
    """
    :return:
    """
    if len(sys.argv) != 2:
        print("Error: Debe proporcionar exactamente un parámetro de entrada.")
        print("Uso: python paymp3.py COMX")
        print("Ejemplo: python paymp3.py COM8")
        return
    
    pygame.mixer.init()
    arduino_port = sys.argv[1]
    print(f"El puerto COM proporcionado es: {arduino_port}")
    baud_rate = 9600
    ser = serial.Serial(arduino_port, baud_rate)

    while True:
        # Read data from serial port
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print("Received:", data)
            # Check if the Arduino sent the "PLAY_MP3" signal
            if data == "PLAY_MP3":
                print("Playing MP3 file...")
                pygame.mixer.music.load("playlist/jamming.mp3")  # Replace "your_mp3_file.mp3" with the path to your MP3 file  | ##Jamming.mp3
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue  # Wait for the MP3 file to finish playing
                ser.flush    


if __name__ == "__main__":
    try:
        main()
    finally:
        print("...")
