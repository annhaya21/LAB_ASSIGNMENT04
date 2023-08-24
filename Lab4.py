class Match:
    def _init_(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def _init_(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        matching_matches = []
        for match in self.matches:
            if team_name in [match.team1, match.team2]:
                matching_matches.append(match)
        return matching_matches

    def list_matches_by_location(self, location):
        matching_matches = []
        for match in self.matches:
            if match.location == location:
                matching_matches.append(match)
        return matching_matches

    def list_matches_by_timing(self, timing):
        matching_matches = []
        for match in self.matches:
            if match.timing == timing:
                matching_matches.append(match)
        return matching_matches
print("NAME : ANJALI VERMA")
print("ROLL NO: E22CSEU1628")
def main():
    flight_table = FlightTable()

    flight_table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    flight_table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Choose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = input()
        
        if choice == '1':
            team_name = input("Enter the team name: ")
            matches = flight_table.list_matches_by_team(team_name)
        elif choice == '2':
            location = input("Enter the location: ")
            matches = flight_table.list_matches_by_location(location)
        elif choice == '3':
            timing = input("Enter the timing: ")
            matches = flight_table.list_matches_by_timing(timing)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose again.")
            continue
        
        print("Matching Matches:")
        for match in matches:
            print(f"Location: {match.location}, Team 1: {match.team1}, Team 2: {match.team2}, Timing: {match.timing}")
        print()


if __name__ == "__main__":
main()