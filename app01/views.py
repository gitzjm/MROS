from django.shortcuts import render,HttpResponse
from MROS import settings
from app01 import models
import json

def login(request):
    """
    登录
    """
    if request.method == "GET":
        return render(request, "login.html")
    else:
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        print(user, pwd)
        login_response = {"is_login": False, "error_msg": None}
        if models.User.objects.filter(name=user, pwd=pwd):
            login_response["is_login"] = True
            request.session["user"] = user
        else:
            login_response["error_msg"] = "用户名密码错误！"
        return HttpResponse(json.dumps(login_response))


def index(request):
    rooms=models.Meeting_room.objects.all()
    # print(rooms)
    return render(request,"index.html",{"rooms":rooms,"time_list":settings.times_list})

def init_booking(request):
    if request.method=="GET":
        print("------------------------")

        chosen_date=request.GET.get('date')
        booking_list=models.Booking.objects.filter(date=chosen_date)
        booking_dict={}
        for item in booking_list:
            booking_dict[str(item.meeting_room_id)+"_"+str(item.times)]={"username": item.user.name,"user_id":item.user.id}
        print(booking_dict)

        meeting_room_list=models.Meeting_room.objects.all()
        data=[]
        for meeting_room in meeting_room_list:
            tr=[]
            tr.append({"text":meeting_room.title,"attrs":{}})
            for i in settings.times_list:
                s=str(meeting_room.id)+"_"+str(i[0])
                if s in booking_dict:
                    td={"text":booking_dict[s]["username"],"attrs":{"room_id":meeting_room.id,"time_id":i[0],"class":""}}
                    if booking_dict[s]["username"]!=request.session["user"]:
                        td["attrs"]["class"]="chosen disable"
                    else:
                        td["attrs"]["class"]="my_choice"


                else:
                    td={"text":"","attrs":{"room_id":meeting_room.id,"time_id":i[0],"class":""}}
                tr.append(td)
            data.append(tr)
        return HttpResponse(json.dumps(data))
    else:
        POST_DATA=json.loads(request.POST.get("POST_DATA"))
        print(type(POST_DATA))
        request.POST.get("date")
        for room_id,item in POST_DATA.items():
            print(room_id,item)
        return HttpResponse("OK")


#
# if room.in+"_"+tm[0] in booking_dict[room.id]
#     td={"text":booking_dict[room.id][tm0]["uesrname"],"attrs":{"room_id":room.id,"time_id":tm[0],"class":"chosen"}}
# Create your views here.

