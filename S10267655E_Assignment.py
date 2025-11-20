#Tan Xin Yi(S10267655E) - CICTP05

# Game variables
import random
game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {},
}

seed_list = ['LET', 'POT', 'CAU']
seeds = {
    'LET': {'name': 'Lettuce',
            'price': 2,
            'growth_time': 2,
            'crop_price': 3
            },

    'POT': {'name': 'Potato',
            'price': 3,
            'growth_time': 3,
            'crop_price': 6
            },

    'CAU': {'name': 'Cauliflower',
            'price': 5,
            'growth_time': 6,
            'crop_price': 14
            },
}


farm = [ [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, 'House', None, None],
         [None, None, None, None, None],
         [None, None, None, None, None] ]

direction = {
    'a': [0, -1],
    'd': [0, 1],
    'w': [-1, 0],
    's': [1, 0]
}


action = {'w':'up',
          's':'down',
          'a':'left',
          'd':'right'}



position=[2,2] #reset position to 2,2


def in_town(game_vars):
    while True:
        show_stats(game_vars)
        print("You are in Albatross Town")
        print("-"*25)
        print("1) Visit Shop")
        print("2) Visit Farm")
        print("3) End Day")
        print()
        print("9) Save Game")
        print("0) Exit Game")
        print("-"*25)

        choice = input("Your choice? ").strip()
        if not choice.isdigit(): #validate input
            print("Invalid input.")
            continue

        choice= int(choice)

        if choice == 1: #visit shop
            in_shop(game_vars)
        elif choice == 2: #visit farm
            in_farm(farm,game_vars,position)
        elif choice == 3: #end day
            end_day(game_vars,farm)
            if game_vars["day"]==21: #check end game
                print(f"You have ${game_vars['money']} after 20 days.")
                if game_vars["money"]>=100:
                    print(f"You have paid off your debt of $100 and made a profit of ${game_vars['money']-100}") #ending game
                    print("You win!")
                else:
                    print("You did not pay off your debt, you lose :(")
                exit()
        elif choice == 9: #saving game
            save_game(game_vars,farm)
        elif choice == 0: #quit game
            confirm= input("Are you sure you want to quit? (Y/N)").upper()
            if confirm == "Y":
                print("Goodbye!")
                break
            else:
                continue
        else: #validate option
            print("Invalid option.")
    
    pass



def in_shop(game_vars):
    while True:
        total_seeds = sum(game_vars["bag"].values()) #total num of seeds in bag
        print()
        print("Welcome to pierce's shop!")
        show_stats(game_vars)
        print("What do you wish to buy?")
        print(f"{'Seed':<20}{'Price':^7}{'Days to Grow':^20}{'Crop Price':^20}")
        print("-"*62)

        index=1
        for item in seeds: #item = "LET" 
            if item=='LET':   #making sure that the crop price is reflected as a range
                price_sold = "2-5"
            elif item=='POT':
                price_sold= "5-8" #i set the range as (original price-1) to (original price+2)
            else:
                price_sold= "13-16"
            print(f" {index}) {seeds[item]['name']:15} {seeds[item]['price']:^5} {seeds[item]['growth_time']:^25} {price_sold:<15}") #printing seeds to buy
            index+=1
            
        print()
        print(" 0) Leave")
        print("-"*62)
        print()

        choice= input("Your choice? ").strip() #validate input
        if not choice.isdigit():
            print("Invalid input.")
            continue
        choice = int(choice)

        if choice == 0:
            print("Leaving shop...")
            break

        elif 0 < choice < index: 
            print(f"You have ${game_vars['money']}")
            quantity = input("How many do you wish to buy? ")

            if not quantity.isdigit() or quantity=="0": #validate input
                print("Invalid input.")
                continue
            
            quantity=int(quantity)

            if total_seeds >= 10: #check for current full bag
                print("Your bag is full. Purchase is rejected.")
                continue

            elif total_seeds+quantity > 10: #check if bag will be full
                print("Too many seeds. Your bag will be full, purchase rejected.")
                continue

            
            crop_index = seed_list[choice-1]  #"LET"
            price = int(seeds[crop_index]["price"])
            total_cost = quantity*price

            if game_vars["money"] >= total_cost:
                print(f"You have bought {quantity} {seeds[crop_index]['name']} seeds.")
                game_vars["money"]-= total_cost #minus off money spent
                game_vars['bag'][crop_index] = game_vars['bag'].get(crop_index, 0) + quantity #equate/add on to value of seed
            else:
                print("You can't afford that!") #if not enough money
        else:
            print("Invalid selection.")

        

def draw_farm(farm,position):
    
    print("+-----"*5+"+")
    for row_index in range(len(farm)):
        print ("|",end="")
        curr_col = farm[row_index]

        for col_index in range(len(curr_col)): #top row
            curr_space = farm[row_index][col_index]
            if curr_space is None: #if empty print blank,print house if house else print PLant
                print("     |",end="")
            elif curr_space=="House":
                print(" HSE |",end="")
            else:
                print(f" {curr_space[0]:<3} |",end="")
        
        print ("\n|",end="")
        for col_index in range(len(curr_col)):  #mid row
            if [row_index,col_index]==position: #print X if plot == position
                print ("  X  |",end="")
            else:
                print ("     |",end="")
            
        print ("\n|",end="")
        for col_index in range(len(curr_col)): #bottom row
            curr_space = farm[row_index][col_index]
            if curr_space is not None and curr_space != "House": #check if theres crops, if got, print no of days left till harvest
                print (f"{curr_space[1]:^5}|",end="")

            else:
                print ("     |",end="") #else print blank space
        print()
        print("+-----"*5 +"+")
    print()



def in_farm(farm,game_vars,position):
    draw_farm(farm,position)

    while True:
        current_plot = farm[position[0]][position[1]]

        print(f"Energy: {game_vars['energy']}")
        print("[WASD] Move")

        if position != [2,2]: #print Plant option for when on plot
            print("P)lant seed") 
        print("R)eturn to Town")

        if current_plot!=None and current_plot[1]== 0 and current_plot!="House": #print harvest only when can
            print(f"H)arvest crop for ${seeds[current_plot[0]]['crop_price']}")


        choice = input("Your choice? ").lower() 
        print()

        if game_vars["energy"] <=0 and choice != "r": #if energy is too low, user unable to do anything else
            print("You're too tired. You should return back to town.")
            draw_farm(farm,position)
            continue

        if choice in direction: #for moving
            move = direction[choice]
            new_position = [position[0]+move[0], position[1]+move[1]] #set new position

            if 0 <= new_position[0] < len(farm) and 0 <= new_position[1] < len(farm[0]): #checking new position if within range
                position = new_position #if within, update current position to new position
                game_vars["energy"] -=1
            else:
                print(f"You are not allowed to move {action[choice]}.")


            draw_farm(farm,position)


        elif choice == "p": #for planting
            if current_plot == "House":
                print("You can't plant at home.")
            elif current_plot != None:
                print("There's already something planted here!") #check if there is anything planted
                continue
        


            if not game_vars["bag"]: #check if got anyt to plant
                print("Your bag is empty.")
                draw_farm(farm,position)
                continue


            item_list = [] #reset item list
            print("-"*70)
            print(f"{'Seed':^15}{'Days to Grow':^20}{'Crop Price':^20}{'Available':^11}")
            print("-"*70)

            index = 1
            for item in game_vars["bag"]: #printing out menu inventory
                name = seeds[item]["name"]
                days = seeds[item]["growth_time"]
                if item =='LET':
                    crop_price = "2-5"
                elif item =='POT':
                    crop_price = "5-8"
                else:
                    crop_price = "13-16"
                qty = game_vars["bag"][item]
                print(f" {index}) {name:<12}{days:^20}{crop_price:^20}{qty:^11}") #printing out what is available for planting
                index += 1
                item_list.append(item) #add available to a list


            print()
            print(" 0) Leave")
            print("-"*70)
            print()

            plant_seed = input("Your choice? ")
            if not plant_seed.isdigit(): #validate input
                print("Invalid input.") 
                draw_farm(farm,position)
                continue
            plant_seed = int(plant_seed)
        
                
            print()
            if plant_seed == 0: #for leaving planting list
                print("Leaving planting inventory...")
                draw_farm(farm,position)
                continue
            if 0< plant_seed <= len(item_list):
                chosen = item_list[plant_seed-1] #find out which seed they chose
                farm[position[0]][position[1]] = [chosen, seeds[chosen]["growth_time"]] #planting the chosen item on farm
                game_vars["bag"][chosen] -= 1 #minus one from inventory
                if game_vars["bag"][chosen] == 0: #remove it from bag if none left
                    game_vars["bag"].pop(chosen) 
                game_vars["energy"] -= 1 
            else:
                print("Invalid seed selection.")

            draw_farm(farm, position)



        elif choice == "h": #for harvesting
            if current_plot is None or current_plot == "House": #ensure there's something on the plot to harvest
                print("There is no crop to harvest!")

            elif current_plot[1] != 0: #check if can harvest
                print("You cannot harvest it yet!")

            else:
                crop = current_plot[0] #get "code name" of crop
                name = seeds[crop]["name"] #full name of crop
                harvest_price = seeds[crop]["crop_price"]

                print(f"You have harvested {name} and sold it for ${harvest_price}") 

                game_vars['energy'] -= 1
                farm[position[0]][position[1]] = None #clear plot of land
                game_vars["money"] += harvest_price #earn money
                print(f"You now have ${game_vars['money']}!")
                draw_farm(farm,position)

        elif choice == "r": #for leaving farm
            print("Returning to town...")
            break

        else:
            print("Invalid action.") #validate input
            draw_farm(farm,position)
            continue



def show_stats(game_vars):
    print("+","-"*52,"+")
    day_string = f"Day {game_vars['day']}" #print "Day {}" etc Day 1
    energy_string = f"Energy {game_vars['energy']}"
    money_string = f"Money ${game_vars['money']}"
    
    print(f"| {day_string:<20}{energy_string:<20}{money_string:<12} |") 

    if not game_vars["bag"]: #check if bag is empty
        print(f"| {'You have no seeds.':<53}|")
    else:
        print("| Your seeds:"+" "*42+"|") #if not print items in bag
        for item in game_vars["bag"]:
            print(f"|  {seeds[item]['name']:<13}: {game_vars['bag'][item]:<37}|")
    print("+","-"*52,"+")
    print()
    pass



def end_day(game_vars,farm):
    game_vars["day"] += 1 #add on to day count
    game_vars["energy"] = 10 #resetting energy
    for row in farm:
            for item in row:
                if item is not None and item!= "House":
                    if item[1] > 0:
                        item[1] -= 1 #minus one day from planted crops
    seeds['LET']['crop_price']=random.randint(2, 5)
    seeds['POT']['crop_price']=random.randint(5, 8)
    seeds['CAU']['crop_price']=random.randint(13, 16) #randomnize the crop price for harvesting after each day

    pass



def save_game(game_vars, farm):
    with open("savegame.txt","w") as file:
        file.write(f"Day: {game_vars['day']}\n") #saving game variables
        file.write(f"Energy: {game_vars['energy']}\n")
        file.write(f"Money: {game_vars['money']}\n")
        file.write("Bag: ")
        for item in game_vars["bag"]: #saving seeds inventory
            file.write(f"{item},{game_vars['bag'][item]}#") #using hashtag instead to prevent conflict when separating

        file.write("\n") #start new line

        for row in farm: #saving farm data
            row_data = []
            for col in row:
                if col == None:
                    row_data.append('None') 
                else:
                    row_data.append(str(col)) #if not empty, append item
            file.write(';'.join(row_data) + '\n') #join items with ; and start new line when new row
        
    print("Game successfully saved!")
    pass



def load_game(game_vars, farm):
    try:
        with open("savegame.txt","r") as file:
            content=file.read().strip()
            if not content:
                raise ValueError("Save file is empty.")  #check if savegame.txt is empty
            file.seek(0) #return back to start of file

            day = energy = money = None #reset variables first
            seed_bag = {}
            farm_data = []
            for line in file:
                data = line.strip().split(":") #data is now "key,value"
                if len(data) == 2: #check for the game vars
                    key,value = data
                    if key == "Day": #set the variables according to saved
                        day = int(value)
                    elif key == "Energy":
                        energy = int(value)
                    elif key == "Money":
                        money = int(value)
                    elif key == "Bag": 
                        seedList = value.strip().split("#") #seperate diff seeds 
                        seedList.pop() #remove empty part after #
                        for seed in seedList:
                            seedvalues = seed.split(",")
                            name = seedvalues[0]
                            value = seedvalues[1]
                            seed_bag[name] = int(value) #add to new bag
                else:
                    row_data = line.strip().split(";") #loading farm data
                    row = []
                    for item in row_data:
                        item.strip()
                        if item == "None": #check if its empty plot
                            row.append(None)
                        elif item =="House": #check if its house
                            row.append(item)
                        else:
                            evaluated_item = eval(item) #changes "['LET',2]" to ['LET',2]
                            row.append(evaluated_item) 
                        
                    farm_data.append(row) 

            # update game variables and farm
            game_vars["day"] = day  
            game_vars["energy"] = energy
            game_vars["money"] = money
            game_vars["bag"] = seed_bag
            farm[:] = farm_data #overwrites current farm with saved one

            
        print("Game loaded successfully!")    
    except (FileNotFoundError,ValueError) as error: #if no file found or empty file
        print(f"Error loading game: {error}")
        print("Saved file could not be found. Starting a new game...")
        save_game(game_vars,farm) #starts new game if unable to load game
    pass

#----------------------------------------------------------------------
#    Main Game Loop
#----------------------------------------------------------------------

print("----------------------------------------------------------")
print("Welcome to Sundrop Farm!")
print()
print("You took out a loan to buy a small farm in Albatross Town.")
print("You have 20 days to pay off your debt of $100.")
print("You might even be able to make a little profit.")
print("How successful will you be?")
print("----------------------------------------------------------")

# Write your main game loop here

while True:  # Loop continues until user exits
    print("1) Start a new game")
    print("2) Load your saved game")
    print()
    print("0) Exit game")
    choice = input("Your choice? ")
    if not choice.isdigit(): #validate input
        print("Invalid input.")
        continue
    choice= int(choice)
    print()
    if choice == 1:
        in_town(game_vars) #enter new game
        break
    elif choice == 2:
        load_game(game_vars, farm) #load game then enter game
        in_town(game_vars)
        break
    elif choice == 0: #quit game
        print("Goodbye!")
        break
    else: #validate input
        print("Invalid choice.")





