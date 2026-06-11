# Module 20 Lesson 6: After-Class Project
# Project Name: Logistical Transit Bottleneck Minimum Platform Calculator

def calculate_min_station_platforms(arrivals_list, departures_list):
    arrivals_list.sort(); departures_list.sort()
    platforms_active = peak_platforms_record = 0
    i = j = 0
    while i < len(arrivals_list) and j < len(departures_list):
        if arrivals_list[i] <= departures_list[j]:
            platforms_active += 1
            peak_platforms_record = max(peak_platforms_record, platforms_active)
            i += 1
        else:
            platforms_active -= 1
            j += 1
    return peak_platforms_record

if __name__ == "__main__":
    arr, dep = [900, 940, 950, 1100], [910, 1200, 1120, 1130]
    print(f"Minimum simultaneous runways tracks platforms required: {calculate_min_station_platforms(arr, dep)}")