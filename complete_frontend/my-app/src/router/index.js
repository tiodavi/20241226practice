import { createRouter, createWebHistory } from "vue-router";
import Login from "@/components/Login.vue";
import MainPage from "@/components/MainPage.vue";
import DrinksPage from "@/components/DrinksPage.vue";
import DrinkDetailPage from "@/components/DrinkDetailPage.vue";
import DrinkDetailEditPage from "@/components/DrinkDetailEditPage.vue";
import ConfirmOrderPage from "@/components/ConfirmOrderPage.vue";
import Test from '@/components/Test.vue'
import CalculatorPage from '@/components/CalculatorPage.vue'


const routes = [
    {
        path: "/",
        name: "Login",
        component: Login,
    },
    {
        path: "/main-page",
        name: "MainPage",
        component: MainPage,
    },
    {
        path: "/drinks-page",
        name: "DrinksPage",
        component: DrinksPage,
    },
    {
        path: "/drink-detail",
        name: "DrinkDetailPage",
        component: DrinkDetailPage,
    },
    {
        path: "/drink-detail-edit",
        name: "DrinkDetailEditPage",
        component: DrinkDetailEditPage,
    },
    {
        path: "/comfirm-order",
        name: "ConfirmOrder",
        component: ConfirmOrderPage,
    },
    {
        path: '/test',
        name: 'Test',
        component: Test
    },
    {
        path: '/calculator',
        name: 'CalculatorPage',
        component: CalculatorPage
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;