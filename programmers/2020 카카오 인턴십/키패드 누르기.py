def solution(numbers, hand):
    hand = "R" if hand == "right" else "L"
    thumbs = {"L": "*", "R": "#"}
    default = {
        1: "L", 4: "L", 7: "L",
        3: "R", 6: "R", 9: "R"
    }
    position = {
        1: (1, 0), 2: (1, 1), 3: (1, 2),
        4: (2, 0), 5: (2, 1), 6: (2, 2),
        7: (3, 0), 8: (3, 1), 9: (3, 2),
        "*": (4, 0), 0: (4, 1), "#": (4, 2)
    }

    results = []

    for number in numbers:
        if number in default:
            results.append(default[number])
            thumbs[default[number]] = number
        else:
            l_distance = (abs(position[number][0] - position[thumbs["L"]][0]) +
                          abs(position[number][1] - position[thumbs["L"]][1]))
            r_distance = (abs(position[number][0] - position[thumbs["R"]][0]) +
                          abs(position[number][1] - position[thumbs["R"]][1]))

            if l_distance == r_distance:
                results.append(hand)
                thumbs[hand] = number
            else:
                selected = "L"
                if l_distance > r_distance:
                    selected = "R"
                results.append(selected)
                thumbs[selected] = number

    return "".join(results)
