import requests
import json
from colorama import Fore, Style
import sys  # For printing caught exceptions, if needed
import requests
import json
from colorama import Fore, Style



class PowerFleetAPIsManager:
    def __init__(self, dict_api_parameters):
        """
        Initialize the PowerFleet API manager with specific API parameters.

        :param dict_api_parameters: A dictionary containing API configuration including:
                                    - cid
                                    - api_key
                                    - url
                                    - plate (optional for live API)
        """
        self.PARAMETERS_REQUEST = dict_api_parameters
        self.CID = self.PARAMETERS_REQUEST["cid"]
        self.API_KEY = self.PARAMETERS_REQUEST["api_key"]

    def get_live_data(self):
        """
        Retrieves live vehicle data from the PowerFleet API.

        :return: JSON string of the response data or None if an error occurs.
        """
        print("**Live API**")

        url = self.PARAMETERS_REQUEST["url"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.API_KEY
        }
        params = {"plate": self.PARAMETERS_REQUEST.get("plate", "")}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            try:
                data = response.json()
                print(Fore.GREEN + "Live API Request Successful!" + Style.RESET_ALL)
                return json.dumps(data, indent=4)
            except ValueError:
                print(Fore.RED + "Failed to parse JSON response." + Style.RESET_ALL)
                print("Response Text:", response.text)
                return None

        except requests.exceptions.Timeout:
            print(Fore.RED + "Request timed out. Please try again later." + Style.RESET_ALL)
        except requests.exceptions.TooManyRedirects:
            print(Fore.RED + "Too many redirects. The URL might be incorrect." + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"An error occurred with the request: {e}" + Style.RESET_ALL)

        return None

    def get_snapshot_data(self, vehicleId, startDate, endDate):
        """
        Retrieves historical snapshot data for a specific vehicle from the PowerFleet API.

        :param vehicleId: ID of the vehicle
        :param startDate: Start date in "YYYY-MM-DD HH:MM:SS" format
        :param endDate: End date in "YYYY-MM-DD HH:MM:SS" format
        :return: JSON string of the response data or None if an error occurs.
        """
        # print(Fore.YELLOW + "**Snapshot API**" + Style.RESET_ALL)

        url = self.PARAMETERS_REQUEST["url"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.API_KEY
        }
        payload = {
            "vehicleId": vehicleId,
            "startDate": startDate,
            "endDate": endDate
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()

            try:
                data = response.json()
                if not data:
                    print(Fore.RED + f"Snapshot API:: VehicleId: {vehicleId} returned 0 records." + Style.RESET_ALL)
                    return -42 # !A value to highlight that there werent any data in DataBse on this vehicle ID
                else:
                    print(Fore.CYAN + f"Snapshot API:: VehicleId: {vehicleId} Request Successful!" + Style.RESET_ALL)
                    return json.dumps(data, indent=4)

            except ValueError:
                print(Fore.RED + "Failed to parse JSON response." + Style.RESET_ALL)
                print("Response Text:", response.text)
                return None

        except requests.exceptions.Timeout:
            print(Fore.RED + "Request timed out. Please try again later." + Style.RESET_ALL)
        except requests.exceptions.TooManyRedirects:
            print(Fore.RED + "Too many redirects. The URL might be incorrect." + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"An error occurred with the request: {e}" + Style.RESET_ALL)

        return None

