#ways to merge and update dictionaries
# merge(|) update(|=)


dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged_dict=dict1 | dict2#used when merging w/o modifying the original dicts and creating a new dict
print(merged_dict)

dict1|=dict2#Updates the left-hand dictionary in place
print(dict1)


#| merges two dictionaries into a new one.
#|= updates a dictionary in place with another dictionary.