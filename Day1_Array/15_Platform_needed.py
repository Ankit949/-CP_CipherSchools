def PlatformNeeded(arrival, departure) :
    arrival.sort()
    departure.sort()
    n=len(arrival)
    platform = 1
    platform_count = 1
    i = 1
    j = 0
    while (i < n and j < n):

        if (arrival[i] <= departure[j]):
            platform += 1
            i += 1
        elif (arrival[i] > departure[j]):
            platform -= 1
            j += 1
        if (platform > platform_count):
            platform_count = platform
    return platform_count

if __name__=="__main__":
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    print(PlatformNeeded(arrival, departure))

