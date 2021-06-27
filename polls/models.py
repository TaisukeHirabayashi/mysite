from django.db import models

# Create your models here.
#学年モデル
class Grade(models.Model):
    #学年の列に当たる
    grades=models.CharField(verbose_name="学年一覧",max_length=10)
    
    #おまじない
    def __str__(self):
        return self.grades
     
    #表に名前を付ける    
    class Meta:
        verbose_name_plural="学年モデル"

        
#メンバーモデル        
class Member(models.Model):
    #学年選択
    grade=models.ForeignKey('Grade',verbose_name="学年を選択してください",on_delete=models.CASCADE)
    
    #部員名
    name=models.CharField(verbose_name="名前",max_length=25)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural="メンバーモデル"
    