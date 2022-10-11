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
        <v-btn icon @click='routeToUser'>
          <v-avatar icon color="black">
            <v-icon dark>
              mdi-account-circle
            </v-icon>
          </v-avatar>
        </v-btn>
      </v-col>
    </v-row>
    <center><h1>Weather Vane</h1></center>
  </v-banner>
</template>

<script>
    export default {
        name: "MyBanner",
        methods: {
            routeToUser() {
                this.$router.push({path: '/user'});
            }
        }
    };
</script>