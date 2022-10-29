from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

# from lib.loaders import load_models
# ​Export just the db and init_db symbols when 'from db import *' is used
__all__ = ('db', 'init_db')   

# our global DB ojbect (imported by models and views)
db = SQLAlchemy()

# support importing a functioning session query
# query = db.session.query

def init_db(app=None, db=None):
   """Initializes the global database object used by the app."""
   if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
      # force_auto_coercion()
      # load_models()
      db.init_app(app)
      
   else:
      raise ValueError('Cannot init DB without db and app objects.')











# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgresql import UUID
# # from lib.loaders import load_models
# # ​Export just the db and init_db symbols when 'from db import *' is used
# __all__ = ('db', 'init_db')
# # our global DB ojbect (imported by models and views)
# db = SQLAlchemy()
# # support importing a functioning session query
# # query = db.session.query
# def init_db(app=None, db=None):
#    """Initializes the global database object used by the app."""
#    if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
#       # force_auto_coercion()
#       # load_models()
#       db.init_app(app)
#    else:
#       raise ValueError('Cannot init DB without db and app objects.')









# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy.dialects.postgresql import UUID


# # # 10443 install notes

# # __all__ = ('db', 'init_db')

# # db = SQLAlchemy()

# # # query = db.session.query

# # def init_db(app=None, db=None):
# #   """Initializes the global database object used by the app."""
# #   if isinstance(app, Flask) and isinstance(db, SQLAlchemy):

# #     db.init_app(app)
  
# #   else:
# #     raise ValueError('Cannot init DB without db and app objects.')

# # app = Flask(__name__)

# # # conn = psycopg2.connect("dbname='homework_db' user='tanya' host='localhost'")

# # # cursor = conn.cursor()

# # # def create_all():
# # #   cursor.execute('''
# # #     CREATE TABLE IF NOT EXISTS Users (
# # #       user_id SERIAL PRIMARY KEY,
# # #       first_name VARCHAR NOT NULL, 
# # #       last_name VARCHAR,
# # #       email VARCHAR NOT NULL UNIQUE,
# # #       phone VARCHAR,
# # #       city VARCHAR, 
# # #       state VARCHAR,
# # #       org_id INTEGER,
# # #       active SMALLINT
# # #     );
# # #   ''')

# # #   cursor.execute('''
# # #     CREATE TABLE IF NOT EXISTS Organizations (
# # #       org_id SERIAL PRIMARY KEY,
# # #       name VARCHAR NOT NULL,
# # #       phone VARCHAR,
# # #       city VARCHAR, 
# # #       state VARCHAR,
# # #       active SMALLINT
# # #     );
# # #     ''')

# # #   print("Creating tables...")
# # #   conn.commit()

# # @app.route('/user/add', methods=['POST'] )
# # def user_add():
# #   post_data = request.json
 
# #   first_name = post_data.get('first_name')
# #   last_name = post_data.get('last_name')
# #   email = post_data.get('email')
# #   phone = post_data.get('phone')
# #   city = post_data.get('city')
# #   state = post_data.get('state')  
# #   org_id = post_data.get('org_id')
# #   active = post_data.get('active')

# #   add_user(first_name, last_name, email, phone, city, state, org_id, active)

# #   return jsonify("User created"), 201

# # def add_user(first_name, last_name, email, phone, city, state, org_id, active):
# #   cursor.execute(f"""
# #   INSERT INTO Users
# #   (first_name, last_name, email, phone, city, state, org_id, active)
# #   VALUES
# #   (%s, %s, %s, %s, %s, %s, %s, %s);""",
# #   (first_name, last_name, email, phone, city, state, org_id, active))
# #   conn.commit()

# # # @app.route('/user_by_id/<user_id>', methods=['GET'] )
# # # def get_user_by_id(user_id):
# # #   cursor.execute('SELECT * FROM users WHERE user_id=%s;', [user_id])
# # #   results = cursor.fetchone()

# # #   if results[7] != None:
# # #     cursor.execute("""
# # #       SELECT U.user_id, U.first_name, U.last_name, U.email, U.phone, U.city, U.state, U.active FROM Users U JOIN Organizations O ON U.org_id=O.org_id
# # #         WHERE U.user_id=%s;""", 
# # #         [user_id])
# # #     results = cursor.fetchone()

# # #   if len(results) > 9: 
# # #     user = {
# # #       'user_id': results[0],
# # #       'first_name': results[1],
# # #       'last_name': results[2],
# # #       'email': results[3],
# # #       'phone': results[4],
# # #       'city': results[5],
# # #       'state': results[6],
# # #       'organization': {
# # #         'org_id': results[7],
# # #         'name': results[8],
# # #         'phone': results[9],
# # #         'city': results[10],
# # #         'state': results[11]
# # #       },
# # #       'active': [12]
# # #     }
# # #     return jsonify(user), 200

# # #   elif len(results) == 9:
# # #     user = {
# # #         'user_id': results[0],
# # #         'first_name': results[1],
# # #         'last_name': results[2],
# # #         'email': results[3],
# # #         'phone': results[4],
# # #         'city': results[5],
# # #         'state': results[6],
# # #         'org_id': results[7],
# # #         'active': results[8]

# # #     }
# # #     return jsonify(user), 200
# # #   else:
# # #     return jsonify('No User Found'), 400

# # # @app.route('/active_users', methods=['GET'] )
# # # def get_all_active_users():
# # #   cursor.execute('SELECT user_id, first_name, last_name, phone, city, state, org_id, active FROM users WHERE active=1')
# # #   results = cursor.fetchall()

# # #   user_list = []

# # #   for users in results:
# # #     if users[7] is not None:
# # #       cursor.execute(f'''
# # #         SELECT org_id, name, phone, city, state 
# # #           FROM Organizations 
# # #           WHERE org_id={users[7]};
# # #         ''')
# # #       org = cursor.fetchone()

   
# # #       user = {
# # #         'user_id': users[0],
# # #         'first_name': users[1],
# # #         'last_name': users[2],
# # #         'email': users[3],
# # #         'phone': users[4],
# # #         'city': users[5],
# # #         'state': users[6],
# # #         'organization': {
# # #           'org_id': org[0],
# # #           'name': org[1],
# # #           'phone': org[2],
# # #           'city': org[3],
# # #           'state': org[4]
# # #         },
# # #         'active': users[8]
# # #       }
# # #       return jsonify(user), 200

# # #   else:
# # #     user = {
# # #         'user_id': results[0],
# # #         'first_name': results[1],
# # #         'last_name': results[2],
# # #         'email': results[3],
# # #         'phone': results[4],
# # #         'city': results[5],
# # #         'state': results[6],
# # #         'org_id': results[7],
# # #         'active': results[8]

# # #     }
# # #     user_list.append(user)

# # #     return jsonify(user_list), 200
# # #   return jsonify("No active users found"), 404


# # # @app.route('/user/activate/<user_id>', methods=['POST'])
# # # def user_activate(user_id):
# # #   cursor.execute('UPDATE users SET active=1 WHERE user_id=%s', [user_id])

# # #   conn.commit()

# # #   return jsonify('User Activated'), 200

# # # @app.route('/user/deactivate/<user_id>', methods=['POST'])
# # # def user_deactivate(user_id):
# # #   cursor.execute('UPDATE users SET active=0 WHERE user_id=%s', [user_id])

# # #   conn.commit()

# # #   return jsonify('User Deactivated'), 200

# # # @app.route('/user/delete/<user_id>', methods=['DELETE'])
# # # def user_delete(user_id):
# # #   cursor.execute('DELETE FROM Users WHERE user_id=%s', [user_id])

# # #   conn.commit()

# # #   return jsonify('User Deleted'), 200

# # # @app.route('/user/update/<user_id>', methods=['POST', 'PUT'] )
# # # def user_update(user_id):
# # #   update_fields = []
# # #   update_values = []
# # #   field_names = ['first_name', 'last_name', 'email', 'phone', 'city', 'state', 'org_id', 'active']

# # #   post_data = request.json

# # #   for field in field_names:
# # #     field_value = post_data.get(field)
# # #     if field_value:
# # #       update_fields.append(str(field) + "=%s")
# # #       update_values.append(field_value)

# # #   if update_fields:
# # #     update_values.append(user_id)

# # #     query_string = f"UPDATE users SET " + ", ".join(update_fields) + "WHERE user_id=%s"

# # #     cursor.execute(query_string, update_values)
# # #     conn.commit()

# # #     return jsonify('User values updated'), 200

# # #   else:
# # #     return jsonify('No values sent in body'), 418

# # # # if __name__ == '__main__':
# # # #   create_all()
# # # #   app.run(port='8089')

# # # # Organizations
# # # # Organizations
# # # # Organizations
# # # # Organizations
# # # # Organizations
# # # # Organizations

# # @app.route('/org/add', methods=['POST'] )
# # def org_add():
# #   post_data = request.json
# #   name = post_data.get('name')
# #   phone = post_data.get('phone')
# #   city = post_data.get('city')
# #   state = post_data.get('state')  
# #   active = post_data.get('active')

# #   add_org(name,phone, city, state, active)

# #   return jsonify("Org created"), 201

# # # def add_org(name, phone, city, state, active):
# # #   cursor.execute(f"""
# # #   INSERT INTO Organizations
# # #   (name, phone, city, state, active)
# # #   VALUES
# # #   (%s, %s, %s, %s, %s);""",
# # #   (name, phone, city, state, active))
# # #   conn.commit()

# # # @app.route('/org_by_id/<org_id>', methods=['GET'])
# # # def  get_org_by_id(org_id):
# # #   cursor.execute('SELECT * FROM organizations WHERE org_id=%s;', (org_id))
# # #   results = cursor.fetchone()

# # #   if results:
# # #     org = {
# # #       'org_id': results[0],
# # #       'name': results[1],
# # #       'phone': results[2],
# # #       'city': results[3],
# # #       'state': results[4],
# # #       'active': results[5],
# # #     }
# # #     return jsonify(org), 200

# # #   else: 
# # #     return jsonify('No Organization Found'), 400

# # # @app.route('/active', methods=['GET'])
# # # def  get_all_active_orgs():
# # #   cursor.execute('SELECT * FROM organizations WHERE active=1;')
# # #   results = cursor.fetchall()

# # #   for orgs in results:
# # #     org_list = []

# # #     org = {
# # #       'org_id': orgs[0],
# # #       'name': orgs[1],
# # #       'phone': orgs[2],
# # #       'city': orgs[3],
# # #       'state': orgs[4],
# # #       'active': orgs[5],
# # #     }

# # #     org_list.append(org)

# # #     if org in org_list:
# # #       return jsonify(org_list), 200

# # #   else: 
# # #     return jsonify('No Organization Found'), 400

# # # @app.route('/org/activate/<org_id>', methods=['POST'])
# # # def org_activate(org_id):
# # #   cursor.execute('UPDATE Organizations SET active=1 WHERE org_id=%s', [org_id])

# # #   conn.commit()

# # #   return jsonify('Organization Activated'), 200

# # # @app.route('/org/deactivate/<org_id>', methods=['POST'])
# # # def org_deactivate(org_id):
# # #   cursor.execute('UPDATE Organizations SET active=0 WHERE org_id=%s', [org_id])

# # #   conn.commit()
  
# # #   return jsonify('Organization Deactivated'), 200

# # # @app.route('/org/delete/<org_id>', methods=['DELETE'])
# # # def org_delete(org_id):
# # #   cursor.execute('DELETE FROM Organizations WHERE org_id=%s', [org_id])

# # #   conn.commit()
  
# # #   return jsonify('Organization Deleted'), 200

# # # @app.route('/org/update/<org_id>', methods=['POST', 'PUT'] )
# # # def org_update(org_id):
# # #   update_fields = []
# # #   update_values = []
# # #   field_names = ['name', 'phone', 'city', 'state', 'active']

# # #   post_data = request.json

# # #   for field in field_names:
# # #     field_value = post_data.get(field)
# # #     if field_value:
# # #       update_fields.append(str(field) + "=%s")
# # #       update_values.append(field_value)

# # #   if update_fields:
# # #     update_values.append(org_id)

# # #     query_string = f"UPDATE organizations SET " + ", ".join(update_fields) + "WHERE org_id=%s"

# # #     cursor.execute(query_string, update_values)
# # #     conn.commit()

# # #     return jsonify('Organization values updated'), 200

# # #   else:
# # #     return jsonify('No values sent in body'), 418

# # # if __name__ == '__main__':
# # #   create_all()
# # #   app.run(host='0.0.0.0', port="8089")




