class Cars:
	def __init__(self, mark, power):
		self.mark = mark
		self.power = power
	
	def move(self):
		print(self.mark, "Едет по дороге")


class Plan(Cars):
	def __init__(self, mark, power, speed):
		# self.mark = mark
		# self.power = power
		self.speed = speed
		super().__init__(mark,power)

	def move(self):
		print(self.mark, "Летит по небу")

		

def do(self, thing):
		tning.move()


tu134 = Plan("Ту-134", 10000, 300)
bugati = Cars("Бугати", 1000)

n=10
# print("Добро пожаловать!")
# a = input("""Выбери транспорт для участия в гонке: 
# 			 1. Самолет
# 			 2. Автомобиль
# 			 Ваш выбор: """)
# if a == 1:
# 	print("Хороший выбор!")

while n >= 0:

	tu134.move()
	bugati.move()
	n-=1