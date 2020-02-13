input = open("input.txt","r").readline

M = int(input())

mat = [[0 for n in range(M+1)] for i in range(M+1)]
#the number of edges is equal to number of pairs of corners
for i in range(M):
	inp = list(map(int,input().strip().split()))
	ep = inp[0]
	c = inp[1:1+ep]
	e = inp[1+ep:]


		