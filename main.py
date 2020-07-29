from bd import create_notice
from logik import every_iteration_check
from web import write_msg, longpoll, VkEventType

while True:
	for event in longpoll.check():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				create_notice(event.user_id, event.text)
				write_msg(event.user_id, 'Новая напоминалка добавлена')
	every_iteration_check()
