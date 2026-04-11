print("Welcome to the Temperature Converter!")

while True:
    user_input = input("Enter temperature in Celsius (or type 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
        
   
    try:
        celsius = float(user_input)
        
       
        fahrenheit = (9/5) * celsius + 32
        kelvin = celsius + 273.15
        
        
        print(f"{celsius}°C  =  {fahrenheit:.1f}°F")
        print(f"{celsius}°C  =  {kelvin:.2f}K")
        print("-" * 25) 
        
    except ValueError:
        print("Please enter a valid number.")