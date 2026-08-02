"""
3-1. Names: Store the names of a few of your friends in a list called names . Print 
each person’s name by accessing each element in the list, one at a time 
"""
names = ["Samuel", "Valeria", "Juan Esteban", "Santiago", "Emmanuel", "Steven", "Manuela", "Sebastian Rubio", "Sebastian Calvo", "Juan Jose"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[7])
print(names[8])
print(names[9])

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them . The text of each mes
sage should be the same, but each message should be personalized with the 
person’s name 
"""
message = "es un peludinchis de corazon"
print( names[0] + message)
print( names[1] + message)
print( names[2] + message )
print( names[3] + message)
print( names[4] + message)
print( names[5] + message)
print( names[6] + message)
print( names[7] + message)
print( names[8] + message)
print( names[9] +message)

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner . Then use your list to print a message to each person, inviting 
them to dinner 
"""
people = ["Valeria", "Manuela", "Emmanuel", "Aura","Lina"]
dinner_message = ", queria invitarte a comer :D"
print("Hola "+people[0]+dinner_message)
print("Hola "+people[1]+dinner_message)
print("Hola "+people[2]+dinner_message)
print("Hola "+people[3]+dinner_message)
print("Hola "+people[4]+dinner_message)

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations . You’ll have to think of 
someone else to invite .
•	Start with your program from Exercise 3-4 . Add a print statement at the 
end of your program stating the name of the guest who can’t make it .
•	Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting .
•	Print a second set of invitation messages, one for each person who is still 
in your list 
"""

print(people[4])
people[4] = "Ana Sofia"
print("Hola "+people[0]+dinner_message)
print("Hola "+people[1]+dinner_message)
print("Hola "+people[2]+dinner_message)
print("Hola "+people[3]+dinner_message)
print("Hola "+people[4]+dinner_message)

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is 
available . Think of three more guests to invite to dinner .
•	Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print 
statement to the end of your program informing people that you found a 
bigger dinner table .
•	Use insert() to add one new guest to the beginning of your list .
•	Use insert() to add one new guest to the middle of your list .
•	Use append() to add one new guest to the end of your list .
•	Print a new set of invitation messages, one for each person in your list
"""
print(people)
people.insert(0, "Juan Jose")
people.insert(3, "Sebastian Rubio")
people.append("Steven")
print(people)

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests .
•	Start with your program from Exercise 3-6 . Add a new line that prints a 
message saying that you can invite only two people for dinner .
•	Use pop() to remove guests from your list one at a time until only two 
names remain in your list . Each time you pop a name from your list, print 
a message to that person letting them know you’re sorry you can’t invite 
them to dinner .
•	Print a message to each of the two people still on your list, letting them 
know they’re still invited .
•	Use del to remove the last two names from your list, so you have an empty 
list . Print your list to make sure you actually have an empty list at the end 
of your program 
"""
print("Que pena muchachos al final solo puedo invitar a dos JAJAJA")
print("Perdon "+ people.pop() +" ya no puedes venir que pena")
print("Perdon "+ people.pop() +" ya no puedes venir que pena")
print("Perdon "+ people.pop() +" ya no puedes venir que pena")
print("Perdon "+ people.pop() +" ya no puedes venir que pena")
print("Perdon "+ people.pop() +" ya no puedes venir que pena")
print("Perdon "+ people.pop() +" ya no puedes venir que pena")
print(people)
del people[0]
del people[0]
print(people)

"""
3-8. Seeing the World: Think of at least five places in the world you’d like to 
visit .
•	Store the locations in a list . Make sure the list is not in alphabetical order .
•	Print your list in its original order . Don’t worry about printing the list neatly, 
just print it as a raw Python list .
•	Use sorted() to print your list in alphabetical order without modifying the 
actual list .
•	Show that your list is still in its original order by printing it .
•	Use sorted() to print your list in reverse alphabetical order without chang
ing the order of the original list .
•	Show that your list is still in its original order by printing it again .
•	Use reverse() to change the order of your list . Print the list to show that its 
order has changed .
•	Use reverse() to change the order of your list again . Print the list to show 
it’s back to its original order .
•	Use sort() to change your list so it’s stored in alphabetical order . Print the 
list to show that its order has been changed .
•	Use sort() to change your list so it’s stored in reverse alphabetical order . 
Print the list to show that its order has changed
"""

places = ["España", "Brasil", "Japon", "Medellin", "Londres"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
through 3-7 (page 46), use len() to print a message indicating the number 
of people you are inviting to dinner 
"""

print(len(people))
