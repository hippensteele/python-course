import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open("./CPMC/FileIO/recipes.shelf") as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    
    ### append() modifies an in-memory copy of the list; the shelf is not modified
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    
    ### solution 1:
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

### solution 2:
### writeback option opens object in memory; nothing written back until closed or sync'd
### uses more memory, and can be slow on close or sync
### sync will clear the object in memory
with shelve.open("./CPMC/FileIO/recipes.shelf", writeback=True) as recipes:
    # recipes["soup"].append("croutons")
    
    for snack in recipes:
        print(snack, recipes[snack])