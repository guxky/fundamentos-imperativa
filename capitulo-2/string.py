"""
2-3. Personal Message: Store a person’s name in a variable, and print a mes
sage to that person . Your message should be simple, such as, “Hello Eric, 
would you like to learn some Python today?”
"""
name = "samuel"
print("hello "+name+", would you like to learn python today?")

"""
2-4. Name Cases: Store a person’s name in a variable, and then print that per
son’s name in lowercase, uppercase, and titlecase
"""
print(name.lower())
print(name.upper())
print(name.title())

"""
2-5. Famous Quote: Find a quote from a famous person you admire . Print the 
quote and the name of its author . Your output should look something like the 
following, including the quotation marks:
Albert Einstein once said, “A person who never made a 
mistake never tried anything new.”
"""
print('Mon laferte once said, "cuando te diga que te voy a olvidar no me lo creas, por favro"')

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous per
son’s name in a variable called famous_person . Then compose your message 
and store it in a new variable called message . Print your message 
"""
author = "mon laferte"
quote = "Cuando te diga que te voy a olvidar No me lo creas, por favor"

print(author.title() + ' once said, "'+quote+'"')

"""
2-7. Stripping Names: Store a person’s name, and include some whitespace 
characters at the beginning and end of the name . Make sure you use each 
character combination, "\t" and "\n", at least once .
Print the name once, so the whitespace around the name is displayed . 
"""
name_2 = "\t\nsamuel\t\n"
print("nombre sin limpiar: " + name_2)
print("\nusando lstrip():"  + name_2.lstrip())
print("\nusando rlstrip():"  + name_2.rstrip())
print("\nusando strip():"  + name_2.strip())

