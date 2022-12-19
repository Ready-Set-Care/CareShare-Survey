import numpy as np
import pandas as pd


def prepare_questions(questions_path: str) -> pd.DataFrame:
    """
    Load and prepare the list of questions

    Parameters:
    -----------

    link: str
        Link to questions dataset in .csv format
    """
    questions = pd.read_csv(questions_path, index_col=0)
    questions = questions[questions["type"] != "simpleblock"]
    questions = questions[questions["type"] != "intro"]

    #questions["answerType"] = questions["answerType"].map(" ({})".format, na_action="ignore")
    answer_counts = ['293', '301', '301', '301', '301', '139', '62', '301', '301', '37', '264', '301', '247', '54', '301', '301', '301', '301', '301', '301', '301', 'N\\A', '301', '301', 'N\\A', '301', '301', 'N\\A', '301', '301', '301', '253', '266']
    questions['num of respondents'] = answer_counts 

    questions = questions[["name", "type", 'num of respondents']].copy()

    return questions


def prepare_respondent_data(respondents_path: str, other_path) -> pd.DataFrame:
    """
    Load and prepare the data 

    Parameters:
    -----------

    link : str
        Link to respondent dataset in .csv format
    """
    responses = pd.read_csv(respondents_path, index_col=0)

    return responses


