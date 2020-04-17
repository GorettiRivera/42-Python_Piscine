
cookbook = {
    'sandwich':{'ingredients':['ham','bread','cheese','tomatoes'],'meal':'lunch','prep_time':10},
    'cake':{'ingredients':['flour','sugar','eggs'],'meal':'dessert','prep_time':60},
    'salad':{'ingredients':['avocado','arugula','tomatoes','spinach'],'meal':'lunch','prep_time':15}
}

def print_recipe(recipe):
    if recipe in cookbook:
        print(f'Recipe for {recipe}:')
        print(f'Ingredients list: {cookbook[recipe]["ingredients"]}')
        print(f'To be eaten for {cookbook[recipe]["meal"]}')
        print(f'Takes {cookbook[recipe]["prep_time"]} minutes of cooking\n')
    else:
        print("Please enter a valid recipe")

def del_recipe(recipe):
    if recipe in cookbook:
        print(f'The recipe {cookbook[recipe]} has been deleted\n')
        del cookbook[recipe]
    else:
        print("Please enter a valid recipe")

def add_recipe(recipe,ing,meal,time):
    cookbook[recipe] = {'ingredients':ing,'meal':meal,'prep_time':time}

def print_all():
    print('Recipes:')
    for r in cookbook:
        print(r)
    print("\n")

def cooking():
    print("Please select an option by typing the corresponding number:")
    
    try:
        select = int(input("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n"))
        if select == 1:
            add_recipe(input("Please entre the recipe name\n"),\
            input("Please enter the lists of ingredients\n"),\
            input("Please enter the meal\n"),\
            input("Please enter the time\n"))
        elif select == 2:
            del_recipe(input("What is the recipe you want to delete?\n"))
        elif select == 3:
            print_recipe(input("What is the repice you want to print?\n"))
        elif select == 4:
            print_all()
        elif select == 5:
            return
        else:
            print("Please enter a valid option")
    except ValueError:
        print("This option does not exist, please type the corresponding number\n.To exit, enter 5.")
    cooking()

cooking()