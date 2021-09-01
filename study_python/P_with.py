import pickle

# with open("profile.pickle", "rb") as profile_file: #with문을 통해 알아서 종료시켜줌
#     print(pickle.load(profile_file))
    
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I'm studying hard, Python")
    
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
#읽고 쓰는 with문활용