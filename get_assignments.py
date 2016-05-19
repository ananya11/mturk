
ACCESS_ID = access_id
SECRET_KEY = secret_key
HIT_ID = hit
HOST="mechanicalturk.sandbox.amazonaws.com"

from boto.mturk.connection import MTurkConnection
from boto.mturk.question import Question
import csv
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
		                  aws_secret_access_key=SECRET_KEY,
				  host=HOST)

#hits = mtc.get_all_hits()
#with open('hit.txt','w') as hh:
#	for h in hits:
#		print h.HITId
#		hh.write(h.HITId + '\n')

assignments = mtc.get_assignments(HIT_ID, status=None, sort_by='SubmitTime', sort_direction='Ascending', page_size=10, page_number=1, response_groups=None)


with open('assignments.csv','w') as tar:
	csvwriter = csv.writer(tar, delimiter=';', quoting = csv.QUOTE_NONE, quotechar='')	#,escapechar='\\')
	for asgn in assignments:
		row = []
		asgn_id =  asgn.AssignmentId
		print asgn_id
		hit = mtc.get_assignment(asgn_id)
		print hit[1].HITStatus
		for i in range(len(asgn.answers[0])):
			print asgn.answers[0][i].qid + ': ',
			print asgn.answers[0][i].fields[0]

			row.append(asgn.answers[0][i].fields[0])
		csvwriter.writerow(row)
		print row
		print '-----------------'
		
#		for question_form_answer in asgn.answers[0]:
#			print question_form_answer.fields
#			for key, value in question_form_answer.fields:
#				print "%s: %s" % (key,value)



hi = mtc.get_hit(HIT_ID)
print hi.HITId


hits = mtc.get_reviewable_hits(page_size=30, status='Reviewable', sort_by='Expiration', sort_direction='Ascending', page_number=1)

for h in hits:
	print h.HITId
	print h.Question

#print mtc.get_hit(HIT_ID).question[0]
