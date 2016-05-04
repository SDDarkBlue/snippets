from collections import defaultdict
groupedByTerrein = defaultdict(list)
for loc in meetlocaties:
    groupedByTerrein[loc["terreincode"]].append(loc["code"])

newdict = [{"terrein":k, "meetlocaties":v} for k,v in groupedByTerrein.items()]
for loc in newdict:
    if loc["terrein"] == "AKM2":
	print loc["meetlocaties"]
