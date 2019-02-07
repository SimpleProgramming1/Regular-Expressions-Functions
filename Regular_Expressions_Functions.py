

text = """Head southeast on W 56th St toward 8th Ave
0.2 mi

Turn right at the 3rd cross street onto 7th Ave Pass by Starbucks (on the right in 0.3 mi) 0.4 mi Turn left onto W 48th St
 Parts of this road may be closed at certain times or days
0.4 mi

Turn right onto 5th Ave 
Parts of this road may be closed at certain times or days
 Pass by Hop Lun (on the right in 0.7 mi)
1.9 mi

Turn right onto W 9th St
 Destination will be on the right
0.2 mi
9th Street"""


import re


# Split Function

route=re.split("\n",text)
print(route)


# Substitute function

route=re.sub("\n"," ",text)
print(route)

route=re.sub("\d.\d mi","\n",route)
print(route)


# Search function

route1=re.search("5th.+closed",route)
print(route1)


# Match function

re.match("Head",route)


# Findall Function

re.findall("Turn",route)




