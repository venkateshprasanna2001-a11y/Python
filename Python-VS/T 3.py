print("OEE CALCULATOR")

shift_time = 480 # in minutes

breakedown_time = float(input("Enter breakdown time (min): "))
setup_time = float(input("Enter setup time (min): "))
idle_time = float(input("Enter idle time (min): "))

downtime = breakedown_time + setup_time + idle_time
runningtime = shift_time - downtime

availability = runningtime / shift_time

idle_rate = float(input("Enter idle rate (parts/hour): "))
acutal_production = float(input("Enter output (parts): "))
running_time_hours = runningtime / 60

idle_output = idle_rate * running_time_hours

performance = acutal_production / idle_output

good_parts = float(input("Enter good parts produced: "))
total_parts = acutal_production

quaility = good_parts / total_parts

oee = availability * performance * quaility

print("Availability:", availability*100, "%")
print("Performance:", performance*100, "%")
print("Quality:", quaility*100, "%")
print("OEE:", oee*100, "%")