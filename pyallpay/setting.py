# -*- coding: utf-8 -*
'''
    You personal setting of AllPay
'''

ALLPAY_SANDBOX = True
AIO_SERVICE_URL = 'https://payment-stage.allpay.com.tw/Cashier/AioCheckOut/V2'
AIO_SANDBOX_SERVICE_URL = 'http://payment-stage.allpay.com.tw/Cashier/AioCheckOut'

'''
    Get these from AllPay management panel
'''
MERCHANT_ID = '2000132'
HASH_KEY = '5294y06JbISpM5x9'
HASH_IV = 'v77hoKGq4kWxNNIS'

'''
    Please specify your own URL, check out the allpay document for more details
    https://www.allpay.com.tw/Service/API_Help?Anchor=AnchorDoc
'''
ALLPAY_SANDBOX = False # False or True, The sandbox configuration depend on you.
MERCHANT_ID = '2000132'
RETURN_URL = 'http://www.i8d.com.tw/return_url' #當消費者付款完成後,歐付寶會發送付款結果到訂單產生規格中的 ReturnURL
CLIENT_BACK_URL = 'http://www.i8d.com.tw/client_back_url' #Client 返回網站的網址
PAYMENT_INFO_URL = 'http://www.i8d.com.tw/payment_info_url' #Server 端回傳付款相關資訊
