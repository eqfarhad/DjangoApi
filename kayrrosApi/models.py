from django.db import models

class ShowsModel(models.Model):
    episodes_id = models.IntegerField(primary_key=True, db_column='embedded_episodes_id')
    url= models.CharField(max_length=500, db_column='url')
    name =models.CharField(max_length=500, db_column='name')
    episodes_url  =models.CharField(max_length=500,db_column='embedded_episodes_url')
    episodes_name  =models.CharField(max_length=500,db_column='embedded_episodes_name')
    episodes_season =models.IntegerField(db_column='embedded_episodes_season')
    episodes_number =models.IntegerField(db_column='embedded_episodes_number')
    class Meta:
        db_table = 'shows'