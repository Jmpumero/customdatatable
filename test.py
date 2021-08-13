import json
import copy
from typing import Any, Hashable, Iterable, Optional
container = {
    "_metadata":{
    "page": 'kwargs["page"]',
    "per_page": 'kwargs["pagination"]',
    "page_count": 20,
    "total_count": 521,
    "links": [
    {"self": "/products?page=5&per_page=20"},
    {"first": "/products?page=0&per_page=20"},
    {"previous": "/products?page=4&per_page=20"},
    {"next": "/products?page=6&per_page=20"},
    {"last": "/products?page=26&per_page=20"},
    ]
    },
    "records": [
    {
    "name": "Jonh",
    "last_name": "Doe",
    "nationality": "Canadian",
    "phone_number": "+2",
    "address":"address",
    "id":"123",
    "document_id":"111",
    "email": "noone@sample.com",
    "civil_status": "married",
    "age": "23",
    "img": "static/img/profile.png",
    "count_blacklist": 2,
    "postal_address":"postal address",
    "languaje":[
        "Spanish",
        'Italian'
        ],
    "birthday_date":"01-02-1903",
    "document_id_type":"V",
    "status_blacklist": True,
    "motives_blacklist_disable":[
        "Pago con tarjata de credito robada",
        "Retraso en reservacion"
    ],
    "motives_blacklist_enable":[
    ],
    "last_enable_date":"19-06-2011 13:00:22",
    "last_disable_date":"19-06-2021 13:00:21",
    "sensors":[
        
        {
            "Hostpot":[
            {"Fecha":"25-10-2020 15:00","Propiedad":"HPA","Duración":"1h"
            },
            {"Fecha":"27-11-2020 9:00","Propiedad":"HPA","Duración":"30m"
            },
            ]
        },
        {
            "Cast":[
            {"Fecha":"25-10-2020 15:00","Propiedad":"HPA","Duración":"1h"
            },
            ]
        }
    ]
    },
    {
    "name": "Jonhy",
    "last_name": "Perez",
    "nationality": "Venezolano",
    "phone_number": "+2",
    "address":"address",
    "id":"345",
    "document_id":"111",
    "email": "noone@sample.com",
    "civil_status": "married",
    "age": "23",
    "img": "static/img/profile.png",
    "count_blacklist": 2,
    "postal_address":"postal address",
    "languaje":[
        "Spanish",
        'Italian'
        ],
    "birthday_date":"01-02-1903",
    "document_id_type":"V",
    "status_blacklist": False,
    "motives_blacklist_disable":[
        
    ],
    "motives_blacklist_enable":[
    ],
    "last_enable_date":"",
    "last_disable_date":"",
    "sensors":[
        
        {
            "Cast":[
            {"Fecha":"25-10-2020 15:00","Propiedad":"HPA","Duración":"1h"
            },
            ]
        }
    ]
    }
    ]
}

def buscar_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
        for dicc in it:
            if dicc[clave] == valor:
                return dicc
        return None

def test():
    #user_list=(container['records']).copy()
    var='True'
    user_list=copy.deepcopy(container['records'])
    #res = {key: test_dict[key] for key in test_dict.keys() & {'akshat', 'nikhil'}}
    l=[]
    if var=='true':
        for x in range(len(user_list)):
            if user_list[x]['status_blacklist']==False:
                print(str(user_list[x]['status_blacklist']))
                user_list[x]['motives_blacklist_disable']= ", ".join(user_list[x]['motives_blacklist_disable']) #ojo 
                l.append(user_list[x])
    else:
        pass
            
        
        
    #print(l)
    #print(user_list)
    
    
    
def test2():
    users=copy.deepcopy(container['records'])
        
        
    tipo='hotspot'
    user=buscar_dicc(users,"id",'123')
    sensors= user['sensors']
    #print(sensors)
    data_list=''
    if sensors:
        for x in range (len(sensors)):
            if 'hostpot'=='hostpot':
                if sensors[x].get('Hostpot') :
                
                    data_list=sensors[x]['Hostpot']
    
    print({"data":data_list})





if __name__ == "__main__":
    test()
    test2()
    name = 'james'
   
    sensores=['cast','hostpot','butler','eRoomPMS','eRestaurant','web']
    print(sensores)