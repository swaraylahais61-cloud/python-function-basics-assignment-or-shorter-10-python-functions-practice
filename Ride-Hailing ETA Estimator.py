#Ride-Hailing ETA Estimator
def estimate_arrival(distance_km, weather_condition):
    total_minutes = distance_km * 3
    if weather_condition == "rainy":
        total_minutes += 10
    return total_minutes


