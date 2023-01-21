from flask import Blueprint, jsonify, request

# Update the to the actual endpoint from Nexus Mods
bp = Blueprint('new_mods', __name__, url_prefix='/new_mods')
