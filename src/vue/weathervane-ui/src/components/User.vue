<template>
    <v-banner>
    <v-row align="left" justify="left" v-bind:style="{ height: deviceHeight * 0.6 + 'px',}"> 
      <v-col></v-col>
      <v-col>
        <v-img
          :src="require('../assets/weathervane.png')"
          class=""
          position=""
          contain
          height="60"
        />
      </v-col>
      <v-col>
        <v-btn prepend-icon="mdi-logout" color="primary" @click='logout'>
        Logout
        </v-btn>
      </v-col>
    </v-row>
    <center><h1>Weather Vane</h1></center>
  </v-banner>
    <div>
      <pre v-if="isAuthenticated">
        <v-container>
          <v-row align="end">
            <v-col align="end" cols="4">
              <h2>User Profile</h2>
            </v-col>
            <v-row>
              <v-col align="begin">
                <b>Nickname:</b>
                {{ user.nickname }}
                <b>Email:</b>
                {{ user.email }}
                <b>Last Updated:</b>
                {{ formatDatetime(user.updated_at) }}
              </v-col>
            </v-row>
          </v-row>
        </v-container>
      </pre>
    </div>
  </template>
  <script>
    import { useAuth0 } from '@auth0/auth0-vue';
    import moment from'moment';
  
    export default {
      name: "MyUser",
      setup() {
        const { loginWithRedirect, logout, user, isAuthenticated } = useAuth0();
        var baseURL = window.location.origin;
  
        return {
          login: () => {
            loginWithRedirect();
          },
          logout: () => {
            logout({ returnTo: baseURL + '/logout' });
          },
          user,
          isAuthenticated
        };
      },
      methods: {
        formatDatetime(datetime) {
            return this.date = moment(String(datetime)).format('MM/DD/YYYY hh:mm:ss');
        }
      }
    };
  </script>