from django.db import models

# Create your models here.
class Plan(models.Model):
    """ プランモデル """
    plan_name = models.CharField(verbose_name="プラン名", blank=True, max_length=50)
    book_score = models.SmallIntegerField(verbose_name="いいね数", default=0)
    model_score = models.SmallIntegerField(verbose_name="引用数", default=0)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


    class Meta:
        verbose_name_plural = "Plan"
    def __str__(self):
        return self.plan_name

class SpecificPlanList(models.Model):
    """ ユーザ所有のプランリスト """

    is_book = models.BooleanField(verbose_name="いいねか")
    plan = models.ForeignKey('Plan', verbose_name="プラン", on_delete=models.PROTECT)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

class Task(models.Model):
    """ タスクモデル """

    task_name = models.CharField(verbose_name="タスク名", blank=True, max_length=50)
    start_datetime = models.DateTimeField(verbose_name="開始日時", null=True)
    end_datetime = models.DateTimeField(verbose_name="終了日時", null=True)
    url = models.URLField(verbose_name="URL", blank=True, null=True)
    task_memo = models.TextField(verbose_name="タスクメモ", blank=True, null=True)
    plan = models.ForeignKey('Plan', verbose_name="プラン", on_delete=models.PROTECT)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        verbose_name_plural = "Task"
    def __str__(self):
        return self.task_name