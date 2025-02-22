from flask import Blueprint, jsonify

integration_bp = Blueprint("integration", __name__)
@integration_bp.route("/integration", methods=["GET"])   
def integration():
    integration_json = {
       "data":{
          
          "date": {
              "created_at": "2025-02-20",
              "updated_at": "2025-02-20"
          },
          "descriptions": {
              "app_description": "A brief description of the application functionality.",
              "app_logo": "https://cdn.prod.website-files.com/5f05d5858fab461d0d08eaeb/654132b253b4e36b9d799ee4.webp",
              "app_name": "traker.",
              "app_url": "https://j9bj21z1-5000.euw.devtunnels.ms/integration",
              "background_color": "#HEXCODE"  
          },
          "integration_category": "Monitoring & Logging",
          "integration_type": "interval",
          "is_active": True,
          "output": [],
          "key_features": [
              "Feature description 1.",
              "Feature description 2.",
              "Feature description 3.",
              "Feature description 4."
          ],
          "permissions": {
              "monitoring_user": {
                  "always_online": True,
                  "display_name": "Performance Monitor"
              }
          },
          "settings": [
              {
                  "label": "interval",
                  "type": "text",
                  "required": True,
                  "default": "* * * * *"
              },
              {
                  "label": "Key",
                  "type": "text",
                  "required": True,
                  "default": "1234567890"
              },
              {
                  "label": "Do you want to continue",
                  "type": "checkbox",
                  "required": True,
                  "default": True  # Fixed to a boolean
              },
              {
                  "label": "Provide Speed",
                  "type": "number",
                  "required": True,
                  "default": 1000  # Fixed type from string to integer
              },
              {
                  "label": "Sensitivity Level",
                  "type": "dropdown",
                  "required": True,
                  "default": "Low",
                  "options": ["High", "Low"]
              },
              {
                  "label": "Alert Admin",
                  "type": "multi-checkbox",
                  "required": True,
                  "default": ["Super-Admin"],  # Changed to a list
                  "options": ["Super-Admin", "Admin", "Manager", "Developer"]
              }
          ],
          "tick_url": "",
          "target_url": "https://j9bj21z1-5000.euw.devtunnels.ms/webhook"
      }
    }

    return jsonify(integration_json)