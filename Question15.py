#Write a program to plot a bar chart in python to display the result of a school for five co

import matplotlib.pyplot as pl
year=['2015','2016','2017','2018','2019']# list of years
p=[100,75.5,55.25,95.5,61.50]	#list of pass
j=['b','g','r','m','c']		# color code of bar charts
pl.bar(year,  p,  width=0.2,  color=j)		# bar( ) function to create the
pl.xlabel("year")	# label for x-axis
pl.ylabel("Pass%")	# label for y-axis
pl.show( )	#  function  to  display  bar  chart
