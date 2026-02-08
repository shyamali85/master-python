#seasons stored in a tuple
seasons=("winter","spring","summer","autumn")

month=int(input("enter the month you want:"))
# December is considered the first of the Winter
season_index=(month % 12) // 3

print("seasons:", seasons[season_index])