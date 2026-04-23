class Calculator:

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        # Error intencional: no se valida división por cero correctamente
        return a / b

    def multiply(self, a, b):
        # Code smell intencional: variable innecesaria
        result = a * b
        return result
