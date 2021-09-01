import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"name":"unoKim", "age":"28", "hobby":["soccer", "golf", "coding"]}
# print(profile)
# pickle.dump(profile, profile_file) #프로필에 정보를 파일에 저장하는것임
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # 파일에 있는 정보를 프로필에 불러오기
print(profile)
profile_file.close()
