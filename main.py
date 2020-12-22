from tkinter import *
import random
from tkinter.font import Font
from functools import partial
import time

root = Tk()
root.title('2048')
root.geometry('450x450')
root.config(bg='white')

def move(k, e):
	global untouch, num_grid
	if k=='d':
		for i in range(4):
			c = dict(enumerate([j for j in num_grid[i] if j][::-1]))
			for j in range(len(c), 4): c[j] = 0
			for j in range(3):
				if c[j] == c[j+1]:
					c[j] = c[j]*2
					c[j+1] = 0
			c = [j for j in c.values() if j]
			c = (c+[0]*(4-len(c)))[::-1]
			num_grid[i] = c
		[[grid[i][j].config(text=num_grid[i][j] if num_grid[i][j] else '', bg=color[num_grid[i][j]] if num_grid[i][j] else 'grey88') for j in range(4)] for i in range(4)]
		untouch = [(i, j) for i in range(4) for j in range(4) if not num_grid[i][j]]
	if k=='a':
		for i in range(4):
			c = dict(enumerate([j for j in num_grid[i] if j][::-1]))
			for j in range(len(c), 4): c[j] = 0
			for j in range(3):
				if c[j] == c[j+1]:
					c[j] = c[j]*2
					c[j+1] = 0
			c = [j for j in c.values() if j]
			c = ([0]*(4-len(c))+c)[::-1]
			num_grid[i] = c
		[[grid[i][j].config(text=num_grid[i][j] if num_grid[i][j] else '', bg=color[num_grid[i][j]] if num_grid[i][j] else 'grey88') for j in range(4)] for i in range(4)]
		untouch = [(i, j) for i in range(4) for j in range(4) if not num_grid[i][j]]
	if k=='w':
		t = list(zip(*num_grid))
		for i in range(4):
			c = dict(enumerate([j for j in t[i] if j][::-1]))
			for j in range(len(c), 4): c[j] = 0
			for j in range(3):
				if c[j] == c[j+1]:
					c[j] = c[j]*2
					c[j+1] = 0
			c = [j for j in c.values() if j]
			c = ([0]*(4-len(c))+c)[::-1]
			t[i] = c
		num_grid = [list(i) for i in zip(*t)]
		[[grid[i][j].config(text=num_grid[i][j] if num_grid[i][j] else '', bg=color[num_grid[i][j]] if num_grid[i][j] else 'grey88') for j in range(4)] for i in range(4)]
		untouch = [(i, j) for i in range(4) for j in range(4) if not num_grid[i][j]]
	if k=='s':
		t = list(zip(*num_grid))
		for i in range(4):
			c = dict(enumerate([j for j in t[i] if j][::-1]))
			for j in range(len(c), 4): c[j] = 0
			for j in range(3):
				if c[j] == c[j+1]:
					c[j] = c[j]*2
					c[j+1] = 0
			c = [j for j in c.values() if j]
			c = (c+[0]*(4-len(c)))[::-1]
			t[i] = c
		num_grid = [list(i) for i in zip(*t)]
		[[grid[i][j].config(text=num_grid[i][j] if num_grid[i][j] else '', bg=color[num_grid[i][j]] if num_grid[i][j] else 'grey88') for j in range(4)] for i in range(4)]
		untouch = [(i, j) for i in range(4) for j in range(4) if not num_grid[i][j]]
	root.update()
	time.sleep(0.25)
	if untouch:
		new = random.choice(untouch)
		new_num = random.choice([2, 4])
		untouch.remove(new)
		num_grid[new[0]][new[1]] = new_num
		grid[new[0]][new[1]].config(text=new_num, bg=color[new_num])



untouch = [(i, j) for i in range(4) for j in range(4)]
color_hex = ['#050f2c', '#003666', '#00aeff', '#3369e7', '#8e43e7', '#b84592', '#ff4f81', '#ff6c5f', '#ffc168', '#2dde98', '#1cc7d0']
color = {2**i:color_hex[i] for i in range(len(color_hex))}

num_grid = [[0 for j in range(4)] for i in range(4)]
random_start = random.choice(untouch)
num_grid[random_start[0]][random_start[1]] = random.choice([2, 4])
grid = [[Label(root, text=num_grid[i][j] if num_grid[i][j] else '', bg=color[num_grid[i][j]] if num_grid[i][j] else 'grey88', fg='white', justify=CENTER, font=Font(family='Clear Sans Medium', size=28)) for j in range(4)] for i in range(4)]
untouch.remove(random_start)

for i in range(4):
	for j in range(4):
		grid[i][j].place(y=i*100+30, x=j*100+30, width=90, height=90)

for i in 'wasd':
	temp_func = partial(move, i)
	root.bind(f'<{i}>', temp_func)

root.mainloop()