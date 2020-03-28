def data(x1,y1,x2,y2):
	global x_min,x_max,y_min,y_max
	x_min=x1
	x_max=x2
	y_min=y1
	y_max=y2
def clipl(x1,y1,x2,y2):
		
	if x2 - x1 !=0 :
		m=(y2 - y1)/(x2 - x1)
	else:
		m=4000
	if x1 >= x_min and x2 >= x_min:
		
		x_new.append(x2)
		y_new.append(y2)
		
	elif x1 < x_min and x2 >= x_min:
		
		x_new.append(x_min)
		y_new.append(y1+ m*(x_min - x1))
		x_new.append(x2)
		y_new.append(y2)

	elif x1 >= x_min and x2 < x_min :
		
		x_new.append(x_min)
		y_new.append(y1 + m*(x_min - x1))
	
def clipr(x1,y1,x2,y2):
	if x2 - x1 !=0 :
		m=(y2 - y1)/(x2 - x1)
	else:
		m=4000

	if x1 <= x_max and x2 <= x_max:
		
		x_newr.append(x2)
		y_newr.append(y2)
		
	elif x1 > x_max and x2 <= x_max:
		
		x_newr.append(x_max)
		y_newr.append(y1+ m*(x_max - x1))
		x_newr.append(x2)
		y_newr.append(y2)

		
	elif x1 <= x_max and x2 > x_max :
		x_newr.append(x_max)
		y_newr.append(y1 + m*(x_max - x1))
	

def clipt(x1,y1,x2,y2):
	if (y2-y1)!=0:
		m=(x2-x1)/(y2-y1)
	else:
		m=4000
	if y1 <= y_max and y2<= y_max:
		x_newt.append(x2)
		y_newt.append(y2)
	elif y1 > y_max and y2 <= y_max:
		x_newt.append(x1+m*(y_max-y1))
		y_newt.append(y_max)
		x_newt.append(x2)
		y_newt.append(y2)

	elif y1 <= y_max and y2 > y_max:
		x_newt.append(x1+m*(y_max -y1))
		y_newt.append(y_max)


def clipb(x1,y1,x2,y2):
	if (y2-y1)!=0:
		m=(x2-x1)/(y2-y1)
	else:
		m=4000
	if y1 >= y_min and y2>= y_min:
		x_newb.append(x2)
		y_newb.append(y2)
	elif y1 < y_min and y2 >= y_min:
		x_newb.append(x1+m*(y_min-y1))
		y_newb.append(y_min)
		x_newb.append(x2)
		y_newb.append(y2)

	elif y1 >= y_min and y2 < y_min:
		x_newb.append(x1+m*(y_min -y1))
		y_newb.append(y_min)
