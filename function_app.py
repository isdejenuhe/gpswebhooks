import azure.functions as func
from src.routes.mailgunRoutes import mailgunRoutes

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
app.register_functions(mailgunRoutes)
