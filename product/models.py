from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256,verbose_name="상품명")
    price = models.IntegerField(verbose_name="가격")
    stock = models.PositiveIntegerField(verbose_name="재고")
    info = models.TextField(verbose_name="상품 정보")
    creator = models.ForeignKey("user.User",on_delete=models.CASCADE, verbose_name="생성자")
    creation_date = models.DateTimeField(auto_now_add=True,verbose_name="등록일")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "상품"
        verbose_name_plural = "상품"