# shopping_list = ("milk","pasta","eggs","spam","soup","bread","rice","beans")
# for item in shopping_list:
#     if item == "spam":
#         continue
#     elif item == "bread":
#         break
#     print("Buy "+item)

meal = ("cereal","soymilk","apples","wasSpam","bananas","walnuts","almonds","yogurt","oranges")
for item in meal:
    if item == "Spam":
        foundSpam = True
        break;
else: # 'else' here executes if the for-loop was not broken out of
    foundSpam = False
    print("Let's eat!")
if foundSpam:
    print("Can't I have a meal without Spam?")