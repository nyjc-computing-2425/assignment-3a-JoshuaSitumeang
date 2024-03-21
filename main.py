nric = input('Enter an NRIC number: ')

# Type your code below

prefix = nric[0].upper()
valid = ('STFG')
if len(prefix) != 1:
  print('invalid_nric')
elif prefix.isalpha():
  print ('Prefix letter is valid')
else:
  print ('Prefix letter is invalid')

digits = nric[1:8]
valid = ('len(7)')
if len(digits) != 7:
  print('invalid_nric')
elif digits.isdigit():
  print('Digits are valid')
else:
  print ('Digits are invalid')

suffix = nric[8:].upper()
valid1 = ('JZIHGFEDCBA')
valid2 = ('XWUTRQPNMLK')
if len(suffix) != 1:
  print('invalid_nric')
elif suffix.isalpha():
  print ('Suffix letter is valid')
else:
  print ('Suffix letter is invalid')

invalid_nric = "NRIC is invalid."
valid_nric = "NRIC is valid."