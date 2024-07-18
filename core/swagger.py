from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


docs = get_schema_view(
    openapi.Info(
        title="AQUATICKINGDOM REST API",
        default_version='v1',
        description="Добро пожаловать в AquaticKingdom REST API – ваш надёжный партнёр в мире аквариумистики! Наш API предоставляет богатый функционал для управления вашим аквамагазином, позволяя легко управлять ассортиментом продукции, заказами, клиентами и многим другим!!.",
        terms_of_service="AquaticKingdom REST API создан для того, чтобы упростить вашу работу и повысить эффективность вашего аквамагазина. Независимо от того, занимаетесь ли вы продажей рыб, оборудования или аксессуаров, наше API поможет вам управлять вашим бизнесом с легкостью и уверенностью.",
        contact=openapi.Contact(email="melaniegolden20@gmail.com"),
        license=openapi.License(name="MIT Lisence"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
