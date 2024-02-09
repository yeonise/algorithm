def solution(n, cores):
    if len(cores) >= n:
        return n

    n -= len(cores)
    left = 1
    right = max(cores) * n

    while left < right:
        mid = (left + right) // 2
        works = sum([mid // core for core in cores])

        if works < n:
            left = mid + 1
        else:
            right = mid

    work_hours = left
    works_per_core = [(work_hours - 1) // core for core in cores]
    remain_works_for_last_hour = n - sum(works_per_core)

    for idx, core in enumerate(cores, start=1):
        core_can_work = (work_hours % core == 0)
        if core_can_work:
            remain_works_for_last_hour -= 1

            if remain_works_for_last_hour == 0:
                return idx
