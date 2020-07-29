import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint



#vk token of group
token = '9283bf46c124e12004b1c5289f05984f2d5405905ddbfe9ede0d89bee31d51b619d143d029b89980bd1ee'

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

def write_msg(user_id, message, attachment=''):
	random_id = randint(1, 1000000)
	vk.method('messages.send', 
		{'user_id': user_id, 
		'message': message, 
		'random_id': random_id} 
	)
