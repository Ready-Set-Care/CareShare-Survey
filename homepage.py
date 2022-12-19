import streamlit as st

def load_homepage():
    """
    The homepage is loaded using .markdown.
    """
    st.markdown("**Total Participants:** 301")
    st.markdown("**Launched On:** December 8, 2022")
    st.markdown("### Description of Respondents")
    st.markdown("People who are providing care to a relative or family member 60 years of age or older. Respondent or another family member must have paid for any of the costs associated with caring for the relative.")
    st.markdown("**Gender:** Any")
    st.markdown("**Age:** Any")
    load_screener_questions()
    
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


def load_screener_questions():
    with st.expander("See screening questions"):
        st.markdown("1. What is your gender?")
        st.markdown("2. Please enter your age:___")
        st.markdown("3. Which of the following have you participated in over the past 12 months? *Please select all that apply.* (TERMINATE if not *Cared for a relative or family member to help them take care of themselves*.)")
        st.markdown("4. In the previous question you mentioned that you cared for a family member to help them take care of themselves. Did you or another family member pay for any of the costs associated with their care? (TERMINATE if not *Yes*.)")
        st.markdown("5. Please enter the age of the relative or family member you helped take care of over the past year: (TERMINATE if not *60+*.)")
        st.markdown("6. What is your approximate annual household income (before tax)? (TERMINATE if *Prefer not to say*.)")
