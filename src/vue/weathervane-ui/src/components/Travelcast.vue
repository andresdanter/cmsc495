<template>
    <div class="MyTravelcast"> 
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
                            Leg
                        </th>
                        <th class="text-left">
                            Date
                        </th>
                        <th class="text-left">
                            Time
                        </th>
                        <th class="text-left">
                            Temp
                        </th>
                        <th class="text-left">
                            Forecast
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="item in travelcast"
                        :key="item.Date"
                    >
                        <td>{{ item.Leg }}</td>
                        <td>{{ item.Date }}</td>
                        <td>{{ item.Time }}</td>
                        <td>{{ item.Temp }}</td>
                        <td>{{ item.Forecast }}</td>
                    </tr>
                </tbody>
            </v-table>
        </center>
    </div>
</template>

<script>
    import axios from 'axios';
    import moment from'moment';

    export default {
        name: "MyTravelcast", 
        data() {
            return {
                travelcast: [],
                addresses: '', 
                date: '', 
                datePassed: '',
            };
        },
        methods: {
            getTravelcast() {
                const uri = (process.env.VUE_APP_API_URI == null) ? 'https://api.weathervaneapp.com' : process.env.VUE_APP_API_URI
                const path = uri + '/travelcast?addresses=' + this.addresses + '&date=' + this.date + '&datePassed=' + this.datePassed;
                axios.get(path).then((res) => {
                    this.travelcast = res.data;
                    console.log(this.travelcast);
                }).catch((error) => {
                    console.error(error);
                });
            },
        },
        created: function() {
            this.addresses = this.$route.params.addresses;
            this.date = moment(String(this.$route.params.date)).format('MM/DD/YYYY hh:mm:ss');
            this.datePassed = this.$route.params.datePassed;
            this.getTravelcast();
        }
    };
</script>


<style scoped>
    /deep/ .v-table{
        width: 1000px;
    }
</style>