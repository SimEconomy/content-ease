from flask import Flask, request, jsonify
import easegen.core_requirements as core

app = Flask(__name__)

@app.route('/generate/text', methods=['POST'])
def generate_text():
    data = request.get_json()
    if 'params' not in data:
        return jsonify({'status': 'error', 'message': 'Missing params'}), 400
    content_type = data['params']['type']
    params = {key: value for key, value in data['params'].items() if key != 'type'}
    generated_content = core.generate_text(content_type, **params)
    return jsonify({'status': 'success', 'content': generated_content})

@app.route('/generate/image', methods=['POST'])
def generate_image():
    data = request.get_json()
    if 'params' not in data:
        return jsonify({'status': 'error', 'message': 'Missing params'}), 400
    content_type = data['params']['type']
    params = {key: value for key, value in data['params'].items() if key != 'type'}
    generated_content = core.generate_image(content_type, **params)
    return jsonify({'status': 'success', 'content': generated_content})

@app.route('/generate/video', methods=['POST'])
def generate_video():
    data = request.get_json()
    if 'params' not in data:
        return jsonify({'status': 'error', 'message': 'Missing params'}), 400
    content_type = data['params']['type']
    params = {key: value for key, value in data['params'].items() if key != 'type'}
    generated_content = core.generate_video(content_type, **params)
    return jsonify({'status': 'success', 'content': generated_content})

if __name__ == '__main__':
    app.run()