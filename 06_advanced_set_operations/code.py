# USEFULNESS OF SETS

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
# Takes the friends set, and removes Abroad from it
print(local_friends)


local = {"Rolf"}
abroad2 = {"Bob", "Anne"}

friends2 = local.union(abroad2)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)