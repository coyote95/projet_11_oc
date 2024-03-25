import json, datetime
from flask import Flask,render_template,request,redirect,flash,url_for
from dotenv import load_dotenv

load_dotenv()


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except:
        error_message = "Sorry, that email wasn't found."
        return render_template('index.html', error_message=error_message)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():

    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if competition and club:
        current_date = datetime.datetime.now().date()
        competition_date = datetime.datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S').date()

        if competition_date >= current_date:
            if placesRequired <=12:
                if int(club["points"]) >= placesRequired  :
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
                    club['points'] = int(club['points']) - placesRequired #update points club
                    flash('Great-booking complete!')

                else:
                    flash('Error: Insufficient places available for booking!')
            else:
                flash('Error: You cannot book more than 12 places!')
        else:
            flash('Error: The competition has already passed.')

    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))