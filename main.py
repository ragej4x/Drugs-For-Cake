import pygame as pg
import random

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

rv = False
gv = False
bv = False
r , g , b = 0,0,0

# EVENTHANDER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def event_handler():
	global loop

	for event in pg.event.get():
		if event.type == pg.QUIT:
			loop = False

	surface = pg.transform.scale(window , (width , height))
	display.blit(surface , (0,0))

# DISPLAY FPS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def display_fps():
	font = pg.font.Font("data/bin/font" , 18, bold = True)
	get_fps = str(int(clock.get_fps()))
	blit_fps = font.render(get_fps , True , (255,255,255))
	display.blit(blit_fps , (5,5))

# PLAYER CLASS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class player_class():
	def __init__(self):
		self.x = 481
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
		self.layer_0 = pg.image.load("data/bin/map/city/layer_0.map")
		self.layer_1 = pg.image.load("data/bin/map/city/layer_1.map")

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

			if player.hitbox.left < border_14.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_14.top:
				player.y -= 1
				player.camera_y = player.y - height//6

		border_15 = pg.draw.rect(window,(255,0,255),(199 - player.camera_x ,357 - player.camera_y,1,143),2)
		border_16 = pg.draw.rect(window,(255,0,255),(195 - player.camera_x ,357 - player.camera_y,1,143),2)

		if player.hitbox.colliderect(border_15):
			if player.hitbox.left < border_15.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_15.top:
				player.y -= 1
				player.camera_y = player.y - height//6	

		if player.hitbox.colliderect(border_16):
			if player.hitbox.right > border_16.left:
				player.x -= 1
				player.camera_x = player.x - width//7

		border_17 = pg.draw.rect(window,(255,0,255),(16 - player.camera_x ,413 - player.camera_y,5,5),2)
		border_18 = pg.draw.rect(window,(255,0,255),(13 - player.camera_x ,415 - player.camera_y,5,5),2)

		if player.hitbox.colliderect(border_17):
			if player.hitbox.left < border_17.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_17.top:
				player.y -= 1
				player.camera_y = player.y - height//6	

		if player.hitbox.colliderect(border_18):
			if player.hitbox.top < border_18.bottom:
				player.y += 1
				player.camera_y = player.y - height//6	

		border_19 = pg.draw.rect(window,(255,0,255),(73 - player.camera_x ,478 - player.camera_y,5,5),2)
		border_20 = pg.draw.rect(window,(255,0,255),(70 - player.camera_x ,480 - player.camera_y,5,5),2)


		if player.hitbox.colliderect(border_19):
			if player.hitbox.left < border_19.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_19.top:
				player.y -= 1
				player.camera_y = player.y - height//6	

		if player.hitbox.colliderect(border_20):

			if player.hitbox.right > border_20.left:
				player.x -= 1
				player.camera_x = player.x - width//7

		border_21 = pg.draw.rect(window,(255,0,255),(164 - player.camera_x ,480 - player.camera_y,5,5),2)
		border_22 = pg.draw.rect(window,(255,0,255),(161 - player.camera_x ,482 - player.camera_y,5,5),2)


		if player.hitbox.colliderect(border_21):
			if player.hitbox.left < border_21.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_19.top:
				player.y -= 1
				player.camera_y = player.y - height//6	

		if player.hitbox.colliderect(border_22):

			if player.hitbox.right > border_22.left:
				player.x -= 1
				player.camera_x = player.x - width//7

		border_23 = pg.draw.rect(window,(255,0,255),(38 - player.camera_x ,385 - player.camera_y,5,43),2)
		border_24 = pg.draw.rect(window,(255,0,255),(45 - player.camera_x ,387 - player.camera_y,5,45),2)
		
		if player.hitbox.colliderect(border_23):
			if player.hitbox.right > border_23.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_23.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_24):

			if player.hitbox.left < border_24.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_24.bottom:
				player.y += 1
				player.camera_y = player.y - height//6	

		border_25 = pg.draw.rect(window,(255,0,255),(273 - player.camera_x ,383 - player.camera_y,5,5),2)
		border_26 = pg.draw.rect(window,(255,0,255),(270 - player.camera_x ,385 - player.camera_y,5,5),2)
		
		if player.hitbox.colliderect(border_25):
			if player.hitbox.left < border_25.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_25.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_26):

			if player.hitbox.right > border_26.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_26.bottom:
				player.y += 1
				player.camera_y = player.y - height//6	

		border_27 = pg.draw.rect(window,(255,0,255),(273 - player.camera_x ,223 - player.camera_y,5,5),2)
		border_28 = pg.draw.rect(window,(255,0,255),(270 - player.camera_x ,225 - player.camera_y,5,5),2)
		
		if player.hitbox.colliderect(border_27):
			if player.hitbox.left < border_27.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_27.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_28):

			if player.hitbox.right > border_28.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_28.bottom:
				player.y += 1
				player.camera_y = player.y - height//6	
		

		border_29 = pg.draw.rect(window,(255,0,255),(273 - player.camera_x ,143 - player.camera_y,5,5),2)
		border_30 = pg.draw.rect(window,(255,0,255),(270 - player.camera_x ,145 - player.camera_y,5,5),2)
		
		if player.hitbox.colliderect(border_29):
			if player.hitbox.left < border_29.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_29.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_30):

			if player.hitbox.right > border_30.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_30.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_31 = pg.draw.rect(window,(255,0,255),(401 - player.camera_x ,143 - player.camera_y,5,5),2)
		border_32 = pg.draw.rect(window,(255,0,255),(398 - player.camera_x ,145 - player.camera_y,5,5),2)
		
		if player.hitbox.colliderect(border_31):
			if player.hitbox.left < border_31.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_31.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_32):

			if player.hitbox.right > border_32.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_32.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_33 = pg.draw.rect(window,(255,0,255),(401 - player.camera_x ,68 - player.camera_y,5,5),2)
		border_34 = pg.draw.rect(window,(255,0,255),(398 - player.camera_x ,69 - player.camera_y,5,5),2)
		
		if player.hitbox.colliderect(border_33):
			if player.hitbox.left < border_33.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_33.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_34):

			if player.hitbox.right > border_34.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_34.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_35 = pg.draw.rect(window,(255,0,255),(273 - player.camera_x ,65 - player.camera_y,5,5),2)
		border_36 = pg.draw.rect(window,(255,0,255),(270 - player.camera_x ,67 - player.camera_y,5,5),2)

		if player.hitbox.colliderect(border_35):
			if player.hitbox.left < border_35.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_35.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_36):

			if player.hitbox.right > border_36.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_36.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_37 = pg.draw.rect(window,(255,0,255),(193 - player.camera_x ,64 - player.camera_y,5,5),2)
		border_38 = pg.draw.rect(window,(255,0,255),(190 - player.camera_x ,65 - player.camera_y,5,5),2)
		
		if player.hitbox.colliderect(border_37):
			if player.hitbox.left < border_37.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_37.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_38):

			if player.hitbox.right > border_38.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_38.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_39 = pg.draw.rect(window,(255,0,255),(96 - player.camera_x ,67 - player.camera_y,5,5),2)
		border_40 = pg.draw.rect(window,(255,0,255),(93 - player.camera_x ,68 - player.camera_y,5,5),2)
	
		if player.hitbox.colliderect(border_39):
			if player.hitbox.left < border_39.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_39.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_40):

			if player.hitbox.right > border_40.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_40.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_41 = pg.draw.rect(window,(255,0,255),(96 - player.camera_x ,145 - player.camera_y,5,5),2)
		border_42 = pg.draw.rect(window,(255,0,255),(93 - player.camera_x ,146 - player.camera_y,5,5),2)
	
		if player.hitbox.colliderect(border_41):
			if player.hitbox.left < border_41.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_41.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_42):

			if player.hitbox.right > border_42.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_42.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_43 = pg.draw.rect(window,(255,0,255),(193 - player.camera_x ,145 - player.camera_y,5,5),2)
		border_44 = pg.draw.rect(window,(255,0,255),(190 - player.camera_x ,146 - player.camera_y,5,5),2)

		if player.hitbox.colliderect(border_43):
			if player.hitbox.left < border_43.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_43.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_44):

			if player.hitbox.right > border_44.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_44.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_45 = pg.draw.rect(window,(255,0,255),(119 - player.camera_x ,455 - player.camera_y,5,5),2)
		border_46 = pg.draw.rect(window,(255,0,255),(118 - player.camera_x ,456 - player.camera_y,5,5),2)

		if player.hitbox.colliderect(border_45):
			if player.hitbox.left < border_45.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_45.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_46):

			if player.hitbox.right > border_46.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_46.bottom:
				player.y += 1
				player.camera_y = player.y - height//6

		border_47 = pg.draw.rect(window,(255,0,255),(300 - player.camera_x ,182 - player.camera_y,200,165),2)
		border_48 = pg.draw.rect(window,(255,0,255),(294 - player.camera_x ,185 - player.camera_y,204,170),2)

		if player.hitbox.colliderect(border_47):
			if player.hitbox.left < border_47.right:
				player.x += 1
				player.camera_x = player.x - width//7

			if player.hitbox.bottom > border_47.top:
				player.y -= 1
				player.camera_y = player.y - height//6	


		if player.hitbox.colliderect(border_48):

			if player.hitbox.right > border_48.left:
				player.x -= 1
				player.camera_x = player.x - width//7

			if player.hitbox.top < border_48.bottom:
				player.y += 1
				player.camera_y = player.y - height//6


	def collider(self):

		collider_1 = pg.draw.rect(window,(255,0,0),(0 - player.camera_x ,160 - player.camera_y,125,50),2)
		collider_2 = pg.draw.rect(window,(255,0,0),(125 - player.camera_x ,195 - player.camera_y,70,15),2)
		collider_3 = pg.draw.rect(window,(255,0,0),(350 - player.camera_x ,380- player.camera_y,62,20),2)
		collider_4 = pg.draw.rect(window,(255,0,0),(282 - player.camera_x ,375 - player.camera_y,64,25),2)

		if not player.hitbox.colliderect(collider_1):
			self.layer_1.set_alpha((255))

		if not player.hitbox.colliderect(collider_2):
			self.layer_1.set_alpha((255))

		if not player.hitbox.colliderect(collider_3):
			self.layer_1.set_alpha((255))

		if not player.hitbox.colliderect(collider_4):
			self.layer_1.set_alpha((255))

		if player.hitbox.colliderect(collider_1):
			self.layer_1.set_alpha((50))

		if player.hitbox.colliderect(collider_2):
			self.layer_1.set_alpha((50))

		if player.hitbox.colliderect(collider_3):
			self.layer_1.set_alpha((50))

		if player.hitbox.colliderect(collider_4):
			self.layer_1.set_alpha((50))

		print(player.x , player.y)

map = map_class()

# NPC CLASS
class npc_class():
	def __init__(self):
		self.gaza_x = 0
		self.gaza_y = 0


	def update_npc(self):
		pass
		#gaza_rect = pg.draw.rect()

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
	map.collider()


	event_handler()
	display_fps()
	pg.display.flip()
	clock.tick(60)