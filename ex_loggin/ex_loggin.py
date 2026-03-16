import logging

logger = logging.getLogger("converter_system")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_of_handler = logging.FileHandler('converter_system.log') 
    file_of_handler.setFormatter(formatter)
    logger.addHandler(file_of_handler)


def convert_to_celsius(fahrenheit):
    logger.debug(f"Converting {fahrenheit} to celsius")
    celsius = (fahrenheit - 32) * 5.0/9.0
    logger.debug(f"Result of conversion: {celsius}")
    return celsius

def start_app():
    logger.info("Temperature Converter App started")

    while True:
        fahrenheit = input("Please enter the temperature in fahrenheit: ")

        try:
            fahrenheit = float(fahrenheit)
            if fahrenheit < -459.67:
                logger.warning("Temperature cannot be less than absolute zero")
                print("Temperature cannot be less than absolute zero. Please try again.")
                continue
            break
        except ValueError:
                logger.error(f"Invaild input: {fahrenheit}")
                print("Invalid input.")

    celsius = convert_to_celsius(fahrenheit)
    print(f"The temperature in Celsius is: {celsius:.2f}")