import 'vuetify/styles' // Global CSS has to be imported
import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import App from './App.vue'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { createWebHistory, createRouter } from "vue-router";
import Search from './components/Search.vue'
import Forecast from './components/Forecast.vue'
import Travelcast from './components/Travelcast.vue'

const routes = [
  {
    path: '/',
    name: 'Home', 
    component: Search,
  },
  {
    path: '/forecast/:address/:date/:datePassed',
    name: 'Forecast',
    component: Forecast
  },
  {
    path: '/travelcast/:addresses/:date/:datePassed',
    name: 'Travelcast',
    component: Travelcast
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)
app.use(vuetify)
app.use(router)
app.mount('#app')