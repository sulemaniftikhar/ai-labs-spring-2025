class CarMaintenanceChecker:
    def __init__(self):
        # dictionary to store issue weights
        self.issue_weights = {
            "Engine noise": 4,
            "Check engine light": 5,
            "Poor fuel efficiency": 3,
            "Strange vibrations": 3,
            "Difficulty starting": 4,
            "Braking issues": 5,
            "Unusual exhaust smoke": 4,
            "Steering problems": 3
        }
        # threshold for maintenance
        self.threshold = 15

    def ask_user_about_issues(self):
        # initialize total score
        total_score = 0

        print("Please answer the following questions with 'Yes' (1) or 'No' (0):")
        for issue, weight in self.issue_weights.items():
            response = input(f"Are you experiencing {issue.lower()}? (Yes = 1, No = 0): ").strip()
            if response == "1":
                total_score += weight

        return total_score

    def determine_maintenance(self, total_score):
        # determine if maintenance is needed
        if total_score > self.threshold:
            print("\nBased on the issues reported, your car may require maintenance. "
                  "It is recommended to visit a mechanic for a thorough inspection.")
        else:
            print("\nBased on the issues reported, your car does not seem to require immediate maintenance. "
                  "\nHowever, if you are concerned, consulting a mechanic is always a good idea.")

    def run(self):
        total_score = self.ask_user_about_issues()
        self.determine_maintenance(total_score)


if __name__ == "__main__":
    car_checker = CarMaintenanceChecker()
    car_checker.run()
