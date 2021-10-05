weather = "dirty"
# weather = "sunny"
# weather = "rain"
if weather == "rain": 
    print("take a umbrella")
elif weather == "sunny":
    print("take a sun-protector")
else:
    print("have a good day")

temp = int(input("기온은 어때요?"))  # 숫자입력 폼
if 30 <= temp:
    print("It's too hot")
elif 10 <= temp and temp < 30:
    print("It's good")
elif 0 <= temp < 10:
    print("take a jaket")
else:
    print("It's too cold")
