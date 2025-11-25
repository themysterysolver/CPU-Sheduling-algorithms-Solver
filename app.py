import streamlit as st
from logic import algoSolver

st.title('CPU scheduling algorithm')


at = st.text_input('Arrival time')
bt = st.text_input('Burst time')


option = st.selectbox(
    "Algorithm",
    ("First come first served(FCFS)", "Shortest job first(SJF)", "Shortest remaining time first(SRTF)","Premptive Priority scheduling",
     "Non-Premptive priority scheduling","Round robin(RR)"),
    index=None,
    placeholder="Choose an algorithm"
)

tq = None
priority = None

if option == "Round robin(RR)":
    tq = st.text_input('Time quantum')
elif option == "Premptive Priority scheduling" or option == "Non-Premptive priority scheduling":
    priority = st.text_input('Priority')


if st.button('Solve'):
    ans = algoSolver(at,bt,option,tq,priority)
    if not ans:
        st.error("Incorrect input")



