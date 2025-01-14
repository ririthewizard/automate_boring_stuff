#List to dictionary
inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonInv = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

print(addToInventory(inventory1, dragonInv))