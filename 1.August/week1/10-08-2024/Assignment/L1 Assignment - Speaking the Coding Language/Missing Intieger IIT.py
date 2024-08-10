def find_missing_number(numbers):
  obj = {}
  for i in range(1, len(numbers) + 2):
    obj[i] = 0
  
  for i in range(len(numbers)):
    if numbers[i] in obj:
      del obj[numbers[i]]
  
  for key in obj:
    print(key)



