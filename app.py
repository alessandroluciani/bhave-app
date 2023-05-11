
import streamlit as st


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# Titolo dell'app
st.title("ERIN: Assistente di behavioral profiling")

#if st.button("Inizia"):
genre = st.radio(
"Specializzazione medico: ",
('Oncologo', 'Chirurgo', 'Radioterapista'))

if genre == 'Oncologo':
    st.write('You selected comedy.')
elif genre == 'Chirurgo':
    st.write("You didn\'t select comedy.")
elif genre == 'Radioterapista':
    st.write("You didn\'t select c.")

choice = st.number_input("prendi un numero", 0, 10)








