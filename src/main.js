import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import Home from './views/Home.vue'
import 'primeicons/primeicons.css'
import './assets/main.css'



const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
  ]
})

const app = createApp(App)
app.use(PrimeVue)
app.use(router)
app.mount('#app')
