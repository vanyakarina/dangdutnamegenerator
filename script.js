document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generate-button').addEventListener('click', function() {
        const day = parseInt(document.getElementById('day').value);
        const month = parseInt(document.getElementById('month').value);
        const gender = document.getElementById('gender').value;

        let firstName = 'Unknown';
        let lastName = 'Unknown';

        // Example name generation logic
        const maleFirstNames = ["Yanto", "Ujang", "Rinto", "Eko", "Dadang", "Asep", "Rohman", "Tresno", "Koswara", "Deden", "Saiful", "Bahri", "Burhan", "Udin", "Donny", "Bram", "Dedi", "Iskandar", "Aceng", "Supri", "Jajang", "Beny", "Rusman", "Jaka", "Wendi", "Iman", "Aan", "Emon", "Hans", "Memet", "Entis"];
        const femaleFirstNames = ["Mona", "Murni", "Dewi", "Mulan", "Titin", "Yuli", "Wati", "Lina", "Siti", "Iis", "Ainun", "Euis", "Icha", "Sulis", "Nyai", "Mawar", "Melati", "Rosa", "Yuni", "Mamah", "Pipin", "Wati", "Yanti", "Lani", "Imas", "Nur", "Vina", "Dora", "Sandy", "Neneng", "Astuti"];
        const maleLastNames = ["Spakbor", "Karbu", "Hercules", "Pintu", "Power Window", "Bandros", "Tombak", "Knalpot", "Melarat", "Belang", "Wordpress", "Coboy"];
        const femaleLastNames = ["Rombeng", "Pelet", "Aduhai", "Vario", "Subur", "Mesra", "Manja", "Jambak", "Blackberry", "Semok", "Supra", "Melorot"];

        if (gender === 'L') {
            firstName = day <= maleFirstNames.length ? maleFirstNames[day - 1] : 'Unknown';
            lastName = month <= maleLastNames.length ? maleLastNames[month - 1] : 'Unknown';
        } else if (gender === 'P') {
            firstName = day <= femaleFirstNames.length ? femaleFirstNames[day - 1] : 'Unknown';
            lastName = month <= femaleLastNames.length ? femaleLastNames[month - 1] : 'Unknown';
        }

        const result = `Nama dangdut kamu adalah ${firstName} ${lastName}`;
        document.getElementById('result').textContent = result;
    });
});
