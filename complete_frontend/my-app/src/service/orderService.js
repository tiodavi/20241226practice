// orderService.js
// 訂單服務
const ORDER_KEY = 'orders';

export const orderService = {
    // 保存訂單
    saveOrder(order) {
        let orders = this.getOrders();
        orders.push(order);
        localStorage.setItem(ORDER_KEY, JSON.stringify(orders));
    },

    // 獲取所有訂單
    getOrders() {
        const orders = localStorage.getItem(ORDER_KEY);
        return orders ? JSON.parse(orders) : [];
    },

    // 清空所有訂單
    clearOrders() {
        localStorage.removeItem(ORDER_KEY);
    },

    // 更新特定訂單
    updateOrder(index, updatedOrder) {
        let orders = this.getOrders();
        orders[index] = updatedOrder;
        localStorage.setItem(ORDER_KEY, JSON.stringify(orders));
    }
};
