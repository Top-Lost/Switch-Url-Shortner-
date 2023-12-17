from swibots import Client
from config import BOT_TOKEN


app = Client(
    token=BOT_TOKEN,
    plugins=dict(
        root="plugins"
    )
)
