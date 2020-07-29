from bd import give_all_notices_need_to_send
from web import write_msg
from datetime import datetime

def every_iteration_check():
	data = give_all_notices_need_to_send()
	for notice in data:
		write_msg(notice.user_id, notice.text)
		notice.last_sending = datetime.now()
		notice.save()
