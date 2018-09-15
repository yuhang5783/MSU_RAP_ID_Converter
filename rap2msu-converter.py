relation={}
for i in open("RAP-MSU_2018-03-29.txt"):
        rap=str(i.split()[0])
        msu=str(i.split()[1])
        if rap!="None":
            relation[rap]=msu

for j in open("your-id-list-one-gene-per-line.txt"):
    id=j.strip()
    if id in relation.keys():
        if "," in relation[id]:
            s=relation[id].split(",")
            for a in s:
                print(id,a,sep="\t")
        else:
            print(id,relation[id],sep="\t")
    else:
        print(id,"None",sep="\t")


