class npc_class():
	def __init__(self):
		self.txt_animation = 0
		self.font = pg.font.Font("data/bin/font" , 20, bold = True)
		self.diag_box = pg.image.load("data/bin/asset/diag_box.asset")
		self.speed = 5

		self.narr_diag_1 = False

		self.player_diag_1 = False
		self.player_diag_2 = False
		self.player_diag_3 = False
		self.player_diag_4 = False
		self.player_diag_5 = False
		self.player_diag_6 = False

		self.strger_diag_1 = False
		self.strger_diag_2 = False
		self.strger_diag_3 = False
		self.strger_diag_4 = False
		self.strger_diag_5 = False

		# CAR VAR
		self.car = {"car_left":False , "car_right":False , "car_up":False , "car_down":False}
		self.cooldown = 0
		self.spawn = False
		self.selector = random.randint(0,3)
		self.car_x , self.car_y = 0,0



	def update_npc(self):
		jubirt_rect = pg.draw.rect(window,(0,0,200), (500 - player.camera_x ,500 - player.camera_y , 30,30))
	

	def diag(self):
		font = pg.font.Font("data/bin/font" , 10, bold = True)
		skip = font.render("PRESS : L_SHIFT TO SKIP.",True , (30,30,30))
		enter = font.render("PRESS : ENTER TO CONTINUE.",True ,(30,30,30))
		
		# NARRATOR DIAG 1 ++++++++++++++++++++++++++++++++++++++++++++++++++++

		if self.narr_diag_1 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))

			narr_diag_1 = {"diag_1":"Tomorrow is Roshela's birthday and you need to buy a cake for her 16th birthday",
			"diag_2":"but you dont have any money."}
			
			narr_diag_txt_1 = self.font.render(narr_diag_1["diag_1"][0:self.txt_animation//self.speed], True ,(30,30,30))
			
			display.blit(narr_diag_txt_1,(5,405))

			if  self.txt_animation >= len(narr_diag_1["diag_1"]) + 150:
				narr_diag_txt_1 = self.font.render(narr_diag_1["diag_2"][0:self.txt_animation//self.speed - 120], True ,(30,30,30))
				display.blit(narr_diag_txt_1,(5,435))
				
				if self.txt_animation >= len(narr_diag_1["diag_2"]) + 560:
					self.txt_animation = 10000

			self.txt_animation += 1

			if self.txt_animation <= 10000:
				display.blit(skip,(650,500))

			if self.txt_animation >= 10000:
				display.blit(enter,(650,500))

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 10000

			if keyinput[pg.K_RETURN] and self.txt_animation >= 10000 - 1:
					self.narr_diag_1 = False
					self.txt_animation = 0
			
		# DIAG 1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		if self.player_diag_1 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))

			player_diag_1 = {"diag_1" :"Tomorrow is roshela's birthday WTF!!" , 
			"diag_2":"I dont have any money to buy her a gift."}

			player_diag_txt_1 = self.font.render(player_diag_1["diag_1"][0:self.txt_animation//self.speed], True ,(30,30,30))

			#diag_box_1 = pg.draw.rect(display,(30,30,30),(0,400, width,200))
			display.blit(player_diag_txt_1,(5,405))

			if  self.txt_animation >= len(player_diag_1["diag_1"]) + 100:
				player_diag_txt_1 = self.font.render(player_diag_1["diag_2"][0:self.txt_animation//self.speed - 100], True ,(30,30,30))
				display.blit(player_diag_txt_1,(5,435))

				if self.txt_animation >= len(player_diag_1["diag_2"]) + 450:
					self.txt_animation = 10000

			self.txt_animation += 1


			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 10000

			if keyinput[pg.K_RETURN] and self.txt_animation >= 10000:
					self.player_diag_1 = False
					self.txt_animation = 0

			if self.txt_animation <= 10000 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 10000:
				display.blit(enter,(650,500))

		# DIAG 2 +++++++++++++++++++++++++++++++++++=

		if self.player_diag_2 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			player_diag_2 = {"diag_1":"I need some money but how can i...?"}
			diag_2 = self.font.render(player_diag_2["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_2,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 500

			if keyinput[pg.K_RETURN] and self.txt_animation >= 200 - 1:
					self.player_diag_2 = False
					self.txt_animation = 0

			if self.txt_animation <= 200:
				display.blit(skip,(650,500))

			if self.txt_animation >= 200:
				display.blit(enter,(650,500))

			#diag_box_1 = pg.draw.rect(display,(30,30,30),(0,400, width,200))
		
		# DIAG 3 ++++++++++++++++++++++++++++++++++++++++++++++++++

		if self.player_diag_3 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			player_diag_3 = {"diag_1":"Huh who tf are you?"}
			diag_3 = self.font.render(player_diag_3["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_3,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 100

			if keyinput[pg.K_RETURN] and self.txt_animation >= 100 - 1:
					self.player_diag_3 = False
					self.txt_animation = 0

			if self.txt_animation <= 100 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 100:
				display.blit(enter,(650,500))

		# DIAG 4 ++++++++++++++++++++++++++++++++++++++++++++++++

		if self.player_diag_4 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))

			player_diag_4 = {"diag_1":"Ok but how?"}
			diag_4 = self.font.render(player_diag_4["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_4,(5,405))
			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 80

			if keyinput[pg.K_RETURN] and self.txt_animation >= 80 - 1:
					self.player_diag_4 = False
					self.txt_animation = 0

			if self.txt_animation <= 80 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 80:
				display.blit(enter,(650,500))

		# DIAG 5 +++++++++++++++++++++++++++++++++++++++++++++++++


		if self.player_diag_5 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			
			player_diag_5 = {"diag_1":"HUH? ARE YOU CRAZY??!!"}
			diag_5 = self.font.render(player_diag_5["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_5,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 110

			if keyinput[pg.K_RETURN] and self.txt_animation >= 110 - 1:
					self.player_diag_5 = False
					self.txt_animation = 0

			if self.txt_animation <= 110 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 110:
				display.blit(enter,(650,500))

		# DIAG 6 +++++++++++++++++++++++++++++++++++++++++++++++++

		if self.player_diag_6 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))

			player_diag_6 = {"diag_1":"Hmmm.... Ok im in."}
			diag_6 = self.font.render(player_diag_6["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_6,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 110

			if keyinput[pg.K_RETURN] and self.txt_animation >= 110 - 1:
					self.player_diag_6 = False
					self.txt_animation = 0

			if self.txt_animation <= 110 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 110:
				display.blit(enter,(650,500))

		# STRANGER DIAG 1 +++++++++++++++++++++++++++++++++++++++++
		if self.strger_diag_1 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			strger_diag_1 = {"diag_1":"Psstt.... psstt... Hey kid you want some money?"}

			diag_1 = self.font.render(strger_diag_1["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_1,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 240

			if keyinput[pg.K_RETURN] and self.txt_animation >= 240 - 1:
					self.strger_diag_1 = False
					self.txt_animation = 0

			if self.txt_animation <= 240 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 240:
				display.blit(enter,(650,500))

		# STRANGER DIAG 2 +++++++++++++++++++++++++++++++++++++++++
		if self.strger_diag_2 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			strger_diag_2 = {"diag_1":"It doesn't matter."}

			diag_2 = self.font.render(strger_diag_2["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_2,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 100

			if keyinput[pg.K_RETURN] and self.txt_animation >= 100 - 1:
					self.strger_diag_6 = False
					self.txt_animation = 0

			if self.txt_animation <= 100 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 100:
				display.blit(enter,(650,500))

		# STRANGER DIAG 3 +++++++++++++++++++++++++++++++++++++++++
		if self.strger_diag_3 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			strger_diag_3 = {"diag_1":"Sell some drugs."}

			diag_3 = self.font.render(strger_diag_3["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_3,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 90

			if keyinput[pg.K_RETURN] and self.txt_animation >= 90 - 1:
					self.strger_diag_3 = False
					self.txt_animation = 0

			if self.txt_animation <= 90 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 90:
				display.blit(enter,(650,500))


		# STRANGER DIAG 4 +++++++++++++++++++++++++++++++++++++++++

		if self.strger_diag_4 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			strger_diag_4 = {"diag_1":"No. if you ask why drugs,  drugs is expensive",
			"diag_2":"but selling it is more profitable."}

			diag_4 = self.font.render(strger_diag_4["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_4,(5,405))

			if self.txt_animation >= len(strger_diag_4) + 200:
				diag_4 = self.font.render(strger_diag_4["diag_2"][0:self.txt_animation//self.speed - 80], True, (30,30,30))
				display.blit(diag_4,(5,435))
				if self.txt_animation >= len(strger_diag_4["diag_2"]) + 360:
					self.txt_animation = 10000

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 10000

			if keyinput[pg.K_RETURN] and self.txt_animation >= 400 - 1:
					self.strger_diag_4 = False
					self.txt_animation = 0

			if self.txt_animation <= 400 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 400:
				display.blit(enter,(650,500))

		# STRANGER DIAG 5 +++++++++++++++++++++++++++++++++++++++++
		if self.strger_diag_5 == True:
			display.blit(self.diag_box,(0,height/1.6 - 5))
			strger_diag_5 = {"diag_1":"Now go on kid make some money."}

			diag_5 = self.font.render(strger_diag_5["diag_1"][0:self.txt_animation//self.speed], True, (30,30,30))
			display.blit(diag_5,(5,405))

			self.txt_animation += 1

			if keyinput[pg.K_LSHIFT]:
				self.txt_animation = 10000

			if keyinput[pg.K_RETURN] and self.txt_animation >= 150 - 1:
					self.strger_diag_5 = False
					self.txt_animation = 0

			if self.txt_animation <= 150 - 1:
				display.blit(skip,(650,500))

			if self.txt_animation >= 150:
				display.blit(enter,(650,500))
		
# CARSSS!!!!!!!!!!
	def cars(self):
		
		if self.selector == 0 or self.selector == 1:
			car_rect_lr = pg.draw.rect(window,(0,0,200),(self.car_x - player.camera_x, self.car_y - player.camera_y, 32,15))
		
		if self.selector == 2 or self.selector == 3:
			car_rect_ud = pg.draw.rect(window,(0,0,200),(self.car_x - player.camera_x, self.car_y - player.camera_y, 15,32))

	
			
		if self.spawn == True:
			self.selector = random.randint(0,3)
			self.spawn = False
			self.cooldown = 0

		if self.selector == 0:
			self.car["car_right"] = True
			self.car["car_left"] = False
			self.car["car_down"] = False
			self.car["car_up"] = False

		if self.selector == 1:
			self.car["car_left"] = True
			self.car["car_right"] = False
			self.car["car_down"] = False
			self.car["car_up"] = False
		
		if self.selector == 2:
			self.car["car_up"] = True
			self.car["car_right"] = False
			self.car["car_left"] = False
			self.car["car_down"] = False
	

		if self.car["car_right"] == True:
			self.car_x += 3
			self.car_y = 85
			self.car_x = 0


		if self.car["car_left"] == True:
			self.car_x -= 3
			self.car_y = 120
			self.car_x -= 500



		if self.car["car_up"] == True:
			self.car_y -= 3
			self.car_y = 500
			self.car_x = 205
			

		if self.car["car_down"] == True:
			self.car_y += 3
			self.car_y = 0
			self.car_x = 205
			self.car_x += 3



		#print(self.selector)
		self.cooldown += 0.2

		if self.cooldown >= 100:
			self.spawn = True

npc = npc_class()
