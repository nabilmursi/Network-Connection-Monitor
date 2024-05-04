import subprocess
import sys

def check_installed(package_name):
    """Check if a Python package is already installed."""
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def install_package(package_name):
    """Install a Python package using pip if the user agrees."""
    user_input = input(f"{package_name} is not installed. Do you want to install it? (y/n): ").strip().lower()
    if user_input == 'y':
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"{package_name} installed successfully.")
    else:
        print(f"Installation of {package_name} skipped.")

def check_and_install_packages():
    """Check and manage the installation of required Python packages."""
    required_packages = ['requests', 'terminaltables']
    for package in required_packages:
        if check_installed(package):
            print(f"{package} is already installed.")
        else:
            install_package(package)

def install_iftop():
    """Check for iftop and offer to install it if not present."""
    if subprocess.run(["which", "iftop"], stdout=subprocess.PIPE).stdout.strip() == b'':
        print("iftop is not installed.")
        user_input = input("Do you want to install iftop? (y/n): ").strip().lower()
        if user_input == 'y':
            try:
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", "iftop"], check=True)
                print("iftop installed successfully.")
            except subprocess.CalledProcessError:
                print("Failed to install iftop. Please check your permissions and try again.")
        else:
            print("Installation of iftop skipped.")
    else:
        print("iftop is already installed.")

def install_dependencies():
    """Main function to manage the installation of dependencies."""
    check_and_install_packages()
    install_iftop()

if __name__ == "__main__":
    install_dependencies()
