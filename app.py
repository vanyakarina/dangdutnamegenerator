from flask import Flask, render_template, request

app = Flask(__name__)

# Define name lists
male_first_names = [
    "Yanto", "Ujang", "Rinto", "Eko", "Dadang", "Asep", "Rohman", "Tresno", "Koswara", "Deden", 
    "Saiful", "Bahri", "Burhan", "Udin", "Donny", "Bram", "Dedi", "Iskandar", "Aceng", "Supri", 
    "Jajang", "Beny", "Rusman", "Jaka", "Wendi", "Iman", "Aan", "Emon", "Hans", "Memet", "Entis"
]

female_first_names = [
    "Mona", "Murni", "Dewi", "Mulan", "Titin", "Yuli", "Wati", "Lina", "Siti", "Iis", "Ainun", 
    "Euis", "Icha", "Sulis", "Nyai", "Mawar", "Melati", "Rosa", "Yuni", "Mamah", "Pipin", 
    "Wati", "Yanti", "Lani", "Imas", "Nur", "Vina", "Dora", "Sandy", "Neneng", "Astuti"
]

male_last_names = [
    "Spakbor", "Karbu", "Hercules", "Pintu", "Power Window", "Bandros", "Tombak", "Knalpot", 
    "Melarat", "Belang", "Wordpress", "Coboy"
]

female_last_names = [
    "Rombeng", "Pelet", "Aduhai", "Vario", "Subur", "Mesra", "Manja", "Jambak", "Blackberry", 
    "Semok", "Supra", "Melorot"
]

def get_name_from_date(day, month, gender):
    if not (1 <= day <= 31) or not (1 <= month <= 12):
        return "Tanggal dan Bulan lahir salah."
    
    if gender == 'L':
        first_names = male_first_names
        last_names = male_last_names
    elif gender == 'P':
        first_names = female_first_names
        last_names = female_last_names
    else:
        return "Jenis kelamin hanya bisa P (perempuan) atau L (laki-laki)"
    
    first_name = first_names[day - 1] if day <= len(first_names) else "Unknown"
    last_name = last_names[month - 1] if month <= len(last_names) else "Unknown"

    return f"{first_name} {last_name}"

@app.route('/', methods=['GET', 'POST'])
def index():
    fictional_name = None
    if request.method == 'POST':
        day = int(request.form['day'])
        month = int(request.form['month'])
        gender = request.form['gender']
        fictional_name = get_name_from_date(day, month, gender)
    return render_template('index.html', fictional_name=fictional_name)

if __name__ == '__main__':
    app.run(debug=True)
