<template>
    <div class="MyLogout"> 
        <WVBanner />
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
    import WVBanner from './Banner.vue'

    export default {
        name: "MyLogout", 
        components: {
          WVBanner
        },
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