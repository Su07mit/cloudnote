from flask import Flask, render_template, request, redirect, jsonify
import boto3
import uuid
from datetime import datetime
import json

app = Flask(__name__)

AWS_REGION = 'us-east-1'
AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
S3_BUCKET = 'cloudnote-backup-2026'

db = boto3.resource('dynamodb', region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY)

s3 = boto3.client('s3', region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY)

table = db.Table('Notes')

@app.route('/')
def home():
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    response = table.scan()
    notes = response['Items']
    if search:
        notes = [n for n in notes if search.lower() in n['note'].lower()]
    if category:
        notes = [n for n in notes if n.get('category') == category]
    notes = sorted(notes, key=lambda x: (x.get('pinned', False) == False, x.get('timestamp', '')))
    return render_template('home.html', notes=notes, search=search, category=category)

@app.route('/add', methods=['POST'])
def add():
    note = request.form['note']
    category = request.form.get('category', 'General')
    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'note': note,
        'category': category,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'pinned': False
    })
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    table.delete_item(Key={'id': id})
    return redirect('/')

@app.route('/pin/<id>')
def pin(id):
    response = table.get_item(Key={'id': id})
    note = response['Item']
    current = note.get('pinned', False)
    table.update_item(
        Key={'id': id},
        UpdateExpression='SET pinned = :p',
        ExpressionAttributeValues={':p': not current}
    )
    return redirect('/')

@app.route('/backup')
def backup():
    response = table.scan()
    notes = response['Items']
    backup_data = json.dumps(notes, indent=2, default=str)
    filename = f"backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=filename,
        Body=backup_data,
        ContentType='application/json'
    )
    return redirect('/?backed_up=true')

@app.route('/edit/<id>', methods=['POST'])
def edit(id):
    data = request.get_json()
    table.update_item(
        Key={'id': id},
        UpdateExpression='SET note = :n',
        ExpressionAttributeValues={':n': data['note']}
    )
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)



