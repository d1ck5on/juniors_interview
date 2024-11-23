def appearance(intervals: dict[str, list[int]]) -> int:
    def construct_interval(time: int,
                           idx: int,
                           user_type: str) -> tuple[int, int, str]:
        return (time, 1 - 2 * (idx % 2), user_type)

    def is_all(is_lesson: bool, pupil_cnt: int, tutor_cnt: int):
        return is_lesson and pupil_cnt > 0 and tutor_cnt > 0

    lesson = [
        construct_interval(time, idx, "lesson")
        for idx, time in enumerate(intervals["lesson"])
    ]
    tutor = [
        construct_interval(time, idx, "tutor")
        for idx, time in enumerate(intervals["tutor"])
    ]
    pupil = [
        construct_interval(time, idx, "pupil")
        for idx, time in enumerate(intervals["pupil"])
    ]
    all_intervals = sorted(lesson + tutor + pupil)

    is_lesson_now = False
    pupil_cnt = 0
    tutor_cnt = 0
    start, total = -1, 0
    for time, i, user_type in all_intervals:
        match user_type:
            case "lesson":
                is_lesson_now = (i == 1)
            case "pupil":
                pupil_cnt += i
            case "tutor":
                tutor_cnt += i

        if is_all(is_lesson_now, pupil_cnt, tutor_cnt) and start == -1:
            start = time

        if not is_all(is_lesson_now, pupil_cnt, tutor_cnt) and start != -1:
            total += time - start
            start = -1

    return total
