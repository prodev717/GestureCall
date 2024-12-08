# GestureCall

# Video Call Intercom Based on IP System with Vibration Sensor

## Project Overview

This project is a **hardware-software integrated solution** designed to facilitate communication between **deaf individuals and normal users**. It was developed as part of the **Engineering Clinics Course (ECS)** at **VIT-AP University** and addresses a **Smart India Hackathon (SIH)** problem statement.

The system enables **video calls** over a local network with **zero communication costs**, using a combination of hardware (Raspberry Pi) and Python-based software. It also features **sign language translation** and **speech-to-text functionality**, providing a seamless and inclusive communication platform.

---

## Features

### 1. **Video Call Functionality**
- Operates over a **local network (eth0/wlan)**.
- Devices communicate using static IPs through Python's socket library.
- Supports video calls between:
  - Devices designed for deaf individuals.
  - Regular desktops or other devices.

### 2. **Sign Language Translation**
- **Dataset and Mapping:**
  - Static gestures corresponding to 24 commonly used words (mapped to important phrases).
  - Each gesture represented by angles between hand landmarks, captured using Mediapipe.
  - All angles saved in a **Pickle file** for efficient retrieval.
- **Translation Process:**
  - Mediapipe processes real-time hand landmarks.
  - Angles are compared with the pre-trained dataset to identify gestures.
  - The corresponding word is displayed on the user interface.

### 3. **Speech-to-Text Conversion**
- Converts spoken words into text for better understanding, displayed on the UI.

### 4. **Hardware Integration**
- **Raspberry Pi 4** with:
  - XPT2046 5-inch touchscreen.
  - Camera module for video capture.
  - Vibration motor for incoming call alerts (triggered via GPIO).

### 5. **UI Design**
- Simple interface built with Tkinter.
- Displays a list of available devices in the network, retrieved from the server.

---

## How It Works

1. **Server Setup:**
   - A **FastAPI server** provides the list of connected devices, their names, and static IPs.

2. **Communication:**
   - Devices communicate using **socket programming**, exchanging video frames and other data.

3. **Gesture Recognition:**
   - Mediapipe detects hand landmarks.
   - Captured angles are compared to the **pre-trained dataset** stored in a Pickle file.
   - Recognized gestures are mapped to specific words and displayed on the screen.

4. **User Interaction:**
   - Devices display the list of connected devices on the UI.
   - Users select a device to initiate a video call.

5. **Alerts:**
   - Incoming calls trigger the **vibration motor**, notifying deaf users.

---

## Hardware Requirements

- **Raspberry Pi 4**
- **XPT2046 5-inch touchscreen**
- **Camera module**
- **Vibration motor**
- **Local network setup (Ethernet or WiFi)**

---

## Software Stack

- **Programming Language:** Python
- **Libraries and Tools:**
  - [FastAPI](https://fastapi.tiangolo.com/) (Server for managing devices in the network)
  - [OpenCV](https://opencv.org/) (Camera access for desktop)
  - [Mediapipe](https://mediapipe.dev/) (Hand gesture recognition)
  - [Tkinter](https://docs.python.org/3/library/tkinter.html) (UI for user interaction)
  - [Socket](https://docs.python.org/3/library/socket.html) (Local network communication)
  - GPIO (Vibration motor control for alerts)

---

## Acknowledgments

This project was developed as part of the **Engineering Clinics Course (ECS)** at **VIT-AP University** and addresses a **Smart India Hackathon (SIH)** problem statement.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
