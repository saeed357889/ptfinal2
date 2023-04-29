import random as r

workouts = {
    "Bicep": ["Dumbbell bicep curls", "Barbell bicep curls", "Hammer curls", "Preacher curls", "Concentration curls", "Reverse curls", "Chin-ups", "Close-grip chin-ups", "Incline dumbbell curls", "Cable curls"],
    "Triceps": ["Close-grip bench press", "Dips", "Triceps pushdowns", "Skull crushers", "Overhead triceps extensions", "Narrow push-ups", "Diamond push-ups", "Close-grip push-ups", "Cable triceps extensions", "Bench dips"],
    "Shoulders" :["Barbell Overhead Press","Dumbbell Overhead Press","Landmine Press","Arnold Press","Bottoms-Up Kettlebell Press","Banded Delt Raise"],
    "Chest": ["Benchpress","Flat Bench Barbell Press", "Flat Bench Dumbbell Press","Incline Bench Barbell Press","Decline Bench Barbell Press","Decline Bench Dumbbell Press","Decline Bench Dumbbell Fly", "Flat Bench Dumbbell Fly","Dips","Push-up"],
    "Legs": ["BACK SQUATS ", "Front squats ","Romanian deadlifts ","Good mornings","walking lunges","Reverse lunge ", "Lateral lunge ","Hip thrusts","Bulgarian split squat ","Single leg deadlifts "],
    "Cardio": ["Jumping rope", "Sprints", "Stair running", "Hill sprints", "Stationary bike"],
    "CORE": ["Plank", "Russian twist", "Bicycle crunches", "Swiss ball crunches", "Hanging leg raises", "Dead Bug", "Side Plank", "Reverse Crunch", "Medicine Ball Slams", "Windshield Wipers"],
    "PLYOMETRICS": ["Jumping jacks", "Jump squats", "Tuck jumps", "Box jumps", "Lateral bounds", "Single-leg bounds", "Depth jumps", "Skater jumps", "Split squat jumps", "Plyometric push-ups", "Burpees", "Medicine ball slams", "Cone jumps", "Dot drills", "High knees"],
    "BACK": ["Barbell rows", "Pull-ups", "Lat pulldowns", "Seated cable rows", "Face pulls", "Dumbbell rows", "Single-arm rows", "Bent-over rows", "Back extensions"],
    "Agility": ["Suicides", "Ladder drills", "Cone drills", "Shuttle runs", "Side shuffles", "Defensive slides"],
}
reps = {
    "Bicep":["Low weight 10-12 reps X 3 sets", "Middle weight 8-10 reps X 3 sets", "High weight 6-8 reps X 3 sets "],
    "Triceps":["Low weight 10-12 reps X 3 sets", "Middle weight 8-10 reps X 3 sets", "High weight 6-8 reps X 3 sets "],
    "Shoulders":["Low weight 10-12 reps X 3 sets", "Middle weight 8-10 reps X 3 sets", "High weight 6-8 reps X 3 sets "],
    "Chest":["Low weight 8-10 reps X 3 sets", "Middle weight 6-8 reps X 3 sets", "High weight 2-5 reps X 3 sets "],
    "Legs":["Low weight 10-12 reps X 3 sets", "Middle weight 8-10 reps X 3 sets", "High weight 6-8 reps X 3 sets "],
    "PLYOMETRICS":["8-12 reps X 3 sets"],
    "BACK":["Low weight 10-12 reps X 3 sets", "Middle weight 8-10 reps X 3 sets", "High weight 6-8 reps X 3 sets "],
    "Agility":["1.5mins-4mins X 3 sets"],
    "CORE":['30 seconds - 2.5 minutes X 3 sets ']


}

def routines(level):
    if level == "beginner":
        x=0
    elif level == "intermediate":
        x=1
    elif level == "pro":
        x=2
    
    EP= {}
    print('Select your position')
    position=input()
    if position== 'Shooting Guard':
        EP['Day 1: Upper Body']=[workouts["Bicep"][r.randint(0, len(workouts["Bicep"])-1)]+': '+ reps["Bicep"][x],workouts["Triceps"][r.randint(0, len(workouts["Triceps"])-1)]+': '+ reps["Triceps"][x],workouts["BACK"][r.randint(0, len(workouts["BACK"])-1)]+': '+ reps["BACK"][x],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)]+': '+ reps["Shoulders"][x],workouts["Chest"][r.randint(0, len(workouts["Chest"])-1)]+': '+ reps["Chest"][x],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0]]
        EP['Day 2: Lower Body and Plyometrics']=[workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0]]
        EP['Day 3: Agility and Cardio']=[workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)]]
        file = open("workoutprogram.txt","w")
        for key,value in EP.items():
            file.write(f'{key}\n')
            file.write('\n')
            for v in value:
               file.write(f'{v}\n') 
               file.write('\n\n\n')
         
    elif position=='Point Guard':
        EP['Day 1: Upper Body']=[workouts["BACK"][r.randint(0, len(workouts["BACK"])-1)]+': '+ reps["BACK"][x],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)]+': '+ reps["Shoulders"][x],workouts["Chest"][r.randint(0, len(workouts["Chest"])-1)]+': '+ reps["Chest"][x],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0]]
        EP['Day 2: Lower Body and Plyometrics']=[workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0]]
        EP['Day 3: Agility and Cardio']=[workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)]]
        file = open("workoutprogram.txt","w")
        for key,value in EP.items():
            file.write(f'{key}\n')
            file.write('\n')
            for v in value:
               file.write(f'{v}\n') 
               file.write('\n\n\n')
    elif position=='Small Forward':
        EP['Day 1: Full Body Strength ']=[workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Bicep"][r.randint(0, len(workouts["Bicep"])-1)]+': '+ reps["Bicep"][x],workouts["Triceps"][r.randint(0, len(workouts["Triceps"])-1)]+': '+ reps["Triceps"][x],workouts["BACK"][r.randint(0, len(workouts["BACK"])-1)]+': '+ reps["BACK"][x],workouts["Chest"][r.randint(0, len(workouts["Chest"])-1)]+': '+ reps["Chest"][x],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0]]
        EP['Day 2: Plyometrics and Agility']= [workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0]]
        EP['Day 3: Cardio']= [workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)]]
        file = open("workoutprogram.txt","w")
        for key,value in EP.items():
            file.write(f'{key}\n')
            file.write('\n')
            for v in value:
               file.write(f'{v}\n') 
               file.write('\n\n\n')
    elif position == 'Power Forward':
         EP['Day 1: Full Body Strength ']=[workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Bicep"][r.randint(0, len(workouts["Bicep"])-1)]+': '+ reps["Bicep"][x],workouts["Triceps"][r.randint(0, len(workouts["Triceps"])-1)]+': '+ reps["Triceps"][x],workouts["BACK"][r.randint(0, len(workouts["BACK"])-1)]+': '+ reps["BACK"][x],workouts["Chest"][r.randint(0, len(workouts["Chest"])-1)]+': '+ reps["Chest"][x],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)]+': '+ reps["Shoulders"][x],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)+': '+ reps["Shoulders"][x]]]
         EP['Day 2: Plyometrics and Agility']= [workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0]]
         EP['Day 3: Cardio']= [workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)]]
         file = open("workoutprogram.txt","w")
         for key,value in EP.items():
            file.write(f'{key}\n')
            file.write('\n\n\n')
            for v in value:
               file.write(f'{v}\n') 
               file.write('\n\n\n')
    elif position == 'Center':
         EP['Day 1: Full Body Strength ']=[workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts['Legs'][r.randint(0, len(workouts["Legs"])-1)]+': '+ reps["Legs"][x],workouts["Bicep"][r.randint(0, len(workouts["Bicep"])-1)]+': '+ reps["Bicep"][x],workouts["Triceps"][r.randint(0, len(workouts["Triceps"])-1)]+': '+ reps["Triceps"][x],workouts["BACK"][r.randint(0, len(workouts["BACK"])-1)]+': '+ reps["BACK"][x],workouts["Chest"][r.randint(0, len(workouts["Chest"])-1)]+': '+ reps["Chest"][x],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]+': '+ reps["CORE"][0],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)]+': '+ reps["Shoulders"][x],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)]+': '+ reps["Shoulders"][x]]
         EP['Day 2: Plyometrics']= [workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]+': '+ reps["PLYOMETRICS"][0]]
         EP['Day 3: Cardio and Agility']= [workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)]+': '+ reps["Agility"][0],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)]]
         file = open("workoutprogram.txt","w")
         for key,value in EP.items():
            file.write(f'{key}\n')
            file.write('\n')
            for v in value:
               file.write(f'{v}\n') 
               file.write('\n\n\n')
    else:
        return 0
    print(EP)
    return EP
routines('beginner')



        
    

