import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()


rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('draw')
if reslut < 0:
    print('man1 win')
elif result > 0:
    print('man2 win')