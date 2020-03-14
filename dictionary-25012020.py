fruits = {"apple": "red",
          "banana": "yellow"}
print(fruits)


facts = dict()

# add a value
facts["cod"] = "funny"
# look up and print a key
print(facts["cod"])

# add a value
facts["Bill"] = "Gates"
# look up and print a key
print(facts["Bill"])

# add a value
facts["begin"] = 1998
# look up and print a key
print(facts["begin"])

print("cod" in facts)

a = "Ron" not in facts
print(a)

del facts["begin"]
print(facts)


exempl = {"1": "name",
          "2": "age",
          "3": "sex",
          "4": "weight",
          "5": "color"
}

n = input("Input a number ")
if n in exempl:
    ex = exempl[n]
    print(ex)
else:
    print("Not availible")
    
