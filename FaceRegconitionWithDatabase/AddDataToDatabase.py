import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognition-191ed-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')
data = {
    "20057":
        {
            "name":"Bill Gates",
            "major": "Billionare",
            "starting_year":2023,
            "total_attendance":6,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2023-12-21 00:21:11"
        },
    "20059":
        {
            "name": "Ly Thanh Long",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-12-24 18:21:11"
        },
    "20112":
        {
            "name": "Chris Evans",
            "major": "Actor",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "I",
            "year": 2,
            "last_attendance_time": "2023-12-22 19:32:01"
        },
    "21111":
        {
            "name": "Lil Nas X",
            "major": "Singer",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-12-19 08:01:23"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
