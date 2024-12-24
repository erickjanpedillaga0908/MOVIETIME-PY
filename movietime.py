import collections
movies = collections.deque()
snacks = collections.deque()

#movies
x = 3;
for i in range(x):
    i += 1
    inp = input("Enter movie " + str(i) + " of " + str(x) + ": ")
    movies.append(inp)

#snax
for i in range(x):
    i += 1
    inp = input("Enter snack " + str(i) + " of " + str(x) + ": ")
    snacks.append(inp)

print("Movies to watch are: " + str(movies))  
print("Snacks to watch are: " + str(snacks))

#S
print("Press S each time you finish a snack. ")
z = 0;
while z < len(snacks):
    inp = input()
    
    if (inp.upper() == "S"):
        snacks.popleft()
        if len(snacks) == 0:
            print("No more snacks")
        else:
            print(str(snacks))

          

          