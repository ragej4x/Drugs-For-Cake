import pygame as pg


width , height = 820,520
display = pg.display.set_mode((width ,height))
pg.display.set_caption("Drugs 4 Cake")
icon = pg.image.load("data/bin/icon.png")
pg.display.set_icon(icon)
window = pg.Surface((width//3 , height//3))
clock = pg.time.Clock()

bg_t = pg.image.load("data/bin/trans.png")
pg.init()

# VARIABLES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
loop = True
disable_movement = False
animation_frame_speed = 0.2

# EVENTHANDER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def event_handler():
	global loop

	for event in pg.event.get():
		if event.type == pg.QUIT:
			loop = False

	surface = pg.transform.scale(window , (width , height))
	display.blit(surface , (0,0))

# PLAYER CLASS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class player_class():
	def __init__(self):
		self.x = 100
		self.y = 300
		self.speed = 1

		self.right = False
		self.left = False
		self.up = False
		self.down = True

		self.camera_x = self.x - width//7
		self.camera_y = self.y - height//6
		self.camera_speed = 1

		self.hitbox = pg.draw.rect(window , (255,0,0), (self.x - self.camera_x , self.y - self.camera_y + 9, 16,24),2)
		# FOR ANIMATION

		self.idle_right_count = 0
		self.idle_left_count = 0
		self.idle_up_count = 0
		self.idle_down_count = 0
		self.idle_right_list = []
		self.idle_left_list = []
		self.idle_up_list = []
		self.idle_down_list = []

		self.run_right_count = 0
		self.run_left_count = 0
		self.run_up_count = 0
		self.run_down_count = 0
		self.run_right_list = []
		self.run_left_list = []
		self.run_up_list = []
		self.run_down_list = []



	def movement(self):
		global keyinput
		keyinput = pg.key.get_pressed()

		if keyinput[pg.K_RIGHT]:
			self.x += self.speed
			self.camera_x += self.speed

			self.right = True
			self.left = False
			self.up = False
			self.down = False

		if keyinput[pg.K_LEFT]:
			self.x -= self.speed
			self.camera_x -= self.speed

			self.left = True
			self.right = False
			self.up = False
			self.down = False

		if keyinput[pg.K_UP]:
			self.y -= self.speed
			self.camera_y -= self.speed

			self.up = True
			self.right = False
			self.left = False
			self.down = False

		if keyinput[pg.K_DOWN]:
			self.y += self.speed
			self.camera_y += self.speed

			self.down = True
			self.right = False
			self.left = False
			self.up = False

		if keyinput[pg.K_RIGHT] == True and keyinput[pg.K_LEFT] == True:
			self.x += self.speed
			self.camera_x += self.speed

			self.right = True
			self.left = False
			self.up = False
			self.down = False


		if keyinput[pg.K_DOWN] == True and keyinput[pg.K_UP] == True:
			self.y += self.speed
			self.camera_y += self.speed

			self.down = True
			self.right = False
			self.left = False
			self.up = False



	def player_mech(self):
		self.hitbox = pg.draw.rect(window , (255,0,0), (self.x - self.camera_x , self.y - self.camera_y + 9, 16,24),2)


# ANIMATION  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	

	#IDLE

	def idle_animation_right(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/id{num}.anim")
			idle_sprite.set_colorkey((255,0,255))
			self.idle_right_list.append(idle_sprite)
			window.blit(self.idle_right_list[int(self.idle_right_count)],(self.x - self.camera_x , self.y - self.camera_y))

	def idle_animation_left(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/id{num}.anim")
			idle_sprite = pg.transform.flip(idle_sprite , True , False)
			idle_sprite.set_colorkey((255,0,255))
			self.idle_left_list.append(idle_sprite)
			window.blit(self.idle_left_list[int(self.idle_left_count)],(self.x - self.camera_x , self.y - self.camera_y))

	def idle_animation_up(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/idU{num}.anim")
			idle_sprite.set_colorkey((255,0,255))
			self.idle_up_list.append(idle_sprite)
			window.blit(self.idle_up_list[int(self.idle_up_count)],(self.x - self.camera_x, self.y - self.camera_y))

	def idle_animation_down(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/idD{num}.anim")
			idle_sprite.set_colorkey((255,0,255))	
			self.idle_down_list.append(idle_sprite)
			window.blit(self.idle_down_list[int(self.idle_down_count)],(self.x - self.camera_x , self.y - self.camera_y))

	#RUN

	def run_animation_right(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/r{num}.anim")
			idle_sprite.set_colorkey((255,0,255))
			self.run_right_list.append(idle_sprite)
			window.blit(self.run_right_list[int(self.run_right_count)], (self.x - self.camera_x , self.y - self.camera_y))

	def run_animation_left(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/r{num}.anim")
			idle_sprite = pg.transform.flip(idle_sprite, True , False)
			idle_sprite.set_colorkey((255,0,255))
			self.run_left_list.append(idle_sprite)
			window.blit(self.run_left_list[int(self.run_left_count)], (self.x - self.camera_x , self.y - self.camera_y))

	def run_animation_up(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/rU{num}.anim")
			idle_sprite.set_colorkey((255,0,255))
			self.run_up_list.append(idle_sprite)
			window.blit(self.run_up_list[int(self.run_up_count)] , (self.x - self.camera_x , self.y - self.camera_y))

	def run_animation_down(self):
		for num in range(1 , 7):
			idle_sprite = pg.image.load(f"data/anim/rD{num}.anim")
			idle_sprite.set_colorkey((255,0,255))
			self.run_down_list.append(idle_sprite)
			window.blit(self.run_down_list[int(self.run_down_count)], (self.x - self.camera_x , self.y - self.camera_y))

player = player_class()

# PLAYER FUNCTION ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def player_function():

	# IDLE 

	if player.right == True and keyinput[pg.K_RIGHT] == False:
		player.idle_right_count += animation_frame_speed
		player.idle_animation_right()

	if player.left == True and keyinput[pg.K_LEFT] == False:
		player.idle_left_count += animation_frame_speed
		player.idle_animation_left()

	if player.up == True and keyinput[pg.K_UP] == False:
		player.idle_up_count += animation_frame_speed
		player.idle_animation_up()

	if player.down == True and keyinput[pg.K_DOWN] == False:
		player.idle_down_count += animation_frame_speed
		player.idle_animation_down()

	# RUN

	if player.right == True and keyinput[pg.K_RIGHT] == True:
		player.run_right_count += animation_frame_speed
		player.run_animation_right()
	
	if player.left == True and keyinput[pg.K_LEFT] == True:
		player.run_left_count += animation_frame_speed
		player.run_animation_left()

	if player.up == True and keyinput[pg.K_UP] == True:
		player.run_up_count += animation_frame_speed
		player.run_animation_up()

	if player.down == True and keyinput[pg.K_DOWN] == True:
		player.run_down_count += animation_frame_speed
		player.run_animation_down()

# MAP CLASS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class map_class():
	def __init__(self):
		self.layer_0 = pg.image.load("data/bin/map/city/layer_0.png")
		self.layer_1 = pg.image.load("data/bin/map/city/layer_1.png")

	def map_layer_0(self):
		window.blit(self.layer_0,(0 - player.camera_x , 0 - player.camera_y))
	def map_layer_1(self):
		window.blit(self.layer_1,(0 - player.camera_x , 0 - player.camera_y))

	# BORDERS

	def border(self):
		# MAP MAIN BORDER

		border_1 = pg.draw.rect(window,(255,0,255),(0 - player.camera_x ,0 - player.camera_y,500,500),2)

		if player.hitbox.left < border_1.left:
			player.x += 1
			player.camera_x = player.x - width//7

		if player.hitbox.right > border_1.right:
			player.x -= 1
			player.camera_x = player.x - width//7

		if player.hitbox.bottom > border_1.bottom:
			player.y -= 1
			player.camera_y = player.y - height//6

		if player.hitbox.top < border_1.top:
			player.y += 1
			player.camera_y = player.y - height//6			

map = map_class()

# MAINLOOP +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

while loop == True:
	
	window.fill((30,30,30))
	#window.blit(bg_t,(0 - player.camera_x , 0 - player.camera_y))
	if disable_movement == False:
		player.movement()

	map.map_layer_0()
	player_function()
	map.map_layer_1()
	player.player_mech()
	map.border()

	event_handler()
	pg.display.flip()
	clock.tick(60)