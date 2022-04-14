from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app.models import Post, User, db


api = Blueprint('api', __name__, template_folder='apitemps', url_prefix='/api')


@api.route('/reg', methods=['POST'])
def register():
    data = request.get_json()
    # print(data)
    newuser = User(username=data['username'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'], userpass=data['userpass'] )  # Have to figure out this part! current err=
    # TypeError: __init__() missing 3 required positional arguments: 'email', 'first_name', and 'last_name'
    db.session.add(newuser)
    db.session.commit()
    print('New user reg!')
    return 'Registration success!', 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.userpass == data['userpass']:
        print(type(user), user)
        return jsonify({'userid': user.id, 'username': user.username, 'email': user.email}), 200 #Continue on here!  Let's see if we can get this mfer to work!
    else:
        return jsonify({'Login unsuccessful': 'Please try again.'})

    
@api.route('/new/post', methods=['POST'])
def createPost():
    data = request.get_json()
    print(data)
    if not data['userid']:
        return jsonify({'Post unsucessful': 'Please make sure you are logged in! post meets guidelines!'}), 500
    elif data['body'] == '' or data['title'] == '':
        return jsonify({'Post unsucessful': 'Please make sure your post meets guidelines!'}), 500
    else:
        newpost = Post(user_id=data['userid'], title=data['title'], body=data['body'])
        db.session.add(newpost)
        db.session.commit()
        return 'Success, posted!', 201

@api.route('/posts/<string:user_id>', methods=['GET'])
def getPosts(user_id):
    posts = {'postdic': [p.serialize() for p in Post.query.filter_by(user_id=Post.user_id).order_by(Post.timestamp.desc()).all()]}
    print(posts, type(posts))
    return jsonify(posts), 200
    
    
    # 
    # for p in range(len(posts)):
    #     plist.append(p)
    # print(plist)


    

