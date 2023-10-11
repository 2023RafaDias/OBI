x = ["7","3","2"]

x = sorted(x)

print(x)

join()
split()
strip()
format()
lower() upper()
replace()
find() index()
translate()

format_map()	Similar to format(), this function returns the formatted string after replacing specific values from the mapping in the string placeholders ‘{}’.
count()	Returns the number of occurrences of a specified string in another specified string.
startswith()	Returns True if the string starts with the specified string. If not, then the function will return False.
endswith()	Returns True if the string ends with the specified string. If not, then the function will return False.
capitalize()	This function capitalizes the string and returns it. If the string has uppercase letters, then this function will convert them into lowercase.
expandtabs()	We can control the number of whitespaces given by “\t” if it is present in the string.
center()	This function centers the string around specified characters of the specified size and returns the string.
__contains()	This function is from the Python String class and it can also be used to check if a string is present in another string.
isdigit()	Returns True if every character in the string is a digit. Returns False if that is not the case.
isalnum()	If the string is made of only alphanumeric characters, then this function will return True. Otherwise, it will return False.
isalpha()	If the string on which this function is called contains only alphabets then this function will return True.
False will be returned if the string is not entirely made up of alphabets.
isdecimal()	Returns True if every character in the string is a decimal. Returns False if that is not the case.
islower()	If the string only contains lowercase letters, then this function will return True. Otherwise, returns False.
isupper()	If the string only contains uppercase letters, then this function will return True. Otherwise, returns False.
isnumeric()	If the string only contains numeric characters, then this function will return True, else False.
isspace()	If the string on which this function is called only contains whitespaces, then the function will return True. The function will return False if that is not the case.
isprintable()	There are certain characters like “\n”, “\t”, etc., that are not printable.
If all the characters in the string are printable then this function will return True otherwise, False.
lsplit()	This function creates a left-justified version of the string and returns it.
rsplit()	This function creates a right-justified version of the string and returns it.
swapcase()	Returns a string where lowercase letters become uppercase and uppercase letters become lowercase.
title()	Returns a string after converting the first letter of the string to uppercase.
swapcase()	Returns a string where lowercase letters become uppercase and uppercase letters become lowercase.
istitle()	Returns True if the string is in the title case. Returns False otherwise.
rfind()	Returns the last position where the specified substring was found in the string.
zfill()	This function fills the string with a specific number of 0s at the beginning of that string.
rindex()	Returns the last position where the specified substring Python String Functions was found in the string.
splitlines()	This is just like the split() function, instead, it uses a new line as the delimiter to split the string.
This function returns a list of strings where each index of the list used to be a line in the original string.
partition()	This function returns a tuple where the string is split up into three parts.
maketrans()	The translation table is returned upon execution of this function. The translation table can be used in translations.
