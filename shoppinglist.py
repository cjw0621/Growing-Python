class ShoppingList:

    def __init__(self):
        self.shopping_list_dict = {}

    def shopping_list(self, add_item_to_list):
    	"""
    	Adds items i to users shopping list
    	"""
    	if add_item_to_list not in self.shopping_list_dict:
            try:
                while True:
                    print("--" * 25)
                    item_quantity = int(input("How many units would you like to add to {}?\n".format(add_item_to_list)))
                    print("--" * 25)
                    try:
                        self.shopping_list_dict[add_item_to_list] = "{0}{1}".format("x", item_quantity)
                        print("{} was added to your shopping list".format(add_item_to_list))
                        print("--" * 25)
                        ShoppingList.u_i_transition(self)
                        break

                    except ValueError:
                        print("--" * 25)
                        print("Please enter a number")
                        continue
                print("--" * 25)

            except KeyError:
                print("Item already in list")

    def u_i_transition(self):
    	"""
    	Transitions from intial start to the main program body
    	"""
    	while True:
            print("--" * 25)
            user_input = str(input("Type an item you would like to add to your list\nType help to view commands\n").capitalize())
            print("--" * 25)

            if user_input == "View":
                print("--" * 25)
                print("Shopping List:")
                for k, v in self.shopping_list_dict.items():
                    print(k, ":", v)
                print("--" * 25)
                continue
                
            elif user_input == "Del":
                while True:
                    u_i = input("What would you like to remove from your shopping list?\n").capitalize()
                    if u_i in self.shopping_list_dict:
                        del self.shopping_list_dict[u_i]
                        print("--" * 25)
                        print("{} has been removed from your shopping list".format(u_i))
                        break
                    else:
                        print("Item is not in your shopping list")
                        self.u_i_transition()
                        
            elif user_input == "Edit":
                """
                Edits users shopping list
                -displays the users current shopping list 
                -asks user which item they want to edit               
                """
                for k, v in self.shopping_list_dict.items():
                    print(k, ":", v)
                print("--" * 25)
                u_i_1 = input("Which item would you like to edit?\n").capitalize()
                print("--" * 25)
                while True:
                    """
                    Checks to make sure user enters an integer 
                    Throws up exception if input is 
                                           
                     Checks to make sure user inputs a value thats in their shopping list
                     throws up an exception if user inputs an invalid value
                        """
                    if u_i_1 in self.shopping_list_dict:
                        u_i_2 = int(input("How many units of {0} would you like instead?\n".format(u_i_1)))
                        print("--" * 25)
                        try:
                            self.shopping_list_dict[u_i_1] = "{0}{1}".format("x", u_i_2)
                            print("Shopping list updated")
                            print("-" * 25)
                            break
                        except ValueError:
                            print("Please enter a number")
                            print("--" * 25)
                            continue                       
                    else:
                    	print("{} was not found in your shopping list".format(u_i_1))
                    	print("--" * 25)
                    	u_i_3 = input("Would you like to add it to your shopping list?").capitalize()
                    	if u_i_3 == "Yes":
                    		self.shopping_list(u_i_1)
                    		
                    	elif u_i_3 == "No":
                    		self.u_i_transition()
                    		
                    	else:
                    		print("Invalid response")
                    		
            elif user_input == "Help":
            	print("Type View to view your shopping list.\nType Edit to edit your item quantity.\nType Del to remove an item from your shopping list.")

            else:                
                if user_input in self.shopping_list_dict:
                	print("It looks like you already added {} to your shopping list".format(user_input))
                	
                else:                	
                    ShoppingList.shopping_list(self, user_input)


if __name__ == "__main__":
    
    start = ShoppingList()
    start_list = input("What would you like to add to your shopping list?\n").capitalize()
    start.shopping_list(start_list)
