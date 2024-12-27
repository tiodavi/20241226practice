<template>
  <div class="calculator-container">
    <div class="calculator">
      <div class="display">{{ display || '0' }}</div>
      <div class="buttons">
        <button class="btn operator" @click="clear">C</button>
        <button class="btn operator" @click="toggleSign">+/-</button>
        <button class="btn operator" @click="percentage">%</button>
        <button class="btn operator" @click="operate('÷')">÷</button>
        
        <button class="btn" @click="append('7')">7</button>
        <button class="btn" @click="append('8')">8</button>
        <button class="btn" @click="append('9')">9</button>
        <button class="btn operator" @click="operate('×')">×</button>
        
        <button class="btn" @click="append('4')">4</button>
        <button class="btn" @click="append('5')">5</button>
        <button class="btn" @click="append('6')">6</button>
        <button class="btn operator" @click="operate('-')">-</button>
        
        <button class="btn" @click="append('1')">1</button>
        <button class="btn" @click="append('2')">2</button>
        <button class="btn" @click="append('3')">3</button>
        <button class="btn operator" @click="operate('+')">+</button>
        
        <button class="btn zero" @click="append('0')">0</button>
        <button class="btn" @click="dot">.</button>
        <button class="btn operator" @click="equals">=</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CalculatorPage',
  data() {
    return {
      display: '',
      previousValue: null,
      operator: null,
      newNumber: false
    }
  },
  methods: {
    clear() {
      this.display = '';
      this.previousValue = null;
      this.operator = null;
    },
    append(number) {
      if (this.newNumber) {
        this.display = '';
        this.newNumber = false;
      }
      this.display = `${this.display}${number}`;
    },
    dot() {
      if (this.newNumber) {
        this.display = '0';
        this.newNumber = false;
      }
      if (!this.display.includes('.')) {
        this.display += '.';
      }
    },
    toggleSign() {
      this.display = this.display.charAt(0) === '-' ? 
        this.display.slice(1) : `-${this.display}`;
    },
    percentage() {
      this.display = `${parseFloat(this.display) / 100}`;
    },
    operate(operator) {
      this.calculate();
      this.previousValue = parseFloat(this.display);
      this.operator = operator;
      this.newNumber = true;
    },
    calculate() {
      if (this.previousValue !== null && this.operator !== null) {
        const current = parseFloat(this.display);
        let result = 0;

        switch (this.operator) {
          case '+':
            result = this.previousValue + current;
            break;
          case '-':
            result = this.previousValue - current;
            break;
          case '×':
            result = this.previousValue * current;
            break;
          case '÷':
            result = this.previousValue / current;
            break;
        }

        this.display = `${parseFloat(result.toFixed(8))}`;
        this.previousValue = null;
        this.operator = null;
      }
    },
    equals() {
      this.calculate();
      this.newNumber = true;
    }
  }
}
</script>

<style scoped>
.calculator-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #000000, #1a0f30);
  padding: 20px;
  position: relative;
  overflow: hidden;
}

/* 添加魔法星星效果 */
.calculator-container::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
    radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px);
  background-size: 50px 50px, 30px 30px;
  background-position: 0 0, 25px 25px;
  animation: twinkle 8s linear infinite;
}

.calculator {
  background: rgba(20, 12, 40, 0.9);
  border-radius: 20px;
  border: 2px solid #9b6dff;
  box-shadow: 0 0 20px #9b6dff,
              inset 0 0 20px rgba(155, 109, 255, 0.5);
  width: 100%;
  max-width: 400px;
  padding: 25px;
  position: relative;
  backdrop-filter: blur(5px);
}

.display {
  background: rgba(10, 6, 20, 0.9);
  color: #e4c6ff;
  padding: 20px;
  text-align: right;
  font-size: 2.5em;
  font-family: 'Cinzel', serif;
  border-radius: 10px;
  margin-bottom: 20px;
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  word-break: break-all;
  border: 1px solid #9b6dff;
  box-shadow: 0 0 10px rgba(155, 109, 255, 0.3),
              inset 0 0 10px rgba(155, 109, 255, 0.2);
  text-shadow: 0 0 5px #e4c6ff;
}

.buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.btn {
  background: rgba(73, 45, 120, 0.8);
  border: 1px solid #9b6dff;
  padding: 20px;
  font-size: 1.5em;
  color: #e4c6ff;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Cinzel', serif;
  text-shadow: 0 0 5px #e4c6ff;
  box-shadow: 0 0 10px rgba(155, 109, 255, 0.2);
}

.btn:hover {
  background: rgba(93, 55, 150, 0.9);
  transform: translateY(-2px);
  box-shadow: 0 0 15px #9b6dff;
  text-shadow: 0 0 10px #ffffff;
}

.btn:active {
  transform: translateY(0);
  box-shadow: 0 0 5px #9b6dff;
}

.operator {
  background: rgba(120, 45, 100, 0.8);
  border-color: #ff9be6;
  color: #ffd6f5;
}

.operator:hover {
  background: rgba(150, 55, 120, 0.9);
  box-shadow: 0 0 15px #ff9be6;
}

.zero {
  grid-column: span 2;
}

/* 添加動畫效果 */
@keyframes twinkle {
  0% { opacity: 0.5; }
  50% { opacity: 1; }
  100% { opacity: 0.5; }
}

@keyframes glow {
  0% { box-shadow: 0 0 5px #9b6dff; }
  50% { box-shadow: 0 0 20px #9b6dff; }
  100% { box-shadow: 0 0 5px #9b6dff; }
}

/* RWD 設計 */
@media (max-width: 480px) {
  .calculator {
    padding: 15px;
  }

  .display {
    font-size: 2em;
    padding: 15px;
    min-height: 60px;
  }

  .btn {
    padding: 15px;
    font-size: 1.2em;
  }
}

@media (max-width: 320px) {
  .display {
    font-size: 1.5em;
    padding: 10px;
    min-height: 50px;
  }

  .btn {
    padding: 10px;
    font-size: 1em;
  }
}
</style> 