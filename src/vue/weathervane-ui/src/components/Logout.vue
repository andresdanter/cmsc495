<template>
    <div class="MyLogout"> 
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
        <center><h1>Weather Vane</h1></center>
    </v-banner>
        <center>
            <br/>
            <h2>You have been logged out</h2>
            <br/>
            <br/>
            <div>
            <v-btn
              depressed
              color="secondary"
              @click='goHome'
            >
              Go Back to Weather Vane
            </v-btn>
            </div>
        </center>
    </div>
</template>

<script>
    export default {
        name: "MyLogout", 
        methods: {
            goHome() {
                this.$router.push({path: '/'});
            }
        }
    };
</script>


<style scoped>
    /deep/ .v-table{
        width: 1000px;
    }
</style>