def calculator():
  while True:
    expression = input("\nEnter your calculation(or type 'exit' to quit): ")
    if expression.lower() == "exit":
      break
    try:
      result=eval(expression)
      print("Result:", result)
    except ZeroDivisionError:
      print("Error! Division by zero.")
    except:
      print("Invalid expression! please try again.")
 calculator()
  
