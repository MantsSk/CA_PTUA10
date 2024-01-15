class TimeUtils:
    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return (hours * 60 * 60) + (minutes * 60) + seconds

print(TimeUtils.time_to_seconds("01:30:00")) # Output: 5400
print(TimeUtils.time_to_seconds("12:30:00")) # Output: 45000
