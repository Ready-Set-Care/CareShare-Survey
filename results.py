import pandas as pd
import streamlit as st

# Custom Packages
import question_class

QUESTION_TYPE_MAP = {
       'Q2': 'MULTCHOICE',
       'Q3': 'NUMBER',
       'Q4': 'NUMBER',
       'Q5': 'NUMBER',
       'Q6': 'MULTCHOICE',
       "Q7": 'MULTANSWER',
       'Q8': 'MULTANSWER',
       "Q9": 'LIKERT',
       'Q12': 'LIKERT',
       'Q13': 'SHORT',
       'Q14': 'SHORT',
       'Q15': 'LIKERT',
       'Q16': 'SHORT',
       'Q17' : 'SHORT',
       'Q18': 'MULTCHOICE',
       'Q19': 'MULTCHOICE',
       'Q20': 'MULTCHOICE',
       "Q21": 'LIKERT',
       'Q22': 'MULTCHOICE',
       'Q23': 'LIKERT',
       'Q24': 'LIKERT',
       'Q35': 'LIKERT',
       'Q36': 'SHORT',
       'Q37': 'SHORT'
}

QUESTION_NAME_MAP = {
    'Q2': 'Which of these best describes the older adult you care for?',
    'Q3': "What is the approximate total monthly cost of your REL's care?",
    'Q4': "How much of that $COST monthly cost is paid for by your REL's income, benefits, and savings?",
    'Q5': 'How much of the $COST monthly cost do you pay for?',
    'Q6': 'Does your family currently share costs?',
    "Q7": "How do you share the costs associated with your REL's care?",
    'Q8': 'How do you send or receive money with your family?',
    "Q9": "Do you agree or disagree that the cost of your 's care is shared fairly by everyone in your family?",
    'Q12': "How interested are you in an application like CareShare that would help your family share your REL's caregiving expenses?",
    'Q13': 'Why are you not interested in an application CareShare?',
    'Q14': 'Why are you interested in an application CareShare?',
    'Q15': 'How interested do you think your family members would be in an application like CareShare?',
    'Q16': 'Why do you think your family would be interested?',
    'Q17' : 'Why would your family not be interested in an application like CareShare?',
    'Q18': 'Would you mostly use CareShare to: a) ask for financial help from other family members for caregiving costs, or b) to provide financial help for caregiving costs to a family member?',
    'Q19': ' Thinking about Careshare, would you prefer to: a) split specific expenses and bills with your family, or b) to split a single total monthly cost?',
    'Q20': 'Do you think your family would most likely split a (a) fixed monthly payment or (b) variable monthly payment based on costs incurred?',
    "Q21": "Do you agree or disagree that CareShare should only include the primary family caregiver's expenses?",
    'Q22': 'In CareShare, would you want expense receipts for caregiving costs to be: be required | be optional | never be included',
    'Q23': 'How helpful would it be if your family were able to comment on expenses entered into CareShare?',
    'Q24': 'Would be helpful to your family if CareShare provided a way to finance caregiving costs through the app?',
    'Q35': 'Assuming that CareShare worked in the ways you prefer, how interested are you in a product like CareShare?',
    'Q36': 'Is there anything you think we missed that would help your family split the cost of caring for your ?',
    'Q37': 'Was there any part of this survey you found confusing or need more clarification on?'
}


def get_response_data(responses_df, segmentation=None, skip_q=None):
    general_stats(responses_df, segmentation, skip_q)



def general_stats(df, segmentation=None, skip_q=None):
    questions = list(df.columns)
    
    survey_data = []


    for q in questions:
        if q != skip_q:
            type = QUESTION_TYPE_MAP[q]
            # Check if question type is in "question_mapping" and loop through for each question
            if question_class.question_mapping.get(type):
                st.markdown(f'#### {QUESTION_NAME_MAP[q]}')

                # If data is being segmented, loop through each segment for each question 
                if segmentation is not None:
                    for key, value in segmentation.items():
                        st.markdown(f'##### {key}')
                        instance = question_class.question_mapping[type](q, value)
                        instance.display_data()
                else:
                    instance = question_class.question_mapping[type](q, df)
                    instance.display_data()
            st.markdown('---')
        else:
            continue