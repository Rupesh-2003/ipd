from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import os
from mongo_engine import db
from flask_cors import CORS

from Resources.employee import Employee
from Resources.ticket import Ticket
from Resources.order import Order
from Resources.customer import Customer
from Resources.conversation import Conversation

load_dotenv()
app = Flask(__name__)
app.config['MONGODB_HOST'] = os.getenv('MONGODB_URI')
CORS(app)

db.init_app(app)
api = Api(app)

api.add_resource(Employee, '/employee')
api.add_resource(Ticket, '/ticket')
api.add_resource(Order, '/order')
api.add_resource(Customer, '/customer')
api.add_resource(Conversation, '/conversation')


@app.route('/check')
def check():
    return "Checking"

if __name__ == '__main__':
    app.run(debug=True)

