"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = []
    for score in student_scores:
        rounded_score = round(score)
        rounded_scores.append(rounded_score)
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_students_counter = 0
    for score in student_scores:
        if score <= 40:
            failed_students_counter += 1
    return failed_students_counter


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_students = []
    for score in student_scores:
        if score >= threshold:
            best_students.append(score)
    return best_students

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    letter_grade_interval = round((highest - 40) / 4)
    # return [41, 41 + letter_grade_interval, 41 + letter_grade_interval * 2, 41 + letter_grade_interval * 3]
    return [41 + letter_grade_interval * number for number in range(4)]
# print(letter_grades(85))

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    sorted_list = []
    for counter, student in enumerate(student_names):
        total_student_information = str(counter+1) + ". " + str(student) + ": " + str(student_scores[counter])
        sorted_list.append(total_student_information)
    return sorted_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for info in student_info:
        if info[-1] == 100:
            return info
    return []

# print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100], ["Radjah", 99]]))
