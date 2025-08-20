import random


subject=[
    
    "virat kohli ",
    "narendra modi ",
    "sara alikhan ",
    "india cricket tem ",
    "sarukh khan ",
]


actions=[
    
    "matchs play",
    "posted movie ",
    "go to surat ",
    "play tha game",
    "win the ipl ",
    "watch movie "
]

place_or_things=[
    
    "near by home",
    "plate samosa ",
    "cheers up with bear",
    "at navsari ",
    "vist on plane"
]


while True:
    subjects=random.choice(subject)
    actions=random.choice(actions)
    things=random.choice(place_or_things)
    
    headline=f"BREAKING NEWS : {subjects}{actions}{things}"
    print("\n",headline)
    
    
    user_input=input("\n do want to headline ?? (yes/no) : ").strip().lower()
    if user_input=="no":
        break
    if user_input=="yes":
        continue
    if user_input.isdigit():   # ex: "123"
        print("❌ Please type in words (yes/no) not numbers. Try again.")
        continue
    else:
        print("enter a type :  yes or no ")
        continue
print("\n thanks for the watcing news ...have a nice day..")