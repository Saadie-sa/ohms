import streamlit as st 
st.title('HI DADDY')
st.write('HI dadday how are you? I hope your safe with your mommy. i know your fully safe daddy bcuz i know your mom')
st.markdown('<h1>OHMS CALUCALATOR</h1>',unsafe_allow_html=True)
#st.radio('Choose the operator',options=['voltage','Current','Resistance'])
with st.form('form2'):
    col1,col2,col3=st.columns(3)
    col1.number_input('Voltage')
    col2.number_input('Current')
    col3.number_input('Resistance')
    st.form_submit_button('submit')
    