import plotly.express as px
import streamlit as st

def get_value_pcts(df_question):
    vc = df_question.value_counts()
    vc = vc.apply(lambda x: round((x / vc.sum())*100))
    return vc

def get_vc(df_question):
    vc = df_question.value_counts().reset_index()
    vc.columns.values[0] = 'Answer'
    vc.columns.values[1] = 'Counts'
    vc["Percent"] = vc['Counts'].apply(lambda x: round((x / vc['Counts'].sum())*100))
    return vc


class Question:
    """Base class for all question types."""

    def __init__(self, question, response_df) -> None:
        self.question = question
        self.response_df = response_df
        self.count = self.response_df[self.question].count()
        

class NumericQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.mean = round(self.response_df[self.question].mean())
        self.median = round(self.response_df[self.question].median())
        self.min = round(self.response_df[self.question].min())
        self.max = round(self.response_df[self.question].max())
    
    def display_data(self) -> None:
        data =  [self.mean, self.median, self.min, self.max]
        col1, col2, col3 = st.columns(3)
        col1.metric("Mean", f'${data[0]}')
        col2.metric("Median", f'${data[1]}')
        col3.metric("Range", f'${data[2]} - ${data[3]}')


class LikertQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.mean = round(self.response_df[self.question].mean())
        self.median = round(self.response_df[self.question].median())
        self.vc = get_value_pcts(self.response_df[self.question])


    def display_data(self) -> None:
        st.markdown(f'**Mean:** {self.mean}')
        st.markdown(f'**Median:** {self.median}')
        st.markdown("##### Likert Breakdown")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            try:
                col1.metric("1", f'{self.vc[1]}%')
            except KeyError: 
                col1.metric("1", f'0%')
        with col2:
            try:
                col2.metric("2", f'{self.vc[2]}%')
            except KeyError: 
                col2.metric("2", f'0%')
        col3.metric("3", f'{self.vc[3]}%')
        col4.metric("4", f'{self.vc[4]}%')
        with col5:
            col5.metric("5", f'{self.vc[5]}%')
            


class ShortQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.answers = self.response_df.loc[self.response_df[self.question].notnull() == True][self.question]

    def display_data(self) -> None:
        st.dataframe(self.answers)

class MultipleQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.vc = get_vc(self.response_df[self.question])

    def display_data(self) -> None:
        fig = px.bar(self.vc, x='Answer', y='Counts', hover_data=['Percent'])
        st.plotly_chart(fig, theme='streamlit')
            
    
question_mapping = {
    "NUMBER": NumericQuestion,
    "LIKERT": LikertQuestion,
    "MULTCHOICE": MultipleQuestion,
    "SHORT": ShortQuestion,
}