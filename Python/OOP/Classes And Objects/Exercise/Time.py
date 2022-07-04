class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def get_time(self):
        output = ""
        
        if self.hours < 10:
            output += "0" + str(self.hours) + ":"
        else:
            output += str(self.hours) + ":"

        if self.minutes < 10:
            output += "0" + str(self.minutes) + ":"
        else:
            output += str(self.minutes) + ":"

        if self.seconds < 10:
            output += "0" + str(self.seconds)
        else:
            output += str(self.seconds)

        return output

    def next_second(self):
        self.seconds += 1

        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0

            if self.minutes > Time.max_minutes:
                self.hours += 1
                self.minutes = 0

                if self.hours > Time.max_hours:
                    self.hours = 0

        return self.get_time()



#Test codes


"""
time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
"""