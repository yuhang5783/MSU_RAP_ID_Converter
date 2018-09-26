relation={}
for i in open("RAP-MSU_2018-03-29.txt"):
    rap=str(i.split()[0])
    msu=str(i.split()[1])
    if msu!="None":
        if "," in msu:
            for a in msu.split(","):
                relation[a[0:-2]] = rap
        else:
            relation[msu[0:-2]] = rap

# print header
print("MSU", "RAP", sep="\t")

for j in open("your-id-list-one-gene-per-line.txt"):
    id=j.strip()
    if id in relation.keys():
        print(id,relation[id],sep="\t")
    else:
        print(id,"None",sep="\t")

