<template>
    <div class="MyForecast"> 
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
            <v-table>
                <thead>
                    <tr>
                        <th class="text-left">
                            Location
                        </th>
                        <th class="text-left">
                            Date
                        </th>
                        <th class="text-left">
                            Temps
                        </th>
                        <th class="text-left">
                            Forecast
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="item in forecast"
                        :key="item.Date"
                    >
                        <td>{{ item.Location }}</td>
                        <td>{{ item.Date }}</td>
                        <td>{{ item.Temps }}</td>
                        <td>{{ item.Forecast }}</td>
                    </tr>
                </tbody>
            </v-table>
			<div>
            <v-btn
              depressed
              color="secondary"
              @click='goHome'
            >
              Home
            </v-btn>
            </div>
        </center>
    </div>
</template>

<script>
    import axios from 'axios';
    import moment from 'moment';

    const client = axios.create({
        baseURL: (process.env.VUE_APP_API_URI == null) ? 'https://api.weathervaneapp.com' : process.env.VUE_APP_API_URI
    });

    export default {
        name: "MyForecast", 
        data() {
            return {
                forecast: [],
                address: '', 
                date: '', 
                datePassed: '',
                time: '',
                timePassed: ''
            };
        },
        methods: {
            getForecast() {
                const path = '/forecast?address=' + this.address + '&date=' + this.date + '&datePassed=' + this.datePassed;
                client.get(path).then((res) => {
                    this.forecast = res.data;
                    console.log(this.forecast);
                }).catch((error) => {
                    console.error(error);
                });
            },
			goHome() {
                this.$router.push({path: '/'});
            }
        },
        created: function() {
            this.address = this.$route.params.address;
            this.date = moment(String(this.$route.params.date)).format('MM/DD/YYYY');
            this.datePassed = this.$route.params.datePassed;
            this.time = moment(String(this.$route.params.time)).format('hh:mm:ss');
            this.timePassed = this.$route.params.timePassed;
            console.log(this.date);
            console.log(this.time);
            this.getForecast();
        }
    };
</script>


<style scoped>
    /deep/ .v-table{
        width: 1000px;
    }
</style>