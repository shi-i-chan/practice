# Sep 2020

# IDE Sublime Text

# PIL 7.2.0
# Numpy 1.22.3
# Matplotlib 3.4.1

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

import PIL
import numpy
import matplotlib

lab1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
		[1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], 
		[1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1], 
		[1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
		[1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

MAP = lab1
x_len = len(MAP)
y_len = len(MAP[0])

def refill_map():
	the_map = np.zeros((x_len, y_len))
	for i in range(0, x_len):
		for j in range(0, y_len):
			the_map[i][j] = 99
	return the_map 

class queue:
	def __init__(self):
		self.queue = []
	
	def sett(self, element):
		self.queue.append(element)
		
	def gett(self):
		return(self.queue[0])
		
	def remove(self):
		self.queue.pop(0)
		
	def get_len(self):
		return len(self.queue)
		
	def check(self, vertex):
		if vertex in self.queue:
			return(0)
		else:
			return(1)

class dijkstra:
	def __init__(self, start_point, end_point, queue, graph):
		self.points_queue = queue
		self.graph = graph
		self.start_point = start_point
		self.end_point = end_point
		self.vek = {}
		self.slow = {}
	
	def get_dis(self):
		self.vek[str(self.start_point)] = 0
		self.slow[str(self.start_point)] = self.start_point
		self.points_queue.sett(self.start_point)
		while(self.points_queue.get_len() != 0):
			for i in range(1, len(self.graph.dict[str(self.points_queue.gett())])):
				lst = list(self.graph.dict[str(self.points_queue.gett())].keys())
				if lst[i] in self.vek:
					if self.vek[str(lst[i])] > self.graph.dict[str(self.points_queue.gett())][str(lst[i])]["len"] + self.vek[str(self.points_queue.gett())]:
						self.vek[str(lst[i])] = self.graph.dict[str(lst[i])] + self.vek[str(self.points_queue.gett())]
						self.slow[str(lst[i])] = lst[i]
				else:
					self.vek[str(lst[i])] = self.graph.dict[str(self.points_queue.gett())][str(lst[i])]["len"] + self.vek[str(self.points_queue.gett())]
					self.slow[str(lst[i])] = self.points_queue.gett()
					if self.points_queue.check(lst[i]):
						self.points_queue.sett(lst[i])
			self.points_queue.remove()
		now = self.end_point
		path = []
		path.append(self.end_point)
		while(now != self.start_point):
			path.append(self.slow[str(now)])
			now = self.slow[str(now)]
		return(path)

class Graph:
	def __init__(self):
		self.num = 2
		self.dict = {}
		self.dict ["1"] = {
				"values": {
						"name": 1,
						"busy": 1,
						"flag": 1,
						"x": 1,
						"y": 3
						},
				"2": {
					"len": 1,
					"dir": 2
					},
				
				}
		self.dict ["2"] = {
				"values": {
						"name": 2,
						"busy": 0,
						"flag": 0,
						"x": 0,
						"y": 0
						},
				"1": {
					"len": 0,
					"dir": 0
					}
				}
	
	def make_new_vertexes(self, walls, current_maze):
		for direction in range(0, 4):
			if walls[direction] != 0:
				self.dict[str(current_maze)][str(len(self.dict) + 1)] = {
						"len": 1,
						"dir": direction
						}
				self.dict[str(len(self.dict) + 1)] = {
						"values":{
								"name": self.num + 1,
								"busy": 0,
								"flag": 0,
								"x": 0,
								"y": 0
								},
						str(current_maze):{
								"len": 1,
								"dir": self.decoder(direction)
								}
						}
				self.num += 1
	
	def decoder(self, direction):
		if direction == 0:
			return(2)
		elif direction == 1:
			return(3)
		elif direction == 2:
			return(0)
		elif direction == 3:
			return(1)
		   
	def printing(self):
		string = ""
		for i in self.dict.keys():
			string += ("\n{0}: ".format(i)).ljust(5)
			for j in range(1, len(self.dict[str(i)])):
				if self.dict[str(list(self.dict[str(i)])[j])]["values"]["flag"] == 0:
					string += " !!!{0} - ({1})".format(list(self.dict[str(i)])[j], self.dict[str(i)][str(list(self.dict[str(i)])[j])]["len"])  
				else:
					string += " {0} - ({1})".format(list(self.dict[str(i)])[j], self.dict[str(i)][str(list(self.dict[str(i)])[j])]["len"])
		return(string)
		
class Agent:
	def __init__(self, name, x, y, all_map, graph, the_map):
		self.name = name
		self.x = x
		self.y = y
		self.graph = graph
		self.steps = 0
		self.tasks = 0
		self.all_map = all_map
		self.the_map = the_map
		self.task_list = []
		self.current_maze = 1
		self.current_task = 0
		self.go_to_place = 0
		self.place_path = []
		self.stay()
		
	def stay(self):
		self.the_map[self.x][self.y] = 2
	
	def start_move(self):
		if self.current_task == 0:
			self.get_new_task()
			if self.current_task != 0:
				self.get_get()
		else:
			if self.go_to_place == 0:
				walls = self.check_wall()
				if np.sum(walls) == 1 and walls.tolist().index(1) == self.graph.dict[str(self.current_maze)][str(self.current_task)]["dir"]: 
					self.move(walls.tolist().index(1))
					self.fill_ver_len()
				
				elif (np.sum(walls) == 1 and walls.tolist().index(1) != self.graph.dict[str(self.current_maze)][str(self.current_task)]["dir"]) or np.sum(walls) > 1: 
					self.current_maze = self.current_task
					self.fill_flag()
					self.graph.make_new_vertexes(walls, self.current_maze)
					self.get_new_task()
					if self.current_task != 0:
						self.get_get()
				
				elif np.sum(walls) == 0:
					self.fill_flag()
					self.current_maze = self.current_task
					self.get_new_task()
					if self.current_task != 0:
						 self.get_get()
			else:
				if len(self.place_path) > 0:
					self.move(self.place_path[0])
					self.place_path.pop(0)
				else:
					self.go_to_place = 0
					self.start_move()
							   
	def get_get(self):
		di = dijkstra(self.current_maze, self.current_task, queue, self.graph)
		self.place_path = self.fill_place_path(di.get_dis())
		self.go_to_place = 1  
		self.start_move()
	
	def fill_place_path(self, dij_path):
		dij_path = dij_path[::-1]
		move_list = []
		for i in range(0, len(dij_path) - 1):
			direction = self.graph.dict[str(dij_path[i])][str(dij_path[i + 1])]["dir"]
			length = self.graph.dict[str(dij_path[i])][str(dij_path[i + 1])]["len"]
			for j in range(0, length):
				move_list.append(direction)
		self.current_maze = dij_path[-2]
		return(move_list)
	
	def get_new_task(self):
		for i in range(1, len(self.graph.dict) + 1):
			if self.graph.dict[str(i)]["values"]["flag"] == 0:
				if self.graph.dict[str(i)]["values"]["busy"] == 0:
					self.current_task = i
					self.graph.dict[str(i)]["values"]["busy"] = 1
					self.tasks += 1
					break;
			else:
				self.current_task = 0
				self.done = 1
	
	def fill_ver_len(self):
		self.graph.dict[str(self.current_maze)][str(self.current_task)]["len"] += 1
		self.graph.dict[str(self.current_task)][str(self.current_maze)]["len"] += 1
	
	def fill_flag(self):
		self.graph.dict[str(self.current_maze)]["values"]["flag"] = 1
		self.graph.dict[str(self.current_task)]["values"]["x"] = self.x
		self.graph.dict[str(self.current_task)]["values"]["y"] = self.y
		self.graph.dict[str(self.current_task)]["values"]["flag"] = 1
	 
	def check_wall(self):
		walls = np.array([0, 0, 0, 0])
		if self.all_map[self.x - 1][self.y] == 0 and self.the_map[self.x - 1][self.y] != 2: # top
			walls[0] = "1"
		if self.all_map[self.x][self.y - 1] == 0 and self.the_map[self.x][self.y - 1] != 2: # left
			walls[1] = "1"
		if self.all_map[self.x + 1][self.y] == 0 and self.the_map[self.x + 1][self.y] != 2: # bottom
			walls[2] = "1"
		if self.all_map[self.x][self.y + 1] == 0 and self.the_map[self.x][self.y + 1] != 2: # right
			walls[3] = "1"
		return(walls)

	def move(self, dir):
		if dir != 9:
			if dir == 0:
				self.x = self.x - 1
			elif dir == 1:
				self.y = self.y - 1
			elif dir == 2:
				self.x = self.x + 1
			elif dir == 3:
				self.y = self.y + 1
			self.stay()
			self.steps += 1
 
def draw(agents, the_map):
	factor = 30
	# Code to show graph in animation
	#image = Image.new('RGB', (y_len*factor + 300, x_len*factor + 350), color = 'gray')
	image = Image.new('RGB', (y_len*factor, x_len*factor), color = 'gray')
	ima = ImageDraw.Draw(image)
	for i in range(0, x_len):
		for j in range(0, y_len):
			if MAP[i][j] == 1:
				ima.rectangle((
				(j*factor, i*factor), ((j+1)*factor, (i+1)*factor))
				, fill="black"
				)
	for i in range(0, x_len):
		for j in range(0, y_len):
			if the_map[i][j] == 2:
				ima.rectangle((
				(j*factor, i*factor), ((j+1)*factor, (i+1)*factor))
				, fill="green"
				)
	for i in range(0, x_len):
		ima.line([(0, i*factor), (y_len*factor, i*factor)])
	for i in range(0, y_len):
		ima.line([(i*factor, 0), (i*factor, x_len*factor)])

	for i in agents[0].graph.dict.values():
		if int(i["values"]["y"]) != 0:
			ima.text((i["values"]["y"]*factor + 3, i["values"]["x"]*factor + 3), str(i["values"]["name"]))

	for i in agents:
		ima.rectangle((
		(i.y*factor, i.x*factor), ((i.y+1)*factor, (i.x+1)*factor))
		, fill="red"
		)
		ima.text((i.y*factor + 3, i.x*factor + 3), str(i.name))
	# Code to show graph in animation
	# ima.text((y_len*factor + 10, 0), 
	# 		 agents[0].graph.printing()
	# 		 )
	return(image)

def plot_charts():
	steps_list = []
	for agents_num in range(1, 11):
		gr = Graph()
		done = 0
		steps = 0
		agents = []
		agents_steps = []
		agents_tasks = []
		the_map = refill_map()
		for k in range(1, agents_num + 1):
			agents.append(Agent(k, 1, 3, MAP, gr, the_map))
		while (done != 1):
			for i in range(agents_num):
				agents[i].start_move()
			cur_len = 0
			agents_steps = []
			for n in range(agents_num):
				if agents[n].current_task == 0:
					cur_len += 1
			if cur_len == agents_num:
				done = 1
				break;
			steps = steps + 1
		for n in range(agents_num):
			agents_steps.append(agents[n].steps)
			agents_tasks.append(agents[n].tasks)
		steps_list.append(steps)  
		xxx = list(range(1, agents_num + 1))
		plt.bar(xxx, agents_steps, align='center', alpha=0.5)
		plt.xticks(xxx, xxx)
		plt.ylabel('Number of movements')
		plt.title('Robot number')
		plt.savefig('D:agents_steps{0}.jpg'.format(agents_num))
		plt.close()
		plt.bar(xxx, agents_tasks, align='center', alpha=0.5)
		plt.xticks(xxx, xxx)
		plt.ylabel('Number of completed tasks')
		plt.title('Robot number')
		plt.savefig('D:agents_tasks{0}.jpg'.format(agents_num))
		plt.close()
	plt.bar(xxx, steps_list, align='center', alpha=0.5)
	plt.xticks(xxx, xxx)
	plt.ylabel('Itterations')
	plt.title('Number of robots')
	plt.savefig('D:steps.jpg')
	plt.close()
	
def plot_animation(agents_num):
	dpi = 100
	im_width, im_height = 600, 240
	figsize = im_width / float(dpi), im_height / float(dpi)
	fig = plt.figure(figsize=figsize)
	ima = []	
	done = 0
	agents = []
	the_map = refill_map()
	for k in range(1, agents_num + 1):
		agents.append(Agent(k, 1, 3, MAP, gr, the_map))
	while (done != 1):
		for i in range(agents_num):
			agents[i].start_move()
		cur_len = 0
		for n in range(agents_num):
			if agents[n].current_task == 0:
				cur_len += 1
		if cur_len == agents_num:
			done = 1
			break;
		image = draw(agents, the_map)
		im = plt.imshow(image, animated=True)
		plt.tight_layout()
		plt.axis('off')
		ima.append([im])
	Animation = animation.ArtistAnimation(fig, ima, interval=300, blit=True, repeat_delay=1000)
	Animation.save('animation without graph.gif', writer='imagemagick', fps=60)
	plt.show()

queue = queue()
gr = Graph()

#plot_charts() # make plots
plot_animation(8) # make animation