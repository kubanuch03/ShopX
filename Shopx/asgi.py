import os
import django
from django.core.asgi import get_asgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shopx.settings')

# Initialize Django
django.setup()

# Get the ASGI application
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
<<<<<<< HEAD
from django.urls import path

from app_chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/<str:room_name>/', ChatConsumer.as_asgi()),
        ])
    ),
    
})

=======
from app_chat.routing import websocket_urlpatterns

# Define the ASGI application
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
>>>>>>> e289b7570f0bcfeb760f1748f686c33f005fbb82
