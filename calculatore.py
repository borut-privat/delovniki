#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:33:56 2023

@author: boruttrpin
"""
import datetime
import streamlit as st
st.set_page_config(
page_title="Delovni dnevi",
page_icon="🔦")

def is_weekday(date):
    # Monday = 0, Sunday = 6
    return date.weekday() < 5  # Monday to Friday are considered weekdays

holidays = [datetime.date(2023, 8, 15), datetime.date(2023, 8, 14),datetime.date(2023, 10, 31),datetime.date(2023, 11, 1),datetime.date(2023, 12, 25),datetime.date(2023, 12, 26),datetime.date(2024, 1, 1),datetime.date(2024, 1, 2),datetime.date(2024, 2, 8),datetime.date(2023, 3, 31),datetime.date(2024, 4, 1),datetime.date(2024, 4, 27),datetime.date(2024, 5, 1),datetime.date(2024, 6, 25),datetime.date(2024, 8, 15),datetime.date(2024, 10, 31),datetime.date(2024, 11, 1),datetime.date(2024, 12, 25),datetime.date(2024, 12, 26)]

# Initialize the current date
start_date = st.date_input("Začetni datum", datetime.date(2019, 7, 6),format="DD.MM.YYYY")
current_date = start_date
num_days= st.number_input("Koliko delovnih dni kasneje?", value=1, step=1)
exclude_first_day=st.checkbox("Brez začetnega dneva?")
if exclude_first_day:
    current_date += datetime.timedelta(days=1)
num_days-=1
while num_days > 0:
    # Move to the next day
    
    current_date += datetime.timedelta(days=1)
    # Check if the current date is a weekday and not in the holidays list
    if is_weekday(current_date) and current_date not in holidays:
        num_days -= 1

st.write(current_date)
