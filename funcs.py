import json

async def get_inventory_data():
    with open("inventory.json","r") as f:
      users = json.load(f)

    return users

async def open_account(user):
  
  users = await get_inventory_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 250
    users[str(user.id)]["bank"] = 0
    users[str(user.id)]["multi"] = 1
    users[str(user.id)]["bankmax"] = 100
    users[str(user.id)]["premium"] = False

    users[str(user.id)]["cookie"] = 0
    users[str(user.id)]["pie"] = 0
    users[str(user.id)]["milk"] = 0
    users[str(user.id)]["egg"] = 0
    users[str(user.id)]["laptop"] = 0
    users[str(user.id)]["gun"] = 0 
    users[str(user.id)]["medal"] = 0
    users[str(user.id)]["coin"] = 0 
    
    #users[str(user.id)]["btc"] = 0 
    #users[str(user.id)]["apple"] = 0     
    #users[str(user.id)]["android"] = 0

  with open("inventory.json","w") as f:
    json.dump(users,f)
  return True

async def update_inventory(user,change = 0,target = "wallet", add = True):
  users = await get_inventory_data()

  if not add:
    change = change * -1
  
  users[str(user.id)][target] += change

  with open("inventory.json","w") as f:
    json.dump(users,f)
  return True

async def format_commas(amount = 0):
  formatted = "{:,}".format(amount)

  return formatted