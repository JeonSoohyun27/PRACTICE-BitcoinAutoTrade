import pyupbit
from setting import ACCESS,SECRET

ACCESS = ACCESS
SECRET = SECRET
upbit = pyupbit.Upbit(ACCESS,SECRET)

print(upbit.get_balance("KRW-SAND")) #종목 보유 개수(샌드박스)
print(upbit.get_balance("KRW")) #원화금액