def add_numbers(a=0, b=0):
    try:
        return a + b
    except Exception as e:   # It is for all kinf od errors
        print("Error:", e)
        return None



# Another function and somw other exceptions.
def divide_numbers(a, b):
  try:
      return a / b
  except ZeroDivisionError:   # it is for division errors
      print("Error: Division by zero is not allowed!")
      return None
  except TypeError:           # it is for type errors --- like int / str / 
      print("Error: Please provide only numbers!")
      return None
