from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/api/waitlist', methods=['POST'])
def waitlist():
    try:
        data = request.json
        email = data.get('email', '').strip()
        if not email:
            return jsonify({'success': False, 'error': 'Email is required'}), 400
        
        # Simple validation
        if '@' not in email or '.' not in email:
            return jsonify({'success': False, 'error': 'Invalid email format'}), 400
            
        with open('waitlist.txt', 'a') as f:
            f.write(f"{datetime.now().isoformat()} - {email}\n")
            
        return jsonify({'success': True, 'message': 'Added to waitlist'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
