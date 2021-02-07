let models = {
    'BMW': ['','M1', 'M2', 'M3', 'M4', 'M5', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6'],
    'Tesla': ['','Model S', 'Model 3', 'Model X', 'Model Y'],
    'Audi': ['','A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'],
    'Mercedes': ['','S', 'G', 'E', 'C', 'A', 'AMG'],
    'Mazda': ['','2', '3', '4', '5', 'MX', 'CX', 'BT'],
    'Volkswagen': ['','Beetle', 'Golf', 'Passat', 'Polo', 'Tiguan', 'Touareg', 'CC'],
    'Ford': ['','Mustang', 'GT', 'Explorer', 'Fiesta', 'Focus', 'Kuga'],
    'Chevrolet': ['','Camaro', 'Corvette', 'Cavalier', 'Malibu', 'Express'],
    'Honda': ['','Civic', 'CR-V', 'Jade', 'Accord', 'Clarity'],
    'Toyota': ['','Corolla', 'Prius', 'Avalon', 'RAV', 'Venza']
}

document.getElementById('id_brand').addEventListener('change', (e) => {
     let selectElement = document.getElementById('id_models')
    if (e.target.value === '') {
        selectElement.innerHTML = ''
        return
    }

    selectElement.innerHTML = ''
    models[e.target.value].forEach(el => {
        let optionEle = document.createElement('option')
        optionEle.innerText = el
        selectElement.appendChild(optionEle)
    })

})