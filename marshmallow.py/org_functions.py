# import json
# import psycopg2
# from alchemy import create_all
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# conn = psycopg2.connect ("dbname='homework' user='tanya' host='localhost'")
# cursor = conn.cursor()

# @app.route('/org/add', methods=['POST'] )
# def org_add():
#   post_data = request.json
#   name = post_data.get('name')
#   phone = post_data.get('phone')
#   city = post_data.get('city')
#   state = post_data.get('state')  
#   active = post_data.get('active')

#   add_org(name,phone, city, state, active)

#   return jsonify("Org created"), 201

# def add_org(name, phone, city, state, active):
#   cursor.execute(f"""
#   INSERT INTO Organizations
#   (name, phone, city, state, active)
#   VALUES
#   (%s, %s, %s, %s, %s,);""",
#   (name, phone, city, state, active))
#   conn.commit()

# @app.route('/org_by_id/<org_id>', methods=['GET'])
# def  get_org_by_id(org_id):
#   cursor.execute('SELECT * FROM organizations WHERE org_id=%s;', (org_id))
#   results = cursor.fetchone()

#   if results:
#     org = {
#       'org_id': results[0],
#       'name': results[1],
#       'phone': results[2],
#       'city': results[3],
#       'state': results[4],
#       'active': results[5],
#     }
#     return jsonify(org), 200

#   else: 
#     return jsonify('No Organization Found'), 400

# @app.route('/active', methods=['GET'])
# def  get_all_active_orgs():
#   cursor.execute('SELECT * FROM organizations WHERE active=1;')
#   results = cursor.fetchall()

#   for orgs in results:
#     org_list = []

#     org = {
#       'org_id': orgs[0],
#       'name': orgs[1],
#       'phone': orgs[2],
#       'city': orgs[3],
#       'state': orgs[4],
#       'active': orgs[5],
#     }

#     org_list.append(org)

#     if org in org_list:
#       return jsonify(org_list), 200

#   else: 
#     return jsonify('No Organization Found'), 400

# @app.route('/org/activate/<org_id>', methods=['POST'])
# def org_activate(org_id):
#   cursor.execute('UPDATE Organizations SET active=1 WHERE org_id=%s', [org_id])

#   conn.commit()

#   return jsonify('Organization Activated'), 200

# @app.route('/org/deactivate/<org_id>', methods=['POST'])
# def org_deactivate(org_id):
#   cursor.execute('UPDATE Organizations SET active=0 WHERE org_id=%s', [org_id])

#   conn.commit()
  
#   return jsonify('Organization Deactivated'), 200

# @app.route('/org/delete/<org_id>', methods=['DELETE'])
# def org_delete(org_id):
#   cursor.execute('DELETE FROM Organizations WHERE org_id=%s', [org_id])

#   conn.commit()
  
#   return jsonify('Organization Deleted'), 200

# @app.route('/org/update/<org_id>', methods=['POST', 'PUT'] )
# def org_update(org_id):
#   update_fields = []
#   update_values = []
#   field_names = ['name', 'phone', 'city', 'state', 'active']

#   post_data = request.json

#   for field in field_names:
#     field_value = post_data.get(field)
#     if field_value:
#       update_fields.append(str(field) + "=%s")
#       update_values.append(field_value)

#   if update_fields:
#     update_values.append(org_id)

#     query_string = f"UPDATE organizations SET " + ", ".join(update_fields) + "WHERE org_id=%s"

#     cursor.execute(query_string, update_values)
#     conn.commit()

#     return jsonify('Organization values updated'), 200

#   else:
#     return jsonify('No values sent in body'), 418

# if __name__ == '__main__':
#   create_all
#   app.run(host='0.0.0.0', port="8089")


