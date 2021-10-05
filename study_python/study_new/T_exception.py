try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0] , nums[1], nums[2]))
except ValueError:
    print("에러! 타입을 맞춰주세요")
except ZeroDivisionError as err:
    print(err , "에러! 0으로 나눌수가 없습니다.")
except Exception as err:
    print(err, "알 수 없는 에러가 발생함 ㅠㅠ")
    
