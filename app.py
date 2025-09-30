from flask import Flask
app = Flask(__name__)
@app.route("/")
def weather():
  return """
  <h1>Прогноз погоди</h1>
  <ul>
    <li>Київ: 18°C, сонячно</li>
    <li>Львів: 16°C, хмарно</li>
    <li>Одеса: 20°C, дощ</li>
  </ul>
  """
if __name__ == "__main__":
  import os
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
