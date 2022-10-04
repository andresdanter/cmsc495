import 'vuetify/styles' // Global CSS has to be imported
import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import App from './App.vue'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { createWebHistory, createRouter, createWebHashHistory } from "vue-router";
import Search from './components/Search.vue'
import Forecast from './components/Forecast.vue'
import Travelcast from './components/Travelcast.vue'
import { createAuth0, authGuard } from '@auth0/auth0-vue';

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
  }
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

app.use(
  createAuth0({
    domain: "dev-9hy7zhkb.us.auth0.com",
    client_id: "FrRBmDxaWxpZAPVJmG4sQ2jg9zia5WYI",
    redirect_uri: window.location.origin,
    audience: "https://weathervaneapp.com/api"
  })
);

app.mount('#app')
