import random

random_number = random.randint(1, 100)

my_input = int(input('내 키는 몇일까요? 입력 : '))
cnt = 1
while True:
    try: 
        if(my_input == random_number):
            print('맞췄습니다! 내 키는', random_number, '였어요')
            print(cnt, '번 만에 맞췄습니다.') 
            break
        elif(my_input > random_number):
            print('틀렸어요. 좀더 작아요')
        elif(my_input < random_number):
            print('틀렸어요. 좀더 커요')
        my_input = int(input('다시 입력 : '))
        cnt = cnt + 1
    except:
        print('숫자로 입력하세요.')


