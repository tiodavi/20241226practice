<template>
    <div class="body">
      <h1 class="confirm-title">確認訂單</h1>
      <div class="order-grid">
        <div class="order-item" v-for="(drink, index) in drinks" :key="index">
          <h3>飲料 {{ index + 1 }}</h3>
          <ul>
            <li><strong>飲料名稱：</strong>{{ drink.name }}</li>
            <li><strong>糖度：</strong>{{ drink.sugar }}</li>
            <li><strong>冰量：</strong>{{ drink.ice }}</li>
            <li><strong>杯數：</strong>{{ drink.quantity }}</li>
          </ul>
          <button class="edit-button" @click="editDrink(index)">編輯</button>
        </div>
      </div>
      <div class="buttons">
        <button class="confirm-button" @click="submitOrder">送出訂單</button>
      </div>
    </div>
  </template>
  
  <script>
  import { orderService } from '@/service/orderService';
  export default {
    name: 'ConfirmOrder',
    data() {
      return {
        drinks: this.loadOrderData() || [], // 接收多筆飲料資料
        errorShown: false,  // 新增錯誤標記
        isSubmitting: false  // 新增提交狀態追蹤
      };
    },
    methods: {
      editDrink(index) {
        // 返回 OrderDetails，傳遞選中的飲料資料
        this.$router.push({
          name: 'DrinkDetailEditPage',
          query: {
            index, // 傳遞飲料索引
          },
        });
      },
      async submitOrder() {
        try {
          // 準備要發送的訂單數據
          const orderData = {
            orders: this.drinks.map((drink, index) => ({
              id: index + 1,
              name: drink.name,
              sugar: drink.sugar,
              ice: drink.ice,
              quantity: drink.quantity,
              orderTime: new Date().toISOString()
            }))
          };

          // 發送到後端
          const response = await fetch('http://localhost:5000/api/submit-order', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(orderData)
          });

          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }

          const result = await response.json();
          
          if (result.status === 'success') {
            // 清空當前訂單
            orderService.clearOrders();
            // 顯示成功訊息
            alert('訂單已成功送出！');
            // 返回首頁
            this.$router.push({ name: 'DrinksPage' });
          } else {
            console.error('訂單送出失敗:', result.message);
            alert('訂單送出失敗：' + result.message);
          }
        } catch (error) {
          console.error('送出訂單時發生錯誤:', error);
          alert('送出訂單時發生錯誤，請稍後再試');
        }
      },
      loadOrderData() {
        return orderService.getOrders();
      },
    },
  };
  </script>
  <style scoped>
  .body {
    margin: 0;
    font-family: 'Comic Sans MS', cursive, sans-serif; /* 手寫風格字體 */
    background: linear-gradient(135deg, #fff7da, #ffe8e8); /* 柔和漸層背景 */
    color: #4a4a4a; /* 溫暖的文字顏色 */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    min-height: 100vh;
    padding: 20px;
    box-sizing: border-box;
  }
  
  .confirm-title {
    font-size: 36px;
    color: #ff7675; /* 粉色標題文字 */
    margin-bottom: 20px;
    text-align: center;
    border-bottom: 2px dashed #fab1a0; /* 虛線分隔符 */
    padding-bottom: 10px;
  }
  
  .order-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    width: 100%;
    max-width: 1200px;
    margin-bottom: 20px;
  }
  
  .order-item {
    background: #fffaec; /* 柔和奶油背景 */
    border: 2px solid #fab1a0; /* 粉色邊框 */
    border-radius: 15px; /* 圓潤設計 */
    padding: 20px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* 柔和陰影 */
    transition: transform 0.2s ease, box-shadow 0.3s ease;
  }
  
  .order-item:hover {
    transform: scale(1.05); /* 懸停放大 */
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15); /* 懸停時陰影增強 */
  }
  
  .order-item h3 {
    margin-bottom: 10px;
    font-size: 20px;
    color: #ff7675; /* 粉色標題 */
  }
  
  .order-item ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .order-item li {
    margin-bottom: 5px;
    font-size: 16px;
  }
  
  .edit-button {
    background: linear-gradient(to right, #81ecec, #74b9ff); /* 飲料店風漸層按鈕 */
    color: #fff;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
  }
  
  .edit-button:hover {
    background: linear-gradient(to right, #74b9ff, #81ecec); /* 懸停時漸層變化 */
    transform: translateY(-2px); /* 懸停時輕微上移 */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* 提升按鈕層次 */
  }
  
  .buttons {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  
  .confirm-button {
    background: linear-gradient(to right, #fab1a0, #ff7675); /* 粉色漸層按鈕 */
    color: #fff;
    border: none;
    border-radius: 15px; /* 圓潤設計 */
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
  }
  
  .confirm-button:hover {
    background: linear-gradient(to right, #ff7675, #fab1a0); /* 懸停時漸層方向變化 */
    transform: translateY(-2px); /* 懸停時輕微上移 */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* 提升按鈕層次 */
  }
  </style>
  