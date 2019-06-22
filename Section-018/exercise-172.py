'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(mylist):
    return [i for i in mylist if i]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))
