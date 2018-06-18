import app
from app.server import server

server.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
