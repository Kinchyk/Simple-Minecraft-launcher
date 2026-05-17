import minecraft_launcher_lib
import subprocess
import os

nickname = input("Enter your Minecraft nickname: ")

version = input("Enter the minecraft version:")

minecraft_directory = os.path.join(os.getenv("APPDATA"), ".minecraft")

minecraft_launcher_lib.install.install_minecraft_version(
    version,
    minecraft_directory
)

options = {
    "username": nickname,
    "uuid": "",
    "token": ""
}

minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
    version,
    minecraft_directory,
    options
)

subprocess.run(minecraft_command)
