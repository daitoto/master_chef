# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
users = dict()
f = open('chef.log', 'r')
last_id = 0
start_time = 0
end_time = 0
for i, line in enumerate(f):
	s = line[:-1].split(' ')
	log_day = s[0]
	log_month = s[1]
	log_year = s[2]
	log_time = s[3]
	time_string = '%s %s %s %s' % (s[0], s[1], s[2], s[3])
	word = s[5]
	user_id = s[6]
	if len(word) == 0 or word[0] == '1':
		continue
	if not user_id in users:
		users[user_id] = []
	if user_id != last_id:
		if last_id != 0 and end_time - start_time > 0:
			users[last_id].append([
				time.asctime(time.localtime(start_time)),
				end_time-start_time])
		last_id = user_id
		start_time = time.mktime(time.strptime(time_string, '%d %b %Y %H:%M:%S'))
		#print(start_time)
	end_time = time.mktime(time.strptime(time_string, '%d %b %Y %H:%M:%S'))

users[last_id].append([time.asctime(time.localtime(start_time)), end_time-start_time])
#test users
del users['9181c619bbe34e9e935248a70a199e37']
del users['821f97b15f8040f4bc81a27e3110123a']
del users['yD+hLDODcFOwJ1GSjmK1zQ==']
del users['c10e035b6cbb40838d1b02e9f662fbb5']
del users['73746d639a834ea8ab16cfa62482f98d']
del users['PCsoyMoECaMI8EidHM9o4g==']
del users['2159d8d8cfc04ad596a19af3206d6ffc']

tot_num = 0
tot_users = len(users)
next_day_users = 0
use_skill_times = np.zeros(24, np.int64)
use_skill_lens = []
for user in users:
	back_again = False
	his = users[user]
	#print(user)
	#print(his)
	tot_num += len(his)
	if len(his) > 0:
		first_day = int(his[0][0][8:10])

	for h in his:
		today = int(h[0][8:10])
		use_skill_times[int(h[0][11:13])] += 1
		use_skill_lens.append(h[1])
		if today > first_day:
			back_again = True

	if back_again:
		next_day_users += 1

print(tot_num)
print(tot_users)
print(next_day_users)
print(use_skill_times)
print(use_skill_lens)

fig = plt.figure('使用时段和使用时长')
period = fig.add_subplot(211)
length = fig.add_subplot(212)
#period.set_title('使用时段')
#length.set_title('使用时长')
period.bar(np.arange(24), use_skill_times, width=0.8, edgecolor='none')
p_labels = list(map(lambda x: '%02d' % x, list(range(24))))
period.set_xticks(np.arange(24))
period.set_xticklabels(p_labels)
# period.set_xlabel('hour')
# period.set_ylabel('times')

length.hist(use_skill_lens, bins=20, width=10)
# length.set_xlabel('time_length')
# length.set_ylabel('times')

plt.show()
