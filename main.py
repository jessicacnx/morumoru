from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# init
level=0
num_of_flowers=0

# information for now (from database)
name = "Snorlax"
num_of_tasks_completed_today = "1"
num_of_stars = int("70")
total_spent = int("15")
purchased= [1,2]

# calculating levels
for i in range(50):
  if num_of_stars -1 > 0:
    num_of_stars = num_of_stars - i
    i+=1
    level+=1
    num_of_flowers+=i
  else:
    break
  
  # could add tier system here

# level up (for the animation)
remainder = i - num_of_stars
if remainder==i:
  levelup = True
else: 
  levelup = False

# calculating flowers
num_of_flowers -= total_spent

# dashboard
@app.route('/')
def index():
  return render_template('index.html', name=name, num_of_tasks_completed_today=num_of_tasks_completed_today, level=level, remainder=remainder )

# home
@app.route('/home')
def home():
  return render_template('moruhome.html')

# shop
@app.route('/shop')
def shop():
  return render_template('morushop.html')

# help
@app.route('/help')
def help():
  return render_template('help.html')

# portal
#@app.route('/portal')
#def portal():
  #return render_template('help.html')

# media file
#@app.route('/uploads/<path:filename>')
#def download_file(filename):
    #return send_from_directory(MEDIA_FOLDER, filename, #as_attachment=True)

app.run(host='0.0.0.0', port=8080)