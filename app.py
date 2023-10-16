from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
import pandas as pd
import csv

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
@app.route('/')
def hello():
    return render_template('Scanner.html')

# Load the CSV file and store the data
with open(r'.\input.csv') as icsv:
    heading = next(icsv)
    reader = csv.reader(icsv)
    entries = list(reader)


# Define the form
class SchoolForm(FlaskForm):
    #do the same for School code	School Name	Contact Number of school	Teacher escort	Contact Number of teacher escort	Drama	Participant1	Grade	Participant2	Grade	Participant3	Grade	Particpate-4	Grade	Participant5	Grade	Participant6	Grade	Participant7	Grade	Participant8	Grade	Art	Participant1	Grade	Participant2	Grade	Participant3	Grade	Participant4	Grade	Music	Participant1	Grade	Participant2	Grade	Participant3	Grade	Participant4	Grade	Participant5	Grade	Participant6	Grade	Participant7	Grade	Participant8	Grade	Participant9	Grade	Participant10	Grade	Participant11	Grade	Participant12	Grade	Dance	Participant1	Grade	Participant2	Grade	Participant3	Grade	Participant4	Grade	Participant5	Grade	Participant6	Grade	Participant7	Grade	Participant8	Grade	Participant9	Grade	Participant10	Grade	Participant11	Grade	Participant12	Grade

    school_name = StringField('School Name')
    school_contact = StringField('Contact Number of school')
    teacher_name = StringField('Teacher escort')
    teacher_contact = StringField('Contact Number of teacher escort')
    # Drama
    s1DramaN = StringField('Participant 1')
    s1DramaG = StringField('Grade')
    s2DramaN = StringField('Participant 2')
    s2DramaG = StringField('Grade')
    s3DramaN = StringField('Participant 3')
    s3DramaG = StringField('Grade')
    s4DramaN = StringField('Participant 4')
    s4DramaG = StringField('Grade')
    s5DramaN = StringField('Participant 5')
    s5DramaG = StringField('Grade')
    s6DramaN = StringField('Participant 6')
    s6DramaG = StringField('Grade')
    s7DramaN = StringField('Participant 7')
    s7DramaG = StringField('Grade')
    s8DramaN = StringField('Participant 8')
    s8DramaG = StringField('Grade')

    # Art
    s1ArtN = StringField('Participant 1')
    s1ArtG = StringField('Grade')
    s2ArtN = StringField('Participant 2')       
    s2ArtG = StringField('Grade')
    s3ArtN = StringField('Participant 3')
    s3ArtG = StringField('Grade')
    s4ArtN = StringField('Participant 4')
    s4ArtG = StringField('Grade')

    # Music
    s1MusicN = StringField('Participant 1')
    s1MusicG = StringField('Grade')
    s2MusicN = StringField('Participant 2')
    s2MusicG = StringField('Grade')
    s3MusicN = StringField('Participant 3')
    s3MusicG = StringField('Grade')
    s4MusicN = StringField('Participant 4')
    s4MusicG = StringField('Grade')
    s5MusicN = StringField('Participant 5')
    s5MusicG = StringField('Grade')
    s6MusicN = StringField('Participant 6')
    s6MusicG = StringField('Grade')
    s7MusicN = StringField('Participant 7')
    s7MusicG = StringField('Grade')
    s8MusicN = StringField('Participant 8')
    s8MusicG = StringField('Grade')
    s9MusicN = StringField('Participant 9')
    s9MusicG = StringField('Grade')
    s10MusicN = StringField('Participant 10')
    s10MusicG = StringField('Grade')
    s11MusicN = StringField('Participant 11')
    s11MusicG = StringField('Grade')
    s12MusicN = StringField('Participant 12')
    s12MusicG = StringField('Grade')

    # Dance
    s1DanceN = StringField('Participant 1')
    s1DanceG = StringField('Grade')
    s2DanceN = StringField('Participant 2')
    s2DanceG = StringField('Grade')
    s3DanceN = StringField('Participant 3')
    s3DanceG = StringField('Grade')
    s4DanceN = StringField('Participant 4')
    s4DanceG = StringField('Grade')
    s5DanceN = StringField('Participant 5')
    s5DanceG = StringField('Grade')
    s6DanceN = StringField('Participant 6')
    s6DanceG = StringField('Grade')
    s7DanceN = StringField('Participant 7')
    s7DanceG = StringField('Grade')
    s8DanceN = StringField('Participant 8')
    s8DanceG = StringField('Grade')
    s9DanceN = StringField('Participant 9')
    s9DanceG = StringField('Grade')
    s10DanceN = StringField('Participant 10')
    s10DanceG = StringField('Grade')
    s11DanceN = StringField('Participant 11')
    s11DanceG = StringField('Grade')
    s12DanceN = StringField('Participant 12')
    s12DanceG = StringField('Grade')

    

# Submit button
    submit = SubmitField('Submit')





# Route to display the form
@app.route('/form/<school_code>', methods=['GET', 'POST'])
def form(school_code):
    # Find the corresponding entry based on the school code
    entry = next((entry for entry in entries if entry[0] == school_code), None)
    print(entry)
    length = len(entry)
    # Pre-populate the form with the entry data School code	School Name	Contact Number of school	Teacher escort	Contact Number of teacher escort	Drama	Name of Teacher Incharge	Teacher Incharge email	Participant1	Grade	Participant2	Grade	Participant3	Grade	Particpate-4	Grade	Participant5	Grade	Participant6	Grade	Participant7	Grade	Participant8	Grade	Art	Name of Teacher incharge	Teacher incharge email	Participant1	Grade	Participant2	Grade	Participant3	Grade	Participant4	Grade	Music	Teacher incharge email	Participant1	Grade	Participant2	Grade	Participant3	Grade	Participant4	Grade	Participant5	Grade	Participant6	Grade	Participant7	Grade	Participant8	Grade	Participant9	Grade	Participant10	Grade	Participant11	Grade	Participant12	Grade	Dance	Teacher incharge email	Participant1	Grade	Participant2	Grade	Participant3	Grade	Participant4	Grade	Participant5	Grade	Participant6	Grade	Participant7	Grade	Participant8	Grade	Participant9	Grade	Participant10	Grade	Participant11	Grade	Participant12	Grade
    form = SchoolForm(
                        school_name=entry[1] if length > 1 else '', school_contact=entry[2] if length > 2 else '',
                        teacher_name=entry[3] if length > 3 else '', teacher_contact=entry[4] if length > 4 else '',
                        
                        s1DramaN=entry[6] if length > 6 else '', s1DramaG=entry[7] if length > 7 else '',
                        s2DramaN=entry[8] if length > 8 else '', s2DramaG=entry[9] if length > 9 else '',
                        s3DramaN=entry[10] if length > 10 else '', s3DramaG=entry[11] if length > 11 else '',
                        s4DramaN=entry[12] if length > 12 else '', s4DramaG=entry[13] if length > 13 else '',
                        s5DramaN=entry[14] if length > 14 else '', s5DramaG=entry[15] if length > 15 else '',
                        s6DramaN=entry[16] if length > 16 else '', s6DramaG=entry[17] if length > 17 else '',
                        s7DramaN=entry[18] if length > 18 else '', s7DramaG=entry[19] if length > 19 else '',
                        s8DramaN=entry[20] if length > 20 else '', s8DramaG=entry[21] if length > 21 else '',

                        s1ArtN=entry[23] if length > 23 else '', s1ArtG=entry[24] if length > 24 else '',
                        s2ArtN=entry[25] if length > 25 else '', s2ArtG=entry[26] if length > 26 else '',
                        s3ArtN=entry[27] if length > 27 else '', s3ArtG=entry[28] if length > 28 else '',
                        s4ArtN=entry[29] if length > 29 else '', s4ArtG=entry[30] if length > 30 else '',

                        s1MusicN=entry[32] if length > 32 else '', s1MusicG=entry[33] if length > 33 else '',
                        s2MusicN=entry[34] if length > 34 else '', s2MusicG=entry[35] if length > 35 else '',
                        s3MusicN=entry[36] if length > 36 else '', s3MusicG=entry[37] if length > 37 else '',
                        s4MusicN=entry[38] if length > 38 else '', s4MusicG=entry[39] if length > 39 else '',
                        s5MusicN=entry[40] if length > 40 else '', s5MusicG=entry[41] if length > 41 else '',
                        s6MusicN=entry[42] if length > 42 else '', s6MusicG=entry[43] if length > 43 else '',
                        s7MusicN=entry[44] if length > 44 else '', s7MusicG=entry[45] if length > 45 else '',
                        s8MusicN=entry[46] if length > 46 else '', s8MusicG=entry[47] if length > 47 else '',
                        s9MusicN=entry[48] if length > 48 else '', s9MusicG=entry[49] if length > 49 else '',
                        s10MusicN=entry[50] if length > 50 else '', s10MusicG=entry[51] if length > 51 else '',
                        s11MusicN=entry[52] if length > 52 else '', s11MusicG=entry[53] if length > 53 else '',
                        s12MusicN=entry[54] if length > 54 else '', s12MusicG=entry[55] if length > 55 else '',

                        s1DanceN=entry[57] if length > 57 else '', s1DanceG=entry[58] if length > 58 else '',
                        s2DanceN=entry[59] if length > 59 else '', s2DanceG=entry[60] if length > 60 else '',
                        s3DanceN=entry[61] if length > 61 else '', s3DanceG=entry[62] if length > 62 else '',
                        s4DanceN=entry[63] if length > 63 else '', s4DanceG=entry[64] if length > 64 else '',
                        s5DanceN=entry[65] if length > 65 else '', s5DanceG=entry[66] if length > 66 else '',
                        s6DanceN=entry[67] if length > 67 else '', s6DanceG=entry[68] if length > 68 else '',
                        s7DanceN=entry[69] if length > 69 else '', s7DanceG=entry[70] if length > 70 else '',
                        s8DanceN=entry[71] if length > 71 else '', s8DanceG=entry[72] if length > 72 else '',
                        s9DanceN=entry[73] if length > 73 else '', s9DanceG=entry[74] if length > 74 else '',
                        s10DanceN=entry[75] if length > 75 else '', s10DanceG=entry[76] if length > 76 else '',
                        s11DanceN=entry[77] if length > 77 else '', s11DanceG=entry[78] if length > 78 else '',
                        s12DanceN=entry[79] if length > 79 else '', s12DanceG=entry[80] if length > 80 else ''                    
                      )

    # Assign entry values to form fields

    # form.school_name.default = entry[1]
    # form.teacher_name.default = entry[2]
    # form.teacher_contact.default = entry[3]
    # form.student_name.default = entry[4]
    # form.student_contact.default = entry[5]
    # form.participate1.default = entry[6] == 'Yes'
    # form.student1.default = entry[7]
    # form.student2.default = entry[8]
    # form.student3.default = entry[9]
    # form.participate2.default = entry[10] == 'Yes'
    # form.student4.default = entry[11]
    # form.student5.default = entry[12]
    # form.student6.default = entry[13]
    # form.participate3.default = entry[14] == 'Yes'
    # form.student7.default = entry[15]
    # form.student8.default = entry[16]
    # form.student9.default = entry[17]
    # form.process()
    # If the form is submitted and valid, add the data to a new csv file named "output.csv"
# `school_code=entry[0]
# , drama_part=entry[5] == 'Yes'
# , art_part=entry[24] == 'Yes'
# music_part=entry[35] == 'Yes',
# , dance_part=entry[62] == 'Yes'`
    if form.validate_on_submit():

        with open('.\output.csv', 'a') as ocsv:
# export the same data to a csv file
            formData = [
                        school_code, form.school_name.data, form.school_contact.data, form.teacher_name.data,
                        form.teacher_contact.data, entry[5],
                        form.s1DramaN.data, form.s1DramaG.data, form.s2DramaN.data, form.s2DramaG.data,
                        form.s3DramaN.data, form.s3DramaG.data, form.s4DramaN.data, form.s4DramaG.data,
                        form.s5DramaN.data, form.s5DramaG.data, form.s6DramaN.data, form.s6DramaG.data,
                        form.s7DramaN.data, form.s7DramaG.data, form.s8DramaN.data, form.s8DramaG.data,
                        entry[22],  form.s1ArtN.data, form.s1ArtG.data,
                        form.s2ArtN.data, form.s2ArtG.data, form.s3ArtN.data, form.s3ArtG.data, form.s4ArtN.data,
                        form.s4ArtG.data, entry[31],
                        form.s1MusicN.data, form.s1MusicG.data, form.s2MusicN.data, form.s2MusicG.data,
                        form.s3MusicN.data, form.s3MusicG.data, form.s4MusicN.data, form.s4MusicG.data,
                        form.s5MusicN.data, form.s5MusicG.data, form.s6MusicN.data, form.s6MusicG.data,
                        form.s7MusicN.data, form.s7MusicG.data, form.s8MusicN.data, form.s8MusicG.data,
                        form.s9MusicN.data, form.s9MusicG.data, form.s10MusicN.data, form.s10MusicG.data,
                        form.s11MusicN.data, form.s11MusicG.data, form.s12MusicN.data, form.s12MusicG.data,
                        entry[56], form.s1DanceN.data,
                        form.s1DanceG.data, form.s2DanceN.data, form.s2DanceG.data, form.s3DanceN.data,
                        form.s3DanceG.data, form.s4DanceN.data, form.s4DanceG.data, form.s5DanceN.data,
                        form.s5DanceG.data, form.s6DanceN.data, form.s6DanceG.data, form.s7DanceN.data,
                        form.s7DanceG.data, form.s8DanceN.data, form.s8DanceG.data, form.s9DanceN.data,
                        form.s9DanceG.data, form.s10DanceN.data, form.s10DanceG.data, form.s11DanceN.data,
                        form.s11DanceG.data, form.s12DanceN.data, form.s12DanceG.data
                        ]

            print(formData)
            writer = csv.writer(ocsv)
            writer.writerow(formData)

        return render_template('thank_you.html')
    return render_template('form.html', form=form,
                           display1="block" if entry[5] == 'Yes' else "block",
                           display2="block" if entry[22] == 'Yes' else "block",
                           display3="block" if entry[31]== 'Yes' else "block",
                           display4="block" if entry[56] == 'No' else "block")


if __name__ == '__main__':
    app.run(debug=True)
