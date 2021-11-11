libname final "/home/u44239293/final";

data final.ball;
	set work.import1;
run;

*descriptive stats for cateorical variables; 
proc freq data=final.ball;
	tables location outcome;
	title "Table 2: Descriptive Stats for Location and Outcome Variables";

*descriptive stats for quantitative variables;
proc means data=final.ball mean median stddev range min max q1 q3 qrange mode maxdec=2;
	var TM FG TRB	AST	STL	BLK	TOV;
	title "Table 3: Descriptive Stats for Quantitative Variables";
	
*histograms for quantitative variables- with color;
proc sgplot data=final.ball;
	histogram TM/scale=count fillattrs=(color=orange);
	title "Figure 1: Historgram of Total Points";
	xaxis label="Total Points Scored per game";	
	
proc sgplot data=final.ball;
	histogram FG/scale=count;
	title "Figure 2: Historgram of Field Goal Percentage";
	xaxis label="Field Goal Percentange per game";	
proc sgplot data=final.ball;
	histogram TRB/scale=count;
	title "Figure 3: Historgram of Total Rebounds";
	xaxis label="Total Rebounds per game";	
proc sgplot data=final.ball;
	histogram AST/scale=count;
	title "Figure 4: Historgram of Assits";
	xaxis label="Assits per game";	
proc sgplot data=final.ball;
	histogram STL/scale=count;
	title "Figure 5: Historgram of Steals";
	xaxis label="Steals per game";
proc sgplot data=final.ball;
	histogram BLK/scale=count;
	title "Figure 6: Historgram of Blocks";
	xaxis label="Blocks per game";	
proc sgplot data=final.ball;
	histogram TOV/scale=count;
	title "Figure 7: Historgram of Turnovers";
	xaxis label="Turnovers per game";	

*box plots for quantitative variables- with color;
proc sgplot data=final.ball;
	hbox TM/ fillattrs=(color=orange);
	title "Figure 8: Box Plot of Total Points";
	xaxis label="Total Points Scored per game";
proc sgplot data=final.ball;
	hbox FG;
	title "Figure 9: Box Plot of Field Goal Percentage";
	xaxis label="Field Goal Percentange per game";
proc sgplot data=final.ball;
	hbox TRB;
	title "Figure 10: Box Plot of Total Rebounds";
	xaxis label="Total Rebounds per game";
proc sgplot data=final.ball;
	hbox AST;
	title "Figure 11: Box Plot of Assits";
	xaxis label="Assits per game";	
proc sgplot data=final.ball;
	hbox STL;
	title "Figure 12: Box Plot of Steals";
	xaxis label="Steals per game";
proc sgplot data=final.ball;
	hbox BLK;
	title "Figure 13: Box Plot of Blocks";
	xaxis label="Blocks per game";	
proc sgplot data=final.ball;
	hbox TOV;
	title "Figure 14: Box Plot of Turnovers";
	xaxis label="Turnovers per game";
	
*creating a new variable called "avgstl";
data final.ballstl; 
	set final.ball;
	if stl < 5 then AVGSTL = 1;
	if 5 <= stl < 10 then AVGSTL = 2;
	if 10 <= stl < 15 then AVGSTL = 3; 
	if stl >= 15 then AVGSTL = 4;
proc format;
	value steal 1="Low"
				2="Decent"
				3="Average"
				4="High";
data final.ballstl;
	set final.ballstl;
	format AVGSTL steal.; 
	
*bar chart of new "avgstl" variable;	
proc sgplot data=final.ballstl;
	vbar avgstl;
	title "Figure 15: Bar Chart of Average Steals";
	xaxis label="Average steals per game";
	
*frequency table of new "avgstl" variable;
proc freq data=final.ballstl;
	table avgstl;
	title "Table 4: Freq Table for Average Steals";
	
*contingency table of location and outcome variables;
proc freq data=final.ball;
	tables location*outcome;
	title "Table 5: Contingency Table of Location and Outcome Variables";
	
*100% stacked bar chart of 	location and outcome variables;
PROC FREQ DATA=final.ball;
	TABLES location*outcome;
	ODS OUTPUT CrossTabFreqs = CT;
DATA CT2;
	SET CT (DROP = TABLE    _TYPE_    _TABLE_   MISSING);
	IF NOT MISSING (ROWPERCENT);
PROC SGPLOT DATA = CT2;
	TITLE1 'Figure 16: 100% Stacked Bar Chart of Location by Outcome';
	VBAR location / GROUP = outcome RESPONSE=ROWPERCENT;
	YAXIS LABEL = 'Percent within Outcome';
	
*SBS box plots of outcome and field goal percentage;
proc sgplot data=final.ball;
Title1 'Figure 17: Side By Side Boxplots Of Field Goal Percentage by Outcome';
hbox FG / category= outcome;
xaxis label = 'Field Goal Percentage';

*Side By Side Histograms Of Field Goal Percentage By Outcome;
proc sort data=final.ball out=sorted;
by outcome;
proc sgplot data=sorted;
Title1 'Figure 18: Side By Side Histograms Of Field Goal Percentage by Outcome';
histogram FG;
by outcome;
xaxis label = 'Field Goal Percentage';

*simple random sample; 
proc surveyselect data=final.ball out=final.ballsample seed=43 method=srs sampsize=35; 
title "Table 6: Simple Random Sample";

*descriptive stats for SRS;
proc means data=final.ballsample mean median stddev range min max q1 q3 qrange mode maxdec=2;
	var TM FG TRB	AST	STL	BLK	TOV;
	title "Table 7: Descriptive Stats for Simple Random Sample";

*stratified confidence interval of outcome and field goal percentage;
proc means data=final.ballsample alpha=0.05 mean lclm uclm maxdec=2;
	var FG;
	class outcome;
	title "Table 8: Confidence Interval for Field Goal Percentage by Outcome";
	
*scatter plot for assists and total points scored;
proc sgplot data=final.ball;
	reg x=ast y=tm; 
	xaxis label="Assits per game";
	yaxis label="Total Point Scored per game";
	title "Figure 19: Scatterplot for Assists and Total Points Scored";