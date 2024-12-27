<template>
    <div class="test-container">
        <h2>API 測試頁面</h2>
        
        <!-- 測試表單 -->
        <div class="form-group">
            <label>名稱：</label>
            <input type="text" v-model="formData.name" placeholder="請輸入名稱">
        </div>
        
        <div class="form-group">
            <label>數值：</label>
            <input type="text" v-model="formData.key" placeholder="請輸入數值">
        </div>

        <button @click="sendData" :disabled="isLoading">
            {{ isLoading ? '傳送中...' : '傳送資料' }}
        </button>

        <!-- 顯示回應結果 -->
        <div class="response-area" v-if="response">
            <h3>回應結果：</h3>
            <pre>{{ response }}</pre>
        </div>

        <!-- 添加清除按鈕 -->
        <button class="clear-button" @click="clearForm" :disabled="isLoading">
            清除表單
        </button>

        <!-- 添加驗證提示 -->
        <div class="error-message" v-if="validationError">
            {{ validationError }}
        </div>
    </div>
</template>

<script>
export default {
    name: 'TestComponent',
    data() {
        return {
            formData: {
                key: '',
                name: ''
            },
            isLoading: false,
            response: null,
            validationError: '' // 新增驗證錯誤訊息
        }
    },
    methods: {
        validateForm() {
            if (!this.formData.name.trim()) {
                this.validationError = '請輸入名稱';
                return false;
            }
            if (!this.formData.key.trim()) {
                this.validationError = '請輸入數值';
                return false;
            }
            this.validationError = '';
            return true;
        },

        clearForm() {
            this.formData.key = '';
            this.formData.name = '';
            this.response = null;
            this.validationError = '';
        },

        async sendData() {
            if (!this.validateForm()) {
                return;
            }

            try {
                this.isLoading = true;
                console.log('正在發送數據:', this.formData); // 除錯用

                const response = await fetch('http://localhost:5000/api/receive-data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.formData)
                });

                console.log('收到回應:', response); // 除錯用

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                this.response = data;
                alert('資料傳送成功！');
                
            } catch (error) {
                console.error('錯誤:', error);
                this.response = {
                    status: 'error',
                    message: error.message || '發送請求時發生錯誤'
                };
            } finally {
                this.isLoading = false;
            }
        }
    }
}
</script>

<style scoped>
.test-container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 10px;
}

button {
    background: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

button:hover:not(:disabled) {
    background: #45a049;
}

.response-area {
    margin-top: 20px;
    padding: 15px;
    background: #f5f5f5;
    border-radius: 4px;
}

pre {
    white-space: pre-wrap;
    word-wrap: break-word;
}

.clear-button {
    background: #ff4444;
    margin-left: 10px;
}

.clear-button:hover:not(:disabled) {
    background: #cc0000;
}

.error-message {
    color: #ff0000;
    margin-top: 10px;
    font-size: 14px;
}
</style> 