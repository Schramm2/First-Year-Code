#Reference Formatter
#2022/03/23
#Matthew Schramm

reference = input("Enter the reference:\n")

authors = reference[0:reference.find("(")]

year = reference[reference.find("("):reference.find(")")+1]

title = reference[reference.find(")")+2: reference.find(",",reference.find(")"))]

otherInfo = reference[reference.find(",",len(authors+year + title)):len(reference)]

authors = authors.lower()
name1 = authors[0:authors.find(",")].capitalize()
name2 = authors[authors.find(",")+2:authors.find(" ",authors.find(",")+2):].capitalize()
name3 = authors[authors.find(" ",authors.find(",")+2)+1:len(authors)].capitalize()

authors = name1 +", "+ name2 +" "+ name3
title = title.lower()
title = title.capitalize()



print("Reformatted reference:\n",authors,year," ",title,otherInfo, sep = "")