def solution(k, room_number):
    in_use = {}
    answer = []

    for request in room_number:
        if request not in in_use:
            in_use[request] = request + 1
            answer.append(request)
        else:
            room = in_use[request]
            update_list = [request, room]

            while room in in_use:
                room = in_use[room]
                update_list.append(room)

            for r_number in update_list:
                in_use[r_number] = room + 1

            answer.append(room)

    return answer
