#Binge-Watching Time Converter
def convert_minutes(number_of_episodes, duration_per_episode):
    total_minutes = number_of_episodes * duration_per_episode
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    return hours, remaining_minutes


