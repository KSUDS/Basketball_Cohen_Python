# %%

import pandas as pd
import numpy as np
from plotnine import *
import matplotlib as plt

# import os
# os.getcwd()

# %%

ball = pd.read_csv('../data/ball.csv')

ball = ball.drop(columns='Game_Number')

# %%

ball.describe(exclude=[np.number])  

ball.describe()

# %%

# histograms for the numerical variables


f1 = (
    ggplot(ball, aes(x='TM')) +
     geom_histogram(fill = 'orange', color = 'black') +
     labs (x = 'Total Points Scored', y = 'Count', 
        title = 'Figure 1: Histogram for Total Points Scored') +
     theme_bw()   
)

f1.save("f1_cohen_Python.png", width = 15, height = 6)

f2 = (
    ggplot(ball, aes(x='FG')) +
     geom_histogram(fill = 'orange', color = 'black') +
     labs (x = 'Field Goal Percentage', y = 'Count', 
        title = 'Figure 2: Histogram for Field Goal Percentage') +
     theme_bw()     
)

f2.save("f2_cohen_Python.png", width = 15, height = 6)

f3 = (
    ggplot(ball, aes(x='TRB')) +
        geom_histogram(fill = 'orange', color = 'black') +
        labs (x = 'Total Rebounds', y = 'Count', 
            title = 'Figure 3: Histogram for Total Rebounds') +
     theme_bw()   
)

f3.save("f3_cohen_Python.png", width = 15, height = 6)

f4 = (
    ggplot(ball, aes(x='AST')) +
     geom_histogram(fill = 'orange', color = 'black') +
     labs (x = 'Total Assists', y = 'Count', 
        title = 'Figure 4: Histogram for Total Assists') +
     theme_bw()   
)

f4.save("f4_cohen_Python.png", width = 15, height = 6)

f5 = (
    ggplot(ball, aes(x='STL')) +
     geom_histogram(fill = 'orange', color = 'black') +
     labs (x = 'Total Steals', y = 'Count', 
        title = 'Figure 5: Histogram for Total Steals') +
     theme_bw()   
)

f5.save("f5_cohen_Python.png", width = 15, height = 6)

f6 = (
    ggplot(ball, aes(x='BLK')) +
     geom_histogram(fill = 'orange', color = 'black') +
     labs (x = 'Total Blocks', y = 'Count', 
        title = 'Figure 6: Histogram for Total Blocks') +
     theme_bw()   
)

f6.save("f6_cohen_Python.png", width = 15, height = 6)

f7 = (
    ggplot(ball, aes(x='TOV')) +
     geom_histogram(fill = 'orange', color = 'black') +
     labs (x = 'Total Turnovers', y = 'Count', 
        title = 'Figure 7: Histogram for Total Turnovers') +
     theme_bw()   
)

f7.save("f7_cohen_Python.png", width = 15, height = 6)
# %%

# box plotsthe numerical variables

ball.boxplot() # all the numerical data box plots

f8 = ( 
    ggplot(ball,aes(y='TM',x=0)) + 
        geom_boxplot(fill = 'orange', color = 'black') +
        labs (x = 'Count', y = 'Total Points Scored', 
            title = 'Figure 8: Boxplot for Total Points Scored') +
     theme_bw()   
)

f8.save("f8_cohen_Python.png", width = 15, height = 6)

f9 = ( 
    ggplot(ball,aes(y='FG',x=0))+
        geom_boxplot(fill = 'orange', color = 'black') +
        labs (x = 'Count', y = 'Field Goal Percentage', 
            title = 'Figure 9: Boxplot for Field Goal Percentage') +
     theme_bw()   
)

f9.save("f9_cohen_Python.png", width = 15, height = 6)

f10 = ( 
    ggplot(ball,aes(y='TRB',x=0))+
        geom_boxplot(fill = 'orange', color = 'black') +
        labs (x = 'Count', y = 'Total Rebounds', 
            title = 'Figure 10: Boxplot for Total Rebounds') +
     theme_bw()   
)

f10.save("f10_cohen_Python.png", width = 15, height = 6)

f11 = ( 
    ggplot(ball,aes(y='AST',x=0))+
        geom_boxplot(fill = 'orange', color = 'black') +
        labs (x = 'Count', y = 'Total Assists', 
            title = 'Figure 11: Boxplot for Total Assists') +
     theme_bw()   
)

f11.save("f11_cohen_Python.png", width = 15, height = 6)

f12 = ( 
    ggplot(ball,aes(y='STL',x=0))+
        geom_boxplot(fill = 'orange', color = 'black') +
        labs (x = 'Count', y = 'Total Steals', 
            title = 'Figure 12: Boxplot for Total Steals') +
     theme_bw()   
)

f12.save("f12_cohen_Python.png", width = 15, height = 6)

f13 = ( 
    ggplot(ball,aes(y='BLK',x=0))+
        geom_boxplot(fill = 'orange', color = 'black') +
        labs (x = 'Count', y = 'Total Blocks', 
            title = 'Figure 13: Boxplot for Total Blocks') +
     theme_bw()   
)

f13.save("f13_cohen_Python.png", width = 15, height = 6)

f14 = ( 
    ggplot(ball,aes(y='TOV',x=0))+
        geom_boxplot(fill = 'orange', color = 'black') +
        labs(x = 'Count', y = 'Total Turnovers', 
            title = 'Figure 14: Boxplot for Total Turnovers') +
     theme_bw()   
)

f14.save("f14_cohen_Python.png", width = 15, height = 6)
# %%

# creating new categorical variable

ball['avgstl'] = pd.cut(ball['STL'], bins=[0, 5, 10, 14, 99], 
labels=['Low', 'Decent', 'Average', 'High'])

 # %%
# bar chart of new avgstl variable

f15 = (
    ggplot(ball) + 
        geom_bar(aes(x='avgstl'), fill = 'orange', color = 'black') + 
        labs(y = 'Count', x = 'Average Steals', 
            title = 'Figure 15: Bar Chart of Average Steals') +
     theme_bw()   
)

f15.save("f15_cohen_Python.png", width = 15, height = 6)
# %%

#frequency table of avg counts - no percentages

ball['avgstl'].value_counts()
# %%

# contingency table of location and outcome variables - no percents

ball_loc_out = pd.crosstab(index= ball['Location'], columns = ball['Outcome'], margins = True)
print(ball_loc_out)

# %%

#100% stacked bar chart of 	location and outcome variables

f16 = (
    ggplot(ball, aes('Location', fill='Outcome')) +
        geom_bar( position='fill') +
        labs( y = 'Percent of Outcome', title = 'Figure 16: Stacked Bar Chart of Location vs. Outcome') +
     theme_bw()   
)
f16.save("f16_cohen_Python.png", width = 15, height = 6)
# %%

# scatter plot for assists and total points scored

f17 = (
    ggplot(ball, aes(x = 'AST', y = 'TM')) +
    geom_point() +
    labs(title = 'Figure 17: Scatterplot for Assists and Total Points Scored', x = 'Assists', y = 'Total Points Scored') +
     theme_bw()   
)
f17.save("f17_cohen_Python.png", width = 15, height = 6)
# %%
