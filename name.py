from calculator import Calculator
from data_processor import DataProcessor

def main():
    calc = Calculator()
    processor = DataProcessor()

    numbers = [10, 0, 5, -3]

    print("=== Calculator Demo ===")
    for n in numbers:
        try:
            print(f"10 / {n} = {calc.divide(10, n)}")
        except Exception as e:
            print(f"Error: {e}")

    print("\n=== Data Processor Demo ===")
    data = ["hola", "", None, "VIU", "calidad"]
    print(processor.clean_data(data))

if __name__ == "__main__":
    main()
