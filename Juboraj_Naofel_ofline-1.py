import pandas as pd
import numpy as np
import math
import operator

def knn(x,y,count_row,k,j):
	i = 0
	mylist = None
	mylist = []
	print("===========================================================================================================")
	print(x)
	while i<count_row:
		d1 = (x.iat[0,2] - y.iat[i,2])**2
		d2 = (x.iat[0,3] - y.iat[i,3])**2
		d3 = (x.iat[0,4] - y.iat[i,4])**2
		d4 = (x.iat[0,5] - y.iat[i,5])**2
		d5 = (x.iat[0,6] - y.iat[i,6])**2
		d6 = (x.iat[0,7] - y.iat[i,7])**2
		d7 = (x.iat[0,8] - y.iat[i,8])**2
		d8 = (x.iat[0,9] - y.iat[i,9])**2
		dplus = d1+d2+d3+d4+d5+d6+d7+d8
		d = math.sqrt(dplus)
		mylist.append((y.iat[i,0],y.iat[i,1],d))
		#print(d)
		i+=1
	print('---------------------------------------------------------------------------------')
	print('5 recommendations for this movie-------------------------------------------------')
	print('---------------------------------------------------------------------------------')
	mylist.sort(key = operator.itemgetter(2))
	i = 0
	for x in mylist:
		if i>=k:
			break
		print(f'{i+1}. Name:{x[1]} --- ID:{x[0]}')
		i+=1
	print("===========================================================================================================")
def main():
	df = pd.read_csv (r'movies_recommendation_data.csv') 
	count_row = df.shape[0]
	#spliting the data frame according to percentage
	percentage60 = int(count_row*(60/100))
	df_train = df[0:percentage60]
	df_test = df[percentage60:count_row]
	df_test.reset_index(inplace = True, drop = True) 
	#taking the movie id as input
	count_row=count_row-percentage60
	j = 0
	while(j<count_row):
		movieId = df_test[j:(j+1)]
		movieId.reset_index(inplace = True, drop = True)
		print(f"\n\nRecomendation for movie {j+1}")
		knn(movieId,df_train,percentage60,5,j)
		j+=1
main()