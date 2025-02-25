class Activity:
    def __init__(self, date, activity_type, duration, calories_burned):
        self.date = date
        self.activity_type = activity_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"Date: {self.date}, Activity: {self.activity_type}, Duration: {self.duration} mins, Calories Burned: {self.calories_burned} kcal"

class FitnessTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self, date, activity_type, duration, calories_burned):
        activity = Activity(date, activity_type, duration, calories_burned)
        self.activities.append(activity)

    def view_activities(self):
        if not self.activities:
            print("No activities available.")
            return
        for activity in self.activities:
            print(activity)

    def remove_activity(self, date):
        self.activities = [activity for activity in self.activities if activity.date != date]

# Example usage
fitness_tracker = FitnessTracker()
fitness_tracker.add_activity("2025-02-24", "Running", 30, 300)
fitness_tracker.add_activity("2025-02-25", "Cycling", 45, 400)

print("Current Activities:")
fitness_tracker.view_activities()

print("\nRemoving activity for '2025-02-24'")
fitness_tracker.remove_activity("2025-02-24")

print("\nUpdated Activities:")
fitness_tracker.view_activities()