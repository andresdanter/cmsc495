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
      <center><h1>Weather Vane</h1></center>
    </v-banner>
    <div class="MySearch"> 
        <center>
            <div><br></div>
            <div><br></div>
            <span></span>
            <v-text-field clearable type="text" outlined label="Enter Address" id="addressInput" v-model="addressInput" v-on:input="getAutoSuggest" class="shrink" ></v-text-field>
            <v-card class="mx-auto" max-width="500" v-if="addresses.length" style="text-align: left;">
                <v-list v-for="address in addresses" :key="address" @click="selectAddress(address)">{{address}}</v-list>
            </v-card>
            <v-btn color="secondary" size="small" @click="addAddress()">Add Address</v-btn>
            <div><br></div>
            <div>
                <h4 v-if="locations.length"><br>Locations</h4>
                <ul>
                    <li v-for="(loc, index) in locations" :key="index">
                        <span>{{ loc }}</span>
                        <v-btn class="mx-2" color="black"
                               icon="mdi-delete"
                               size="x-small" @click="removeLocation(index)"
                        ></v-btn>
                    </li>
                </ul>
            </div>
            <br>
            <v-select
              :items="options"
              label="Select Option"
              outlined
              v-model="selected"
            ></v-select>
            <v-btn
              depressed
              color="secondary"
              @click='executeOption'
            >
              Submit
            </v-btn>
        </center>
    </div>
</template>

<script>
    import axios from 'axios';

    const client = axios.create({
        baseURL: (process.env.VUE_APP_API_URI == null) ? 'https://api.weathervaneapp.com' : process.env.VUE_APP_API_URI
    });

    export default {
        name: "MySearch", 
        data() {
            return {
                addresses: [],
                addressesString: '',
                selectedAddress: '',
                locations: [],
                options: ['Forecast', 'Travelcast'],
                selected: '',
                alert: false,
            };
        },
        methods: {
            getAutoSuggest() {
                const path = '/addressSuggestions?address=' + this.addressInput;
                client.get(path).then((res) => {
                    this.addresses = res.data;
                }).catch((error) => {
                    console.error(error);
                });
            },
            selectAddress(addy) {
                this.addressInput = addy;
                this.addresses = []
            },
            addAddress() {
                if (this.locations.length < 5) {
                    this.locations.push(this.addressInput);
                    if(this.addressesString == '') {
                        this.addressesString += this.addressInput;
                    } else {
                        this.addressesString += '|' + this.addressInput;
                    }
                    this.addressInput = null;
                } else {
                    this.alert =  true;
                }
            },
            executeForecast(){
                this.$router.push("forecast/" + this.addressesString + '/' + new Date() + '/false')
            },
            executeTravelcast() {
                console.log(this.addressesString);
                this.$router.push("travelcast/" + this.addressesString + '/' + new Date() + '/false')
            },
            executeOption() {
                switch(this.selected) {
                    case 'Forecast':
                        this.executeForecast();
                        break;
                    case 'Travelcast':
                        this.executeTravelcast();
                        break;
                    default:
                        console.log("No option selected");
                }
            },
            removeLocation(index) {
                this.locations.splice(index, 1);
            }
        },
    };
</script>

<style scoped>
    /deep/ .v-text-field{
        width: 500px;
    }
</style>
