import requests
import json
import datetime,time

GIC_Username = "MyGICUserName"
GIC_Password = "MyGICPassword"

UUID_BJ = "UUIDofaNIC"
UUID_GPN = "UUIDofaNIC"
UUID_DAL = "UUIDofaNIC"

def getBWInfo(UUID):
	url = "https://api.yun-idc.com/gic/v1/flow/pipe/" + UUID
	headers = {
    	'token': token,
    	'cache-control': "no-cache",
    }
	response = requests.request("GET", url, headers=headers)
	J_dict = json.loads(response.text)
	tra_in = J_dict["data"]["last_5_minutes_usage"]["in_bps"]
	tra_out = J_dict["data"]["last_5_minutes_usage"]["out_bps"]
	tra_max = max(tra_in,tra_out)
	tra_bw =  J_dict["data"]["max_qos"]
	return (tra_max,tra_bw)

token_url = "https://api.yun-idc.com/gic/v1/get_token/"

token_headers = {
    'content-type': "application/x-www-form-urlencoded",
    'username': GIC_Username,
    'password': GIC_Password,
    'cache-control': "no-cache",
    }



while True:
	print str(datetime.datetime.now())+"\tCDT"
	token_response = requests.request("GET", token_url, headers=token_headers)
	token_obj = json.loads(token_response.text)
	token = token_obj["Access-Token"]

	BJ_cur,BJ_limit = getBWInfo(UUID_BJ)
	GPN_cur,GPN_limit = getBWInfo(UUID_GPN)
	DAL_cur,DAL_limit = getBWInfo(UUID_DAL)

	print "BJS:\t" + str(round(BJ_cur/1000000,3)) + " Mbps\tof " + str(BJ_limit) + " Mbps" 
	print "GPN:\t" + str(round(GPN_cur/1000000,3)) + " Mbps\tof " + str(GPN_limit) + " Mbps" 
	print "DAL:\t" + str(round(DAL_cur/1000000,3)) + " Mbps\tof " + str(DAL_limit) + " Mbps" 

	time.sleep(150)







