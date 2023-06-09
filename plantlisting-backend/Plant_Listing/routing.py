from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing
from chat.middleware import TokenAuthMiddlewareStack

application=ProtocolTypeRouter({
    'websocket':TokenAuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})