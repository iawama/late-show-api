from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.appearance import Appearance
from models.guest import Guest
from models.episode import Episode
from app import db

bp = Blueprint('appearances', __name__)

@bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    
    if not all([rating, guest_id, episode_id]):
        return jsonify({'error': 'Missing required fields'}), 400
        
    if not Guest.query.get(guest_id) or not Episode.query.get(episode_id):
        return jsonify({'error': 'Invalid guest_id or episode_id'}), 400
        
    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400