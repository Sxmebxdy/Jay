"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_list = []
    for item in student_scores:
        new_list.append(round(item))
    return new_list

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed = 0
    for item in student_scores:
        if item <= 40:
            failed += 1
    return failed

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best = []
    for item in student_scores:
        if item >= threshold:
            best.append(item)
    return best

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
    interval_size = (highest - 40) // 4  # Berechnung der Intervallgröße
    return [41 + interval_size * i for i in range(4)]

def student_ranking(student_scores, student_names):
    """Match student names with their scores and return class rankings.

    :param student_scores: list - exam scores in descending order.
    :param student_names: list - student names in descending order by score.
    :return: list - formatted rankings as "<rank>. <student name>: <student score>".
    """
    # Verwenden von enumerate, um den Rang (Index + 1) zu bestimmen
    return [f"{rank + 1}. {name}: {score}" 
            for rank, (name, score) in enumerate(zip(student_names, student_scores))]

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for item in student_info:
        if item[1] == 100:
            return item
    return []
    
