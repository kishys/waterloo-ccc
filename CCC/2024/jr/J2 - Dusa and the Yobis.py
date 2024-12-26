# Kishan Suhi
# CCC - '24 J2: Dusa and the Yobis

dusa=int(input())
a=1
while a != dusa:
	yobis=int(input())
	a+=1
	if dusa > yobis:
		dusa+=yobis
	elif dusa <= yobis:
		print(dusa)
		break