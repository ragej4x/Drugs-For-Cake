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
		self.x = 400
		self.y = 400
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

	def city_border(self):
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


		border_2 = pg.draw.rect(window,(255,0,255),(196 - player.camera_x ,210 - player.camera_y,2,50),2)
		border_3 = pg.draw.rect(window,(255,0,255),(0 - player.camera_x ,260 - player.camera_y,196,2),2)
		border_4 = pg.draw.rect(window,(255,0,255),(0 - player.camera_x ,210 - player.camera_y,196,2),2)

		if player.hitbox.colliderect(border_2):
			if player.hitbox.left < border_2.right:
				player.x += 1
				player.camera_x = player.x - width//7

		if player.hitbox.colliderect(border_3):
			if player.hitbox.top < border_3.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		if player.hitbox.colliderect(border_4):
			if player.hitbox.bottom > border_4.top:
				player.y -= 1
				player.camera_y = player.y - height//6


		border_5 = pg.draw.rect(window,(255,0,255),(65 - player.camera_x ,210 - player.camera_y,2,140),2)
		border_6 = pg.draw.rect(window,(255,0,255),(0 - player.camera_x ,210 - player.camera_y,67,150),2)
		
		if player.hitbox.colliderect(border_5):
			if player.hitbox.left < border_5.right:
				player.x += 1
				player.camera_x = player.x - width//7	

		if player.hitbox.colliderect(border_6):
			if player.hitbox.top < border_6.bottom:
				player.y += 1
				player.camera_y = player.y - height//6


		border_7 = pg.draw.rect(window,(255,0,255),(158 - player.camera_x ,0 - player.camera_y,2,43),2)
		border_8 = pg.draw.rect(window,(255,0,255),(0 - player.camera_x ,0 - player.camera_y,160,43),2)

		if player.hitbox.colliderect(border_7):
			if player.hitbox.left < border_7.right:
				player.x += 1
				player.camera_x = player.x - width//7

		if player.hitbox.colliderect(border_8):
			if player.hitbox.top < border_7.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_9 = pg.draw.rect(window,(255,0,255),(160 - player.camera_x ,0 - player.camera_y,26,20),2)

		if player.hitbox.colliderect(border_9):
			if player.hitbox.right > border_9.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.top > border_9.top:
				player.y += 1
				player.camera_y = player.y - height//6

		border_10 = pg.draw.rect(window,(255,0,255),(282 - player.camera_x ,0 - player.camera_y,218,43),2)

		if player.hitbox.colliderect(border_10):
			if player.hitbox.right > border_10.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_10.bottom:
				player.y += 1
				player.camera_y = player.y - height//6	

		border_11 = pg.draw.rect(window,(255,0,255),(288 - player.camera_x ,400 - player.camera_y,125,100),2)
		border_12 = pg.draw.rect(window,(255,0,255),(282 - player.camera_x ,400 - player.camera_y,2,100),2)

		if player.hitbox.colliderect(border_11):
			if player.hitbox.left < border_11.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_11.top:
				player.y -= 1
				player.camera_y = player.y - height//6	

		if player.hitbox.colliderect(border_12):
			if player.hitbox.right < border_11.left:
				player.x -= 1
				player.camera_x = player.x - width//7


		border_13 = pg.draw.rect(window,(255,0,255),(451 - player.camera_x ,370 - player.camera_y,49,60),2)

		if player.hitbox.colliderect(border_13):
			if player.hitbox.right < border_13.right:
				player.x -= 1
				player.camera_x = player.x - width//7
			
			if player.hitbox.top < border_13.bottom:
				player.y += 1
				player.camera_y = player.y - height//6	
		
		border_14 = pg.draw.rect(window,(255,0,255),(420 - player.camera_x ,480 - player.camera_y,45,20),2)

		if player.hitbox.colliderect(border_14):
			if player.hitbox.bottom > border_14.top:
				player.y -= 1
				player.camera_y = player.y - height//6

			if player.hitbox.left < border_14.right:
				player.x += 1
				player.camera_x = player.x - width//7

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
	map.city_border()

	event_handler()
	pg.display.flip()
	clock.tick(60)