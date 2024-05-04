# Network Connection Monitor

`network_connected_ip.py` is a Python script designed to monitor and display network connections, bandwidth usage, and the geolocation of connected IPs in real-time. It utilizes a text-based user interface (TUI) built with the curses library, making it suitable for deployment on servers and systems where graphical user interfaces are not preferred.

## Features

- **Real-time Monitoring:**
  - Tracks live network connections, displaying the IP address, port, location, and bandwidth usage.
  - Provides insights into communication between different IP addresses.

- **Dynamic Bandwidth Calculation:**
  - Shows bandwidth in either Kbps or Mbps, automatically adjusting based on the scale of the traffic.

- **Geolocation Information:**
  - Retrieves the geographic location (city, country) of each connected IP using the ip-api.com service.

- **Non-blocking Interface:**
  - Updates information every 2 seconds without user interaction.
  - Still responds to user input for navigation and exit commands.

## Dependencies

Make sure you have the following dependencies installed:

- Python 3.x
- curses module (standard with Python for Unix-like systems)
- requests library for HTTP requests
- terminaltables library for formatting tables

## Installation

1. **Clone the Repository:**
   - Begin by cloning the repository to your local machine or server:
     ```
     git clone https://github.com/nabilmursi/network-monitor.git
     cd network-monitor
     ```

2. **Run the Installation Script:**
   - Execute the installation script `network_tools_setup.py` included in the repository to set up necessary Python packages and dependencies:
     ```
     sudo python3 network_tools_setup.py
     ```
   - This script will check for and install required Python packages (requests, terminaltables) and the `iftop` network monitoring tool.

3. **Python and Pip:**
   - If manually installing, ensure that Python 3 and pip are installed:
     ```
     sudo apt update
     sudo apt install python3 python3-pip
     ```

4. **Install Required Python Libraries:**
   - If the automatic script did not run or additional packages are needed, install the necessary Python packages using pip:
     ```
     pip3 install requests terminaltables
     ```

5. **Install iftop (optional):**
   - The script may require the `iftop` network monitoring tool. If not installed, the installation script will prompt you to install it:
     ```
     sudo apt-get install iftop
     ```

6. **Setting up Permissions:**
   - Ensure the script has executable permissions and that Python has access to read system network statistics:
     ```
     sudo chmod +x network_connected_ip.py
     ```

## Usage

To run the `network_connected_ip.py` script, use the following command:

sudo python3 network_connected_ip.py


This will launch the interface in your terminal. Use the arrow keys to navigate through the connections if they exceed one page, and press 'q' to quit the application.

## Troubleshooting

- **Permission Issues:**
  - Ensure the script has executable permissions and that Python has access to read system network statistics.
- **Dependency Errors:**
  - Verify all required packages are installed (requests, terminaltables). If errors persist, try reinstalling the packages.

## Contributing

Contributions to the project are welcome! If you'd like to contribute, follow these steps:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add my feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a Pull Request.

Feel free to customize this README for your specific project. Happy monitoring! 🚀

