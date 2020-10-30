from bd import give_all_notices_need_to_send
from datetime import datetime

def process(sendler):
	data = give_all_notices_need_to_send()
	for notice in data:
		senler.send_notice(notice)
		notice.last_sending = datetime.now()
		notice.save()
