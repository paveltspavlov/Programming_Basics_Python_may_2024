record_in_seconds = float(input())
distance_in_meters = float(input())
time_IN_seconds_for_one_meter = float(input())

# slowing_down = distance_in_meters // 15 * 12.5

time_to_swim_the_distance = distance_in_meters * time_IN_seconds_for_one_meter

slowing_down = float((distance_in_meters // 15) * 12.5)

final_time = time_to_swim_the_distance + slowing_down

if final_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {final_time - record_in_seconds:.2f} seconds slower.")
