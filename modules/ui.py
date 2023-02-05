from services.db import DB
from enum import Enum

class Operations(Enum):
    SESSIONS_NUMBER = "num_sessions"
    MEDIAN_SESSIONS_LENGTH = "median_session_length"
    NUM_UNIQUE_VISITED_SITES = "num_unique_visited_sites"

class UI:
    operations = [o.value for o in Operations]
    db = DB.get_instance()

    def init_ui(self):
        while True:
            try:
                user_input = input("\nPlease enter one of the operations - \n" + '\n'.join(self.operations) + "\n")
                if user_input == Operations.SESSIONS_NUMBER.value:
                    site_url = input("\nPlease insert site URL\n")
                    print("Num sessions for site www.s_1.com = " + self.db.get_num_of_sessions_by_site_url(site_url))
                elif user_input == Operations.MEDIAN_SESSIONS_LENGTH.value:
                    site_url = input("\nPlease insert site URL\n")
                    print("Median session length = " + self.db.get_sessions_length_median(site_url))
                elif user_input == Operations.NUM_UNIQUE_VISITED_SITES.value:
                    visitor_id = input("\nPlease insert visitor ID\n")
                    print("Num of unique sites for visitor = " + self.db.get_num_of_unique_visited_sites(visitor_id))
                elif user_input == "exit":
                    exit()
                else:
                    print("Invalid input. Try again.")
            except KeyError:
                print("Invalid input. Try again.")