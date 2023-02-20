from django.urls import path
from . import consumers

websocket_urlpatterns =[
    # path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
    # path('ws/ac/',consumers.MyAsyncConsumer.as_asgi()),
    # path('ws/admin/', consumers.AdminConsumer.as_asgi()),
    path('ws/patient/', consumers.PateintConsumer.as_asgi()),
]
