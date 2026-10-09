students={
    101:{"Name":"Aditi", "Scores":[20,20,25]},
    102:{"Name":"rahul", "Scores":[45,60,79]},
    101:{"Name":"sneha", "Scores":[85,95,99]},
    101:{"Name":"karan", "Scores":[79,96,96]},
    101:{"Name":"priya", "Scores":[65,85,43]},
}

#calculate avr score and flag p/f
for sid, details in students.items():
    avg = sum(details["Scores"])/len(details["Scores"])
    details["Average"]= avg
    details["Passed"]= avg>=30 #Boolean flag
    
#ptint names of students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])