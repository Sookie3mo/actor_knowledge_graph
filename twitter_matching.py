import jellyfish
import json

twitter_names = []
with open('twitter_users_profile_2254.jl' , 'r') as f1:
    for line in f1:
        row = json.loads(line)
        #print(row)
        name = [row['name'],row['id']]
        twitter_names.append(name)


imdb_names = []
with open('imdb_all_actors.jl' , 'r') as f1:
    for line in f1:
        row = json.loads(line)
        #print(row)
        name = [row['name'],row['id']]
        imdb_names.append(name)



re = []
re2 = []
re3 = []
re4 = []
count1 = count2= count3 =count4 = 0
cnt1 = cnt2 = cnt3 = cnt4 =0
for i in range(0,len(imdb_names)-30000):
	for j in range(0,len(twitter_names)):
		dis_name = jellyfish.jaro_winkler(imdb_names[i][0],twitter_names[j][0])
		#print(imdb_names[i][0],twitter_names[j][0])
		if dis_name>= 0.95:
			re_i = []
			re_i.extend(imdb_names[i])
			re_i.extend(twitter_names[j])
			re.append(re_i)	
			#print(imdb_names[i],twitter_names[j])
			#print(re)
			#print('\n')
			count1 += 1
			if imdb_names[i][1] == twitter_names[j][1]:
				cnt1 +=1

		if dis_name>= 0.94 and dis_name< 0.95:
			re_i = []
			re_i.extend(imdb_names[i])
			re_i.extend(twitter_names[j])
			re2.append(re_i)	
			#print(imdb_names[i],twitter_names[j])
			#print('\n')
			count2 += 1
			if imdb_names[i][1] == twitter_names[j][1]:
				cnt2 +=1
		if dis_name>= 0.93 and dis_name< 0.94:
			re_i = []
			re_i.extend(imdb_names[i])
			re_i.extend(twitter_names[j])
			re3.append(re_i)	
			#print(imdb_names[i],twitter_names[j])
			#print('\n')
			count3 += 1
			if imdb_names[i][1] == twitter_names[j][1]:
				cnt3 +=1
		if dis_name>= 0.925 and dis_name< 0.93:
			re_i = []
			re_i.extend(imdb_names[i])
			re_i.extend(twitter_names[j])
			re4.append(re_i)	
			#print(imdb_names[i],twitter_names[j])
			#print('\n')
			count4 += 1
			if imdb_names[i][1] == twitter_names[j][1]:
				cnt4 +=1
print(re)
print(count1,count2,count3,count4)
print(cnt1,cnt2,cnt3,cnt4)
#all 2254
#(1935, 105, 198, 229)
#(1849, 16, 16, 7)