/**
 * Main application entrypoint
 * 
 * 
 */
import 'vuetify/styles';
import '@mdi/font/css/materialdesignicons.css'
import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import App from './App.vue'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { createWebHistory, createRouter } from 'vue-router'
import Search from './components/Search.vue'
import Forecast from './components/Forecast.vue'
import Travelcast from './components/Travelcast.vue'
import Logout from './components/Logout.vue'
import User from './components/User.vue'
import { createAuth0, authGuard } from '@auth0/auth0-vue'

const routes = [
  {
    path: '/',
    name: 'Search', 
    component: Search,
    beforeEnter: authGuard
  },
  {
    path: '/forecast/:address/:date/:datePassed',
    name: 'Forecast',
    component: Forecast,
    beforeEnter: authGuard
  },
  {
    path: '/travelcast/:addresses/:date/:datePassed',
    name: 'Travelcast',
    component: Travelcast,
    beforeEnter: authGuard
  },
  {
    path: '/user',
    name: 'User',
    component: User,
    beforeEnter: authGuard
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
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
app.component('Datepicker', Datepicker);

app.use(
  createAuth0({
    domain: "dev-9hy7zhkb.us.auth0.com",
    client_id: "FrRBmDxaWxpZAPVJmG4sQ2jg9zia5WYI",
    redirect_uri: window.location.origin
    //audience: "https://weathervaneapp.com/api"
  })
);

app.mount('#app')
