def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    A_index = 0
    last = len(B) - 1

    for B_index, B_number in enumerate(B):
        A_number = A[A_index]

        if A_number < B_number:
            answer += 1
            A_index += 1
        else:
            last -= 1

    return answer
