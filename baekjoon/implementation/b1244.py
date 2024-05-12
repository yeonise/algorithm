import sys

input = sys.stdin.readline

switch_count = int(input().rstrip())
switch_status = [0]
switch_status.extend(list(map(int, input().rstrip().split())))

student_count = int(input().rstrip())
student = [list(map(int, input().rstrip().split())) for _ in range(student_count)]

for gender, number in student:
    if gender == 1:
        multiple = number
        while multiple <= switch_count:
            switch_status[multiple] = switch_status[multiple] ^ 1
            multiple += number
    elif gender == 2:
        switch_status[number] = switch_status[number] ^ 1

        left = number - 1
        right = number + 1
        while 1 <= left and right <= switch_count:
            if switch_status[left] == switch_status[right]:

                switch_status[left] = switch_status[left] ^ 1
                switch_status[right] = switch_status[right] ^ 1

                left -= 1
                right += 1
            else:
                break

count = 0

for number in switch_status[1:]:
    if count > 1 and count % 20 == 0:
        print()

    print(number, end=" ")
    count += 1
