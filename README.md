# Simple-Minecraft-launcher

A simple Minecraft launcher written in Python using minecraft-launcher-lib.

📌 Features
Download any Minecraft version
Launch the game directly from Python
Simple console-based interface
Custom nickname support
⚙️ Requirements

Install the required library:

pip install minecraft-launcher-lib

You also need:

Python 3.8 or higher
Internet connection (to download game files)
🚀 How to Run
Download or clone the project
Open a terminal in the project folder
Run:
python main.py
🎮 How to Use

After starting the program, it will ask you for:

Minecraft nickname – enter your username
Minecraft version – enter the version (example: 1.20.1)

Then the launcher will:

Download the required Minecraft files (if not installed)
Start the game automatically
📁 How It Works

Minecraft is installed to:

%APPDATA%\.minecraft

The launcher uses minecraft-launcher-lib to:

Install Minecraft versions
Generate the launch command
Start the game using Python’s subprocess
🧠 Code Overview

The program:

Takes user input (nickname and version)
Installs the selected Minecraft version
Builds the launch command
Runs Minecraft
⚠️ Notes
This is a basic launcher without Microsoft authentication
Works in offline mode only
Online play requires proper account authentication
📜 License

This project is for educational purposes.
