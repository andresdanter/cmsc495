<template>
    <v-banner>
        <v-row align="left" justify="left" v-bind:style="{ height: deviceHeight * 0.6 + 'px',}"> 
            <v-col>
                <v-img
                :src="require('../assets/weathervane.png')"
                class=""
                position=""
                contain
                height="60"
                />
            </v-col>
        </v-row>
        <center>
            <h1>Weather Vane</h1>
        </center>
    </v-banner>
    <center>
    <div>
        <br/>
        <h2>Welcome</h2>
        <br/>
        <br/>
        <v-btn
            depressed
            color="secondary"
            @click='login'
        >
            Log In 
        </v-btn>
    </div>
    </center>
</template>
<script>
  import { useAuth0 } from '@auth0/auth0-vue';

  export default {
    name: "MyLogin",
    setup() {
      const { loginWithRedirect } = useAuth0();

      return {
        login: () => {
          loginWithRedirect();
        }
      };
    }
  };
</script>