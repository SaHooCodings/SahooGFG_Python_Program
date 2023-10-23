#if-else Approach
def combo_string(a, b):
  
  # your code here
  if len(a) < len(b):
      short = a
      longer = b
  elif len(a) > len(b):
      short = b
      longer = a
  return short+longer+short



#Ternary Approach
def combo_string(a, b):
  
  # your code here
  short = a if(len(a) < len(b)) else b
  longer = b if(len(b) > len(a)) else a
  return short+longer+short
