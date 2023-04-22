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


def routines():
    EP= {}
    print('Select your position')
    position=input()
    if position== 'Shooting Guard':
        EP['upper body']=[workouts["Bicep"][r.randint(0, len(workouts["Bicep"])-1)],workouts["Triceps"][r.randint(0, len(workouts["Triceps"])-1)],workouts["BACK"][r.randint(0, len(workouts["BACK"])-1)],workouts["Shoulders"][r.randint(0, len(workouts["Shoulders"])-1)],workouts["Chest"][r.randint(0, len(workouts["Chest"])-1)],workouts["CORE"][r.randint(0, len(workouts["CORE"])-1)]]
        EP['lower body+Plyo']=[workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)],workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)],workouts["Legs"][r.randint(0, len(workouts["Legs"])-1)],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)],workouts["PLYOMETRICS"][r.randint(0, len(workouts["PLYOMETRICS"])-1)]]
        EP['Agility+cardio']=[workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)],workouts["Agility"][r.randint(0, len(workouts["Agility"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)],workouts["Cardio"][r.randint(0, len(workouts["Cardio"])-1)]]
        print(EP)
        return EP
    else:
        return 0    
routines()



        
    

