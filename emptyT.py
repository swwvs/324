from datetime import datetime


#match = connection.execute("SELECT * FROM Reservations WHERE CartID = 100 and CartCollege ='ksu' ").fetchall()
k=[(123456, 100, 'ksu', '2023-11-30', '2023-11-30', 'true', '00:00', '01:01'), (123456, 100, 'ksu', '2023-12-03', '2023-12-03', 'true', '00:00', '01:01')]



for x in k:
    counter=0
    st=k[counter][6]
    et=k[counter][7]
    print(st)

    counter=counter+1





time_str = "01:01"
time_obj = datetime.strptime(time_str, "%H:%M")
minutes = time_obj.hour * 60 + time_obj.minute
print(minutes)
