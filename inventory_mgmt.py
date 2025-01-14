#DS is {"item": num of that item}
inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inventory2 = {'hunting trap': 3, 'torch': 6, 'gold coin': 42069, 'dagger': 1, 'arrow': 12, 'longsword': 2}

def displayInventory(inventory):
    print("Inventory:")
    numItems = 0

    for i, n in inventory.items():
        numItems += n
        print(f"{n} {i}")

    print(f"Total number of items: {numItems}")

displayInventory(inventory1)
displayInventory(inventory2)