from flask import Blueprint, jsonify, request

# Update the to the actual endpoint from Nexus Mods
bp = Blueprint('games', __name__, url_prefix='/games')
