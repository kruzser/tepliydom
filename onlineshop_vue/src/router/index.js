import { createRouter, createWebHistory } from 'vue-router'
import store from "@/store";

import HomeView from '../views/HomeView.vue'
import Product from "@/views/Product.vue";
import CategoryView from "@/views/CategoryView.vue";
import Search from "@/views/Search.vue";
import CartView from "@/views/CartView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import AccountSettingView from "@/views/AccountSettingView.vue";
import Checkout from "@/views/Checkout.vue";
import Success from "@/views/Success.vue";


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: CategoryView
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUpView
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogInView
  },
  {
    path: '/account',
    name: 'AccountSettingView',
    component: AccountSettingView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
    next({name: 'LogIn', query: { to: to.path }});
  } else {
    next()
  }
})

export default router
