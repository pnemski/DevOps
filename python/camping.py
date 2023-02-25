#Hey, we're going on a camping trip!!

#here is the stuff we need

#tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, flash drive, beard oil, marshmallows

#camping_stuff="tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, flash drive, beard oil, marshmallows"
#print(camping_stuff)
#Python List

camping_list=["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
#print(camping_list)

camp_site=["Crystal Lake", 404, 89.3, True]

#I will bring coffee

#me=camping_list[4]
#print(me)
#You will bring marshmallows

#you=camping_list[-1]
#print(you)

camping_list.append("toilet_paper")

#camping_list.append("bidet")
#camping_list.extend(["bidet", "toilet_paper"])

camping_list.insert(0, "bidet")

#camping_list.remove("tent")

#remove tent:
camping_list.pop(1)



print(camping_list)

