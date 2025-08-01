const table = document.getElementById('table');
const rows = document.getElementsByClassName('rows');
const all = document.querySelector('.total');
const totals = all.querySelectorAll('h5');
const button = document.querySelector('button');
const form = document.getElementsByTagName('form')[0];

const proteins = [];
const carbs = [];
const fats = [];
const calories = [];

for (let i = 0; i < rows.length; i++) {
    proteins.push(rows[i].children[1].textContent);
    carbs.push(rows[i].children[2].textContent);
    fats.push(rows[i].children[3].textContent);
    calories.push(rows[i].children[4].textContent);
}

const protein = proteins.reduce((a, b) => a + parseFloat(b), 0).toFixed(2);
const carb = carbs.reduce((a, b) => a + parseFloat(b), 0).toFixed(2);
const fat = fats.reduce((a, b) => a + parseFloat(b), 0).toFixed(2);
const cal = calories.reduce((a, b) => a + parseFloat(b), 0).toFixed(2);

button.addEventListener('click', () => {
    console.log(protein);
    form.submit();
});
totals[0].textContent = "Total";
totals[1].textContent = protein;
totals[2].textContent = carb;
totals[3].textContent = fat;
totals[4].textContent = cal;