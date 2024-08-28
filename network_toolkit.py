import os
import subprocess
import sys
import requests
import dns.resolver
import psutil
import speedtest

class NetworkToolkit:
    def __init__(self):
        self.geoip_api_url = "http://ip-api.com/json/"
        self.osint_api_url = "https://api.hackertarget.com/"
        self.anime_art = r"""
          /\\
         /__\\
        |    |
        |[O] [O]|
        |   ( )   |
        | (     ) |
        |_________|
        """
    
    def print_anime_intro(self):
        print(self.anime_art)
        print("Welcome to the Anime Network Toolkit! 🌟")

    def show_anime_girl(self):
        print(self.anime_art)
        print("Here’s your anime girl! 😍")

    def get_geolocation(self, ip_address):
        """Get geolocation for a given IP address."""
        try:
            response = requests.get(self.geoip_api_url + ip_address)
            data = response.json()
            return {
                "ip": data.get("query"),
                "city": data.get("city"),
                "region": data.get("regionName"),
                "country": data.get("country"),
                "isp": data.get("isp")
            }
        except Exception as e:
            return {"error": str(e)}

    def dns_lookup(self, domain):
        """Perform DNS lookup for a given domain."""
        try:
            answers = dns.resolver.resolve(domain, 'A')
            return [str(answer) for answer in answers]
        except Exception as e:
            return {"error": str(e)}
    
    def osint_email_search(self, email):
        """Perform OSINT email search using HackerTarget."""
        try:
            response = requests.get(self.osint_api_url + f"emailrecon?email={email}")
            return response.text
        except Exception as e:
            return {"error": str(e)}
    
    def check_network_bandwidth(self):
        """Check network bandwidth using speedtest."""
        st = speedtest.Speedtest()
        download_speed = st.download() / (10 ** 6)  # Convert to Mbps
        upload_speed = st.upload() / (10 ** 6)      # Convert to Mbps
        return {
            "download_speed_mbps": download_speed,
            "upload_speed_mbps": upload_speed
        }
    
    def get_system_specs(self):
        """Get system specifications."""
        specs = {
            "CPU": psutil.cpu_percent(interval=1),
            "Memory": psutil.virtual_memory().percent,
            "Disk": psutil.disk_usage('/').percent
        }
        return specs

    def install_requirements(self):
        """Check and install required packages."""
        required_packages = ['requests', 'dnspython', 'psutil', 'speedtest-cli']

        for package in required_packages:
            try:
                __import__(package)
                print(f"{package} is already installed.")
            except ImportError:
                print(f"{package} not found. Installing...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
if __name__ == "__main__":
    toolkit = NetworkToolkit()
    toolkit.install_requirements()  # Install requirements if necessary
    toolkit.print_anime_intro()
    
    while True:
        print("\nChoose an option:")
        print("1. Geolocation Lookup")
        print("2. DNS Lookup")
        print("3. OSINT Email Search")
        print("4. Check Network Bandwidth")
        print("5. Get System Specs")
        print("6. Show Anime Girl")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ip = input("Enter an IP address for geolocation: ")
            geo_info = toolkit.get_geolocation(ip)
            print("Geolocation Info:", geo_info)
            toolkit.show_anime_girl()

        elif choice == '2':
            domain = input("Enter a domain for DNS lookup: ")
            dns_info = toolkit.dns_lookup(domain)
            print("DNS Info:", dns_info)
            toolkit.show_anime_girl()

        elif choice == '3':
            email = input("Enter an email address for OSINT search: ")
            email_info = toolkit.osint_email_search(email)
            print("Email OSINT Info:", email_info)
            toolkit.show_anime_girl()

        elif choice == '4':
            print("Checking network bandwidth...")
            bandwidth_info = toolkit.check_network_bandwidth()
            print("Network Bandwidth (Mbps):", bandwidth_info)
            toolkit.show_anime_girl()

        elif choice == '5':
            print("Retrieving system specifications...")
            system_specs = toolkit.get_system_specs()
            print("System Specs:", system_specs)
            toolkit.show_anime_girl()

        elif choice == '6':
            toolkit.show_anime_girl()

        elif choice == '7':
            print("Exiting the toolkit. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

