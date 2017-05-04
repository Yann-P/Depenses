# @author Yann Pellegrini
# @licence GPLv3

from random import randint
import time

def _total(expenditures):
	total = 0
	for n in expenditures:
		total += n
	return total

def _delta(n, avg):
	return n - avg

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

def get_money_distribution(expenditures):
	n = len(expenditures) # Number of persons in the group.
	total = _total(expenditures) # Total spent by the group.
	avg = total / n
	due = [[0] * n for i in range(n)]

	for i in range(100):
		deltas = _get_deltas(expenditures, n, avg)

		if(deltas.count(0) >= n - 1):
			break

		paid_least = deltas.index(min(deltas))
		paid_most = deltas.index(max(deltas))

		due_amount = _get_due_amount(expenditures, deltas, paid_most, paid_least)

		due[paid_least][paid_most] += due_amount

		expenditures[paid_least] += due_amount
		expenditures[paid_most] -= due_amount

	return due



# tests

# if __name__ == '__main__':
# 	while True:
# 		print("_____________")
# 		dist = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
# 		print(dist)
# 		print(get_money_distribution(dist))
# 		print("_____________")