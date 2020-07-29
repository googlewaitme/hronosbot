from peewee import *


db = SqliteDatabase('noteces.db')


class Notice(Model):
	date_of_create = DateTimeField()
	text = TextField()
	user_id = TextField()
	last_sending = DateTimeField(default='')
	attachment = TextField()
	
	class Meta:
		database = db
