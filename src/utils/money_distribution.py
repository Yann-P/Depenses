# @author Yann Pellegrini
# @licence GPLv3

from random import randint
import time

def _total(expenditures):
	total = 0
	for n in expenditures:
		total += n
	return total

# @return distance to average.
def _delta(n, avg):
	return n - avg

# @return distance to avg for everybody
def _get_deltas(expenditures, n, avg):
	deltas = [0] * n
	for i, n in enumerate(expenditures):
		deltas[i] = _delta(expenditures[i], avg)
	return deltas


def _get_due_amount(expenditures, deltas, paid_most, paid_least):
	return min(
			deltas[paid_most], 
			abs(expenditures[paid_most] - expenditures[paid_least]) / 2
		)

# @brief You have expenditures in common. This function takes who paid how much and returns 
# the reimbursments that are necessary between the members of the group, so that everybody spent the same amount of money.
# @param expenditures array of reals. ex. [25, 2, 3] : user1 spent 25€, ..., user3 spent 3€.
# @return a matrix that tells who owes how much to who (a owes x euros to b => M[a][b] = x)
def get_money_distribution(expenditures):
	n = len(expenditures) # Number of persons in the group.
	total = _total(expenditures) # Total spent by the group.
	avg = total / n
	due = [[0] * n for i in range(n)] # matrix (a owes x euros to b => M[a][b] = x)

	for i in range(100): # Should be while True, this is a failsafe. Usually the result is found before 2n iterations

		deltas = _get_deltas(expenditures, n, avg) # distance to avg for everybody

		if(deltas.count(0) >= n - 1):
			break

		paid_least = deltas.index(min(deltas))
		paid_most = deltas.index(max(deltas))

		due_amount = _get_due_amount(expenditures, deltas, paid_most, paid_least)

		due[paid_least][paid_most] += due_amount

		expenditures[paid_least] += due_amount
		expenditures[paid_most] -= due_amount

	return due