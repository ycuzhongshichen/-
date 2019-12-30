import django.db

class Student(django.db.models.Model):
    SEX_ITEMS=[ (1,'男'),
                (2,'女'),
                (3, '未知'),
                ]
    STATUS_ITEMS=[(1,"申请"),
                  (2,"通过"),
                  (3, "拒绝"),
                  ]
    name=django.db.models.CharField(max_length=128, verbose_name="姓名")
    sex=django.db.models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession=django.db.models.CharField(max_length=128, verbose_name="职业")
    email=django.db.models.EmailField(verbose_name="Email")
    qq=django.db.models.CharField(max_length=128, verbose_name="QQ")
    phone = django.db.models.CharField(max_length=128, verbose_name="电话")
    status=django.db.models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    created_time=django.db.models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    def __str__(self):
        return '<Student:{}>'.format(self.name)

    class Meta:
        verbose_name=verbose_name_plural="学员信息"
