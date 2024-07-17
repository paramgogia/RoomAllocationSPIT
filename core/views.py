from django.shortcuts import render
import time

# Create your views here.
def index(request):
    times = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
    rooms = ["003", "008", "105", "203", "701", "703", "Board Room"]
    #get todays date using time module
    
    if request.method == 'POST':
        if 'form1' in request.POST:
            date = request.POST['dateinput']
            #get previous date
            today = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(date, "%Y-%m-%d"))-86400))
        elif 'form2' in request.POST:
            date = request.POST['dateinput']
            #get next date
            today = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(date, "%Y-%m-%d"))+86400))
        else:
            today = request.POST['form4']
        return render(request, 'index.html', {'times': times, 'rooms': rooms, 'date': today})
    
    today = time.strftime("%Y-%m-%d")
    return render(request, 'index.html', {'times': times, 'rooms': rooms, 'date': today})
