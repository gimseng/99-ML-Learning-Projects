'''
Install all these packages with pip
Flask==1.1.2
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.3
Jinja2==2.11.2
SQLAlchemy==1.3.18
'''

from flask import Flask
from flask_restful import  Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Restful
api = Api(app)
# Creating/loading sqlite data base. Can be treated as fake database fo RTO
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rto.db'
db = SQLAlchemy(app)

# Adding the columns to the model.
class RtoModel(db.Model):
    Registration = db.Column(db.String(64), primary_key=True)
    Owner = db.Column(db.String(64), nullable=False)
    Maker = db.Column(db.String(64), nullable=False)
    Vehicle = db.Column(db.String(64), nullable=False)
    Fuel_Type = db.Column(db.String(64), nullable=False)
    Chassis = db.Column(db.String(64), nullable=False)
    Engine_Number = db.Column(db.String(64), nullable=False)
    Registration_Date = db.Column(db.String(64), nullable=False)
    Insurance_Valid_Upto = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"RTO( Registration={Registration}, Owner={Owner}, Maker={Maker}, Vehicle={Vehicle}, Fuel_Type={Fuel_Type}, Chassis={Chassis}, Engine_Number={Engine_Number}, Registration_Date={Registration_Date}, Insurance_Valid_Upto={Insurance_Valid_Upto})"


# do the below thing only once for creating the table. 
#db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('Registration', type=str, help='Registration number is required', required=True)
video_put_args.add_argument('Owner', type=str, help="Owner's Name is required", required=True)
video_put_args.add_argument('Maker', type=str, help='Maker details are required', required=True)
video_put_args.add_argument('Vehicle', type=str, help='Vehicle type is required', required=True)
video_put_args.add_argument('Fuel_Type', type=str, help='Type of Fuel is required', required=True)
video_put_args.add_argument('Chassis', type=str, help='Chassis Number is required', required=True)
video_put_args.add_argument('Engine_Number', type=str, help='Engine Number is required', required=True)
video_put_args.add_argument('Registration_Date', type=str, help='Registration Date is required', required=True)
video_put_args.add_argument('Insurance_Valid_Upto', type=str, help='Insurance Due Date is required', required=True)


Resource_fields = {
    'Registration' : fields.String,
    'Owner': fields.String,
    'Maker': fields.String,
    'Vehicle': fields.String,
    'Fuel_Type': fields.String,
    'Chassis': fields.String,
    'Engine_Number': fields.String,
    'Registration_Date': fields.String,
    'Insurance_Valid_Upto': fields.String
}


class RTO(Resource):
    @marshal_with(Resource_fields)
    def get(self, vehicle_number):
        result = RtoModel.query.filter_by(Registration=vehicle_number).first()
        if not result:
            abort(404, message="Vahicle details Not found...")
        return result

    @marshal_with(Resource_fields)
    def put(self, vehicle_number):
        args = video_put_args.parse_args()
        result = RtoModel.query.filter_by(Registration=vehicle_number).first()
        if result:
            abort(409, message="Vehicle already exists...")
        vehicle = RtoModel(Registration=vehicle_number, Owner=args['Owner'], Maker=args['Maker'], Vehicle=args['Vehicle'], Fuel_Type=args['Fuel_Type'], Chassis=args['Chassis'], Engine_Number=args['Engine_Number'], Registration_Date=args['Registration_Date'], Insurance_Valid_Upto=args['Insurance_Valid_Upto'])
        db.session.add(vehicle)
        db.session.commit()
        return vehicle , 201

    def delete(self, video_id):
        return "", 204

api.add_resource(RTO, "/vehicle/<string:vehicle_number>")



if __name__ == '__main__':
    app.run(debug=True)