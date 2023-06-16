class ValueError(Exception):
    pass

class FileNotFoundError(Exception):
    pass

class TypeError(Exception):
    pass

class DataValidator:
    
    def validate_input(self, data):
        
        if not data:
            raise ValueError("Input data is empty.")
        
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
    
    def process_data(self, data):
        self.validate_input(data)
    
    def save_data(self, data, filename):
        self.validate_input(data)
        
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string.")
        
class DataProcessor:
    
    def __init__(self):
        self.data_validator = DataValidator()
    
    def process_data(self, data):
        
        try:
            self.data_validator.process_data(data)
            print("Data processed successfully.")
            
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
    
    def save_data(self, data, filename):
        
        try:
            self.data_validator.save_data(data, filename)
            print(f"Data saved to '{filename}' successfully.")
        
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            
app = DataProcessor()

app.process_data([])  # Вызывает исключение ValueError
app.process_data("data")  # Вызывает исключение TypeError
app.save_data([1, 2, 3], "output.txt")
app.save_data([1, 2, 3], 123)  # Вызывает исключение TypeError