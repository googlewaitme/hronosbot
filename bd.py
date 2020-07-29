from models import Notice
from datetime import datetime, timedelta

def create_notice(user_id, text, attachment=''):
	new_notice = Notice()
	new_notice.text = text
	new_notice.attachment = attachment
	new_notice.date_of_create = datetime.now()
	new_notice.last_sending = datetime.now()
	new_notice.user_id = user_id
	new_notice.save()


def give_all_notices_need_to_send():
	date = datetime.now() - timedelta(days = 365)
	data = list(Notice.select().where(Notice.last_sending < date))
	return data