from django.db import models

# Create your models here.

class Order(models.Model):
    orderer = models.ForeignKey("user.User",on_delete=models.CASCADE,verbose_name="주문자")
    product = models.ForeignKey("product.Product",on_delete=models.CASCADE,verbose_name="상품")
    quantity = models.IntegerField(verbose_name="수량")
    total_price = models.IntegerField(verbose_name="가격")
    creation_date = models.DateTimeField(auto_now_add=True,verbose_name="등록일")

    def __str__(self):
        return str(self.orderer)+' '+str(self.product)

    class Meta:
        db_table = "order"
        verbose_name = "주문"
        verbose_name_plural = "주문"