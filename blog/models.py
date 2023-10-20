from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#사이트명 -카드노출             
    thumb_nail = models.TextField(blank=True, null=True)
    success_rate = models.TextField(blank=True, null=True)#달성률-카드노출
    invest_rate = models.CharField(max_length=200,blank=True, null=True)#금리-카드노출
    text = models.TextField()
    
    INSP_NO = models.CharField(max_length=200, blank=True, null=True) #대출신청번호
    ID_NO = models.CharField(max_length=200, blank=True, null=True)#주민번호
    P_BIZ_NO = models.CharField(max_length=200, blank=True, null=True)#사업자번호
    BIZ_NO = models.CharField(max_length=200, blank=True, null=True)#법인번호
    EXP_INCOME = models.CharField(max_length=200, blank=True, null=True)#연(추정)소득
    TOTAL_INCOME = models.CharField(max_length=200, blank=True, null=True)#총대출신청금액
    ASST_QLTY = models.CharField(max_length=200, blank=True, null=True)#자산건전성
    MORT_AMT = models.CharField(max_length=200, blank=True, null=True)#담보금액
    RNK_AMT = models.CharField(max_length=200, blank=True, null=True)#선순위금액
    VALD_MORT_AMT = models.CharField(max_length=200, blank=True, null=True)#유효담보금액
    MORT_LOCPL = models.CharField(max_length=1000, blank=True, null=True)#담보소재지
    KB_RLEST_MKPC = models.CharField(max_length=200, blank=True, null=True)#KB부동산시세
    ISVT_TRPC = models.CharField(max_length=200, blank=True, null=True)#국토부실거래가
    RGSTCC_CNFR_YN = models.CharField(max_length=200, blank=True, null=True)#등기부등본확인여부
    MORT_WRTH = models.CharField(max_length=200, blank=True, null=True)#등기부등본확인여부

    MAX_LIMIT = models.CharField(max_length=200, blank=True, null=True)#최대한도-카드노출

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        #print(self.__dict__)
        return self.title

class Apply(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    신청금액 = models.CharField(max_length=200,blank=True, null=False)#사이트명 -카드노출             
    신청기간 = models.CharField(max_length=200,blank=True, null=False)
   
    apply_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        #print(self.__dict__)
        return self.author