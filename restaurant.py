#CS175
#Christopher DeTullio
#restaurant
another_search = True
while another_search == True:
    vegetarian = False
    vegan = False
    gluten_free = False
    party_vegetarian = str(input("Is anyone in your party vegetarian? "))
    party_vegan = str(input("Is anyone in your party vegan? "))
    party_gluten_free = str(input("Is anyone in your party gluten-free? "))

    if party_vegetarian == "yes" or party_vegetarian == "Yes":
        vegetarian = True
    if party_vegan == "yes" or party_vegan == "Yes":
        vegan = True
    if party_gluten_free == "yes" or party_gluten_free == "Yes":
        gluten_free = True

    print("Here are your restaurant choices.")

    if vegetarian == False and vegan == False and gluten_free == False:
        print("Joe's Gourmet Burgers\nMama's Fine Italian\nMain Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif vegetarian == True and vegan == False and gluten_free == False:
        print("Mama's Fine Italian\nMain Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif vegetarian == False and vegan == False and gluten_free == True:
        print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif vegetarian == True and vegan == False and gluten_free == True:
        print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif vegetarian == False and vegan == True and gluten_free == False:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif vegetarian == False and vegan == True and gluten_free == True:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif vegetarian == True and vegan == True and gluten_free == False:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif vegetarian == True and vegan == True and gluten_free == True:
        print("Corner Cafe\nThe Chef's Kitchen")
    another_search = str(input("Enter yes if you would like to do another restaurant search (enter 'no' to end): "))
    if another_search == "yes":
        another_search = True
    elif another_search == "no":
        another_search = False
        

