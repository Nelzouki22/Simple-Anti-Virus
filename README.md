# Simple Anti Virus
Overview
This project is a simple antivirus system built using Python. The goal of the project is to teach how basic antivirus mechanisms work, such as monitoring file changes in real-time to detect suspicious activities. It is an educational project that demonstrates how viruses might behave and how antivirus software can potentially mitigate them.

Features
Real-time file system monitoring using watchdog.
Detects and logs changes to files such as creation, modification, and deletion.
Colored output in the terminal for better visibility of events.
Can be extended to include other antivirus techniques like scanning files for known signatures, detecting malicious behavior, etc.
Installation
Clone this repository:
bash
git clone https://github.com/Nelzouki22/Antivirus-Project.git
Navigate to the project folder:
bash
cd Antivirus-Project
Install the required dependencies:
bash
pip install -r requirements.txt
You will need colorama and watchdog for terminal colors and file monitoring.
Run the project:
bash
python antivirus.py
Usage
The antivirus project monitors a specified directory for any changes such as file creation, modification, or deletion. You can configure the directory by changing the path variable in the antivirus.py file.

How It Works
File Monitoring: It uses the watchdog library to observe the file system.
Color-Coded Alerts: It provides color-coded outputs for different events like:
Green for file creation
Yellow for file modification
Red for file deletion
Educational Purpose
This project is meant for educational purposes only. It helps students understand how basic virus-like behavior can be identified and how antivirus tools are built to counter these actions.

Future Enhancements
Adding a file scanning feature for known malicious signatures.
Detecting and stopping suspicious application behavior.
Adding more complex malware detection algorithms.
Contact Information
Email: elzoukigroup2018@gmail.com

LinkedIn: [Nadir Elzouki](https://www.linkedin.com/in/nadir-elzouki-40679a1a9/)

YouTube: [Nadir Elzouki](https://www.youtube.com/@nadirelzouki4529)
Youtube: https://youtu.be/mRDX0OJRd1g
GitHub: Nelzouki22
