from flask import Blueprint, request
from flask_cors import cross_origin
from app.models import Post, User, db



api = Blueprint('api', __name__, template_folder='apitemps', url_prefix='/api')


@api.route('/reg', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    newuser = User(username=data['username'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'], userpass=data['userpass'] )  # Have to figure out this part! current err=
    # TypeError: __init__() missing 3 required positional arguments: 'email', 'first_name', and 'last_name'
    db.session.add(newuser)
    db.session.commit()
    print('New user reg!')
    return 'Registration success!', 201

    
# @api.route('/<int:pid')
# def createPost(pid):
#     newpost = Post()


