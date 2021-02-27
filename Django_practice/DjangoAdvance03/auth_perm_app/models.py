from django.db import models


class School(models.Model):    # "一方"模型
    name = models.CharField(max_length=20, verbose_name="学校名称")
    address = models.CharField(max_length=50,verbose_name="地址")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "schools"
        verbose_name = "学校模型"
        verbose_name_plural = verbose_name


class Student(models.Model):    # "多方"模型
    name = models.CharField(max_length=20,verbose_name="姓名")
    sex = models.CharField(max_length=10,verbose_name="性别")
    score = models.FloatField(verbose_name="成绩")
    school = models.ForeignKey(School,on_delete=models.CASCADE,verbose_name="所在学校")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"
        verbose_name = "学生模型"
        verbose_name_plural = verbose_name
        permissions = (
            ('visit_vip','Can operate vip student'),    # 自定义权限
        )
