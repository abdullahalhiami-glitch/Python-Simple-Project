const display = document.getElementById('display');
const buttons = document.querySelectorAll('button');

let currentInput = '';
let operator = '';
let previousInput = '';

function updateDisplay() {
    if (previousInput && operator) {
        display.value = previousInput + ' ' + operator + ' ' + currentInput;
    } else {
        display.value = currentInput;
    }
}

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.textContent;

        if (value >= '0' && value <= '9' || value === '.') {
            currentInput += value;
            updateDisplay();
        } else if (value === 'C') {
            currentInput = '';
            operator = '';
            previousInput = '';
            display.value = '';
        } else if (value === '=') {
            if (previousInput && operator && currentInput) {
                const result = calculate(parseFloat(previousInput), parseFloat(currentInput), operator);
                display.value = result;
                currentInput = result.toString();
                operator = '';
                previousInput = '';
            }
        } else {
            if (currentInput && !operator) {
                previousInput = currentInput;
                operator = value;
                currentInput = '';
                updateDisplay();
            }
        }
    });
});

function calculate(a, b, op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            return b !== 0 ? a / b : 'Error';
        default:
            return 0;
    }
}