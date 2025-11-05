import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import Sobre from '@/pages/Sobre.vue'
import Contato from '@/pages/Contato.vue'


const routes = [
  { 
    path: '/', 
    name: 'Home', 
    component: Home 

  },
  { 
    path: '/sobre', 
    name: 'Sobre', 
    component: Sobre 

  },
  { 
    path: '/contato',
    name: 'Contato', 
    component: Contato 
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
