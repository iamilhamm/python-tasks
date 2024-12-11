weather_data = {
    "Alger": {
        "temperature": "20°C", "conditions": "Cloudy", 
        "wind_speed": "5 km/h", "humidity": "80%"
    },
    "Oran": {
        "temperature": "20°C", "conditions": "Sunny", 
        "wind_speed": "9 km/h", "humidity": "69%"
    },
    "Taghit": {
        "temperature": "18°C", "conditions": "Rainy", 
        "wind_speed": "5 km/h", "humidity": "90%"
    },
    "Djanet": {
        "temperature": "19°C", "conditions": "Sunny", 
        "wind_speed": "14 km/h", "humidity": "21%"
    },
    "Sidi Bel abbes": {
        "temperature": "17°C", "conditions": "Foggy", 
        "wind_speed": "3 km/h", "humidity": "85%"
    }
}

def welcome_message():
    print("Hello and Welcome to the Weather Forecast!")

def display_weather(city): 

    if weather_data:
        
        print(f"Weather Forecast for {city}:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Conditions: {weather_data['conditions']}")
        print(f"Wind Speed: {weather_data['wind_speed']}")
        print(f"Humidity: {weather_data['humidity']}")
    else:
    
        print(f"Sorry, we dont have information on {city}. Please try again.")

def main():
    welcome_message() 
    
    while True:

        city = input("Enter the name of the city you want the weather forecast for: ").strip()

        
        if city in weather_data:
            display_weather(city)  
            break
        else:
            print("Please enter a valid city name from the list.")
    
    print("Thank you for using the Weather Forecast Application!")

    if __name__ == "__main__":
        main()

