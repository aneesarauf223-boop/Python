student_data = {'id1':
    {'name':['sara'],
     'class': ['v'],
    'Subject_Integration': ['english , math, science']
    },
    'id2':
    {'name': ['david'],  
     'class': ['v'],
    'subject_Intergration': ['english,math,science']
    },
    'id3':
    {'name':['sara'],
     'class': ['v'],
     'Subject_Intergration': ['english,math,science']
    },
    'id4':
    {'name': ['surya'],
     'class': ['v'],
     'Subject_Intergration': ['english,math,science']
    },
}
result =  {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)        
