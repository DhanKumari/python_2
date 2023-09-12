required_skills=['python','github','linux']

candidates={
    'kannu':{'java','linux','python'},
    'mustaf':{'github','java','html','css','python','linux'}
}

interviewees =set()
for candidate , skills in candidates.items():
    #if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)
        
print(interviewees)