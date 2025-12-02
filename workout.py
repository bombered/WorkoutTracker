class Workout:
    """Namespace for workout tracking functionality"""
    
    class Tracker:
        def __init__(self):
            self.workouts = []
        
        def add_workout(self, date, exercise, duration, intensity):
            """Add a new workout to the tracker"""
            workout = {
                'date': date,
                'exercise': exercise,
                'duration': duration,  # in minutes
                'intensity': intensity  # low, medium, high
            }
            self.workouts.append(workout)
        
        def get_workouts(self, date=None):
            """Retrieve workouts, optionally filtered by date"""
            if date:
                return [w for w in self.workouts if w['date'] == date]
            return self.workouts
        
        def total_duration(self):
            """Calculate total workout duration"""
            return sum(w['duration'] for w in self.workouts)


if __name__ == "__main__":
    tracker = Workout.Tracker()
    tracker.add_workout("2024-01-15", "Running", 30, "high")
    tracker.add_workout("2024-01-16", "Yoga", 45, "low")
    
    print(f"Total workouts: {len(tracker.workouts)}")
    print(f"Total duration: {tracker.total_duration()} minutes")