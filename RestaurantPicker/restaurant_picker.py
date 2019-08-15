import random

Boca_restaurants = ['Sushi Yama', 'Boons', 'Las Espadas', 'Villa Rosano', 'Stallones', 'Five Guys', 
                        'Publix', 'Bolay', 'Shake Shack', 'Dominos', 'P.F. Changs', 'California Pizza Kitchen',
                        'Zinburger', 'Houstons', 'Ethos', 'Padrinos', 'Corner Bakery', 'Steves Wood Fire Pizza',
                        'Picanha Brazil', 'Grand Lux Cafe', 'Chipotle']

Winston_restaurants = ['Cugino Forno', 'Nawab', 'Chipotle', 'BJs', 'Five Guys', 'Panera', 'Cheddars', 'Mizu',
                            'Penny Path Cafe', 'Hakka Chow', 'Thai Harmony', 'Hickory Tavern', 'Village Tavern',
                            'Fratellis', 'Ryans', 'Publix','Midtown Cafe', 'Golden India', 'Quanto Basto',
                            'Cowboys Brazilian Buffet', 'Waffle House', 'Basil Leaf', 'Tacoriendo III', 'Mellow Mushroom',
                            'El Rancho Tacqueria', 'Dominos']

def main():
    rest_picker()

def rest_picker():
    print("Boca or Winston Restaurants?", end="\n")
    print("", end="\n")
    City_in = input()  
    print("", end="\n")
    
    if (City_in == 'Boca' or City_in == 'boca'):
        python_choice = random.choice(Boca_restaurants)
        print("Boca Restaurant to go to is '{0}'".format(python_choice))
        decider(Boca_restaurants)

    elif (City_in == 'Winston' or City_in == 'winston'):
        python_choice = random.choice(Winston_restaurants)
        print("Winston Restaurant to go to is '{0}'".format(python_choice))
        decider(Winston_restaurants)
    else:
        print('This script does not consider that city. Retype "Winston" or "Boca".')
    
def decider(City_in):
    pleased = False
    decide_another = input("Another random choice? Enter either 'y' or 'n': ")
    print("", end="\n")
    if decide_another == 'y':
        new_choice = random.choice(City_in)
        while not pleased:
            print("Another restaurant to go to is '{0}'".format(new_choice))
            decide_another = input("Another random choice? Enter either 'y' or 'n': ")
            print("", end="\n")        
            if decide_another == 'n':
                pleased = True
            else:
                new_choice = random.choice(City_in)

if __name__ == '__main__':
    main() 