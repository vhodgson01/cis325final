#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:58:44 2025

@author: torihodgson
"""


import pandas as pd 
import datetime as dt

file = '/Users/torihodgson/Downloads/PremierLeagueMatches.csv'

df = pd.read_csv(file)
print(df.shape)          # Rows and columns
print(df.columns)
print(df.describe)
print(df.info())

df['Date'] = pd.to_datetime(df['Date'],errors = 'coerce')

df['Attendance'] = df['Attendance'].str.replace(',', '', regex=False)
df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')

df = df.dropna(subset=['Result'])

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Result', data=df)
plt.title('Match Results Distribution (Home Win / Draw / Away Win)')
plt.show()

sns.scatterplot(x='homeXG', y='homeScore', data=df)
plt.title('Home Expected Goals vs Actual Score')
plt.show()

sns.scatterplot(x='awayXG', y='awayScore', data=df)
plt.title('Away Expected Goals vs Actual Score')
plt.show()

avg_attendance = df.groupby('Result')['Attendance'].mean().reset_index()

sns.barplot(x='Result', y='Attendance', data=avg_attendance)
plt.title('Average Attendance by Match Result')
plt.xlabel('Match Result')
plt.ylabel('Average Attendance')
plt.show()


df['HomeWin'] = df['Result'] == 'H'

sns.histplot(data=df, x='Attendance', hue='HomeWin', bins=20, kde=True, element='step')
plt.title('Attendance Distribution: Home Wins vs Others')
plt.show()
