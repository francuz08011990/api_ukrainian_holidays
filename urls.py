from api.holiday import Holiday


urls_v1 = [
    (Holiday, 'holiday/year/<int:year>/month/<int:month>/day/<int:day>/'),
]
