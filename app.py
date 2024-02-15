from config import *
from controller.MainController import *
if __name__ == "__main__":
    with app.app_context():
        app.run(host='0.0.0.0', port=80, debug=True)
        