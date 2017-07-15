from requests_toolbelt import MultipartEncoder
import random
import requests

def rH(n):
	return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])

def rI():
	return '%s-%s-%s-%s-%s'%(rH(8),rH(4),rH(4),rH(4),rH(12))

def dL(u,p):
	data={'auth_type':'opentable','client_id':'ot-apps','client_secret':'0pentab1e','grant_type':'password','password':p,'username':u}
	r=requests.post('https://mobile-api.opentable.de/oauth/consumer/token',data=data,headers={'Content-Type':'application/x-www-form-urlencoded','Accept-Encoding':'gzip, deflate','Accept':'application/json','User-Agent':'com.contextoptional.OpenTable/10.21.0.4; iPad; iOS/10.2; 2.0; %s/Anonymous'%(rI()),'Accept-Language':'en-GB;q=1, de-DE;q=0.9, da-DK;q=0.8, en-US;q=0.7, ru-RU;q=0.6'},verify=False)
	return r.content
	
if __name__ == "__main__":
	print dL('test@gmail.com','test')