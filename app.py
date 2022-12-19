import streamlit as st

# Custom Functions
import preprocessing
import results
import segmentations

def main():
    st.title('CareShare Survey Analysis')
    page = st.sidebar.selectbox("Please select a page:", ["Homepage", "Questions", "Results"])
    question_df, respondent_df = load_data()

    if page == "Homepage":
        load_homepage()
    elif page == "Questions":
        load_question_page(question_df)
    elif page == "Results":
        load_results_page(respondent_df)

@st.cache # Caches the data and only run it if it has not been seen before
def load_data(): 
    #DATA_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "data")
    DATA_URL = "https://raw.githubusercontent.com/Ready-Set-Care/CareShare-Survey/main/data/"

    RESPONDENTS_PATH = DATA_URL + "survey_responses.csv"
    OTHER_PATH = DATA_URL + "other_responses.csv"
    QUESTION_PATH = DATA_URL + "CareShare_Survey_Results-Questions.csv"
    
    question_df = preprocessing.prepare_questions(QUESTION_PATH)
    respondent_df = preprocessing.prepare_respondent_data(RESPONDENTS_PATH, OTHER_PATH)
    
    return question_df, respondent_df
    

def load_homepage():
    """
    The homepage is loaded using .markdown.
    """
    st.markdown("**Total Participants:** 301")
    st.markdown("**Launched On:** December 8, 2022")
    
    # Segmentation Information 
    st.markdown("## Segmentations")
    st.markdown("You can segment the results by the following segments using the drop down menu on the Results page.")
    # Description of Provider/Receiver Segment
    st.markdown("#### Provider/Receiver")
    st.markdown("**Question:** Would you mostly use CareShare to: a) ask for financial help from other family members for caregiving costs, or b) to provide financial help for caregiving costs to a family member?")
    st.markdown('The responses are segmented by:')
    st.markdown('* **Provider** - Those who answered *"provide financial help for caregiving costs to a family member"*')
    st.markdown('* **Receiver** - Those who answered *"ask for financial help from other family members for caregiving costs"*')
    # Description of More/Less Fair Segment
    st.markdown("#### More/Less Fair")
    st.markdown("**Question:** Do you agree or disagree that the cost of your REL's care is shared fairly by everyone in your family?")
    st.markdown('The segmented responses are based on the Likert scale (1-5) with the choices being: **not fair at all, somewhat unfair, neutral, somewhat fair,** and **very fair.**')



def load_question_page(df):
    """
    The Question page is loaded using .markdown. 
    """
    st.markdown("# Questions")
    st.markdown("This shows the list of survey questions in the order that the respondent saw them.")
    st.table(df)

def load_results_page(df):
    option = st.selectbox(
        "Select the one of the segmentations:",
        ("All Respondents", "Provider/Receiver", "More/Less Fair", "Kano-All Respondents"))

    st.markdown(f'## Survey Results for {option}')

    if option == "Provider/Receiver":
        segmentation = segmentations.get_segmentation("Provider or Receiver", df)
        results.get_response_data(df, segmentation, "Q18")
    elif option == "More/Less Fair":
        segmentation = segmentations.get_segmentation("More or less fair", df)
        results.get_response_data(df, segmentation, "Q9")
    elif option == "Kano-All Respondents":
        image_path = "https://github.com/Ready-Set-Care/CareShare-Survey/blob/main/images/CareShare-Kano-Results.png"
        st.image(image_path)
    else:
        results.get_response_data(df)


if __name__ == "__main__":
    main()

