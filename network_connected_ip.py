import curses
import subprocess
import requests
import time

def get_connected_ips():
    """Fetch connected IPs and their ports using netstat."""
    result = subprocess.run(['netstat', '-tn'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.split('\n')
    connections = []
    for line in lines:
        if 'ESTABLISHED' in line and ':' in line:
            parts = line.split()
            ip_port = parts[4]
            ip, port = ip_port.split(':')
            if ip != "127.0.0.1":
                connections.append((ip, port))
    return connections

def get_public_ip():
    """Fetch the public IP address using ipify API."""
    try:
        response = requests.get('https://ifconfig.me')
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException:
        return "Error fetching public IP"

def get_bandwidth_usage(interface='eth0'):
    """Calculate the server's bandwidth usage."""
    def read_bytes():
        with open(f"/sys/class/net/{interface}/statistics/tx_bytes", 'r') as f:
            tx_bytes = int(f.read())
        with open(f"/sys/class/net/{interface}/statistics/rx_bytes", 'r') as f:
            rx_bytes = int(f.read())
        return tx_bytes, rx_bytes

    tx1, rx1 = read_bytes()
    time.sleep(2)  # Delays for 2 seconds to get the rate
    tx2, rx2 = read_bytes()

    tx_rate = ((tx2 - tx1) * 8) / 1024 / 2  # Convert bytes to Kbps over 2 seconds
    rx_rate = ((rx2 - rx1) * 8) / 1024 / 2
    return tx_rate, rx_rate

def get_location(ip):
    """Get the geolocation of an IP using the ip-api.com service."""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            return f"{data['city']}, {data['country']}"
        else:
            return "Location Unknown"
    except Exception:
        return "Location Unknown"

def format_bandwidth(tx, rx):
    """Format bandwidth for display in Mbps or Kbps."""
    if tx >= 1024 or rx >= 1024:
        return f"TX: {tx / 1024:.2f} Mbps, RX: {rx / 1024:.2f} Mbps"
    else:
        return f"TX: {tx:.0f} Kbps, RX: {rx:.0f} Kbps"

def draw_menu(stdscr, current_row, connections, bandwidth):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    public_ip = get_public_ip()
    header_text = f"Server IP: {public_ip} | Total Bandwidth: {format_bandwidth(bandwidth[0], bandwidth[1])}"
    footer_text = "Press 'q' to quit, use arrow keys to scroll."

    # Draw header
    stdscr.addstr(0, 0, header_text, curses.A_REVERSE)
    stdscr.hline(1, 0, curses.ACS_HLINE, width)

    # Column titles with vertical separators
    title_format = "{:<18}|{:<7}|{:<27}|{:<20}"
    stdscr.addstr(2, 0, title_format.format("IP Address", "Port", "Location", "Bandwidth (TX/RX)"))
    stdscr.hline(3, 0, curses.ACS_HLINE, width)  # Horizontal line under titles

    # Draw connection lines
    for idx, conn in enumerate(connections):
        ip, port = conn
        location = get_location(ip)
        per_conn_tx, per_conn_rx = bandwidth[0] / len(connections), bandwidth[1] / len(connections)
        connection_string = title_format.format(ip, port, location, format_bandwidth(per_conn_tx, per_conn_rx))
        line_y = 4 + idx * 2  # Calculate line position
        stdscr.addstr(line_y, 0, connection_string)
        stdscr.hline(line_y + 1, 0, curses.ACS_HLINE, width)  # Horizontal line after each entry

    # Draw footer
    stdscr.hline(height - 2, 0, curses.ACS_HLINE, width)
    stdscr.addstr(height - 1, 0, footer_text, curses.A_REVERSE)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)  # Set getch() non-blocking
    current_row = 0
    while True:
        connections = get_connected_ips()
        bandwidth = get_bandwidth_usage()
        draw_menu(stdscr, current_row, connections, bandwidth)

        try:
            key = stdscr.getch()
            if key == curses.KEY_DOWN and current_row < len(connections) - 1:
                current_row += 1
            elif key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == ord('q'):
                break
        except curses.error:
            pass  # Ignore curses error due to no input

        time.sleep(2)  # Refresh rate of 2 seconds

if __name__ == "__main__":
    curses.wrapper(main)
