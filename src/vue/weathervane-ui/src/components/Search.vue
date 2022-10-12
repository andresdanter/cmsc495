<!--
Search component which defines the content served via the main root (/) route

Weather Vane Application
Course: CMSC495
Group 1
-->

<template>
  <WVBanner />
  <div class="MySearch"> 
    <center>
      <div><br></div>
      <div><br></div>
      <v-text-field
          id="addressInput"
          v-model="addressInput"
          v-on:input="getAutoSuggest"
          clearable
          outlined
          label="Enter Location"
      ></v-text-field>
      <v-card class="mx-auto" max-width="500" v-if="addresses.length" style="text-align: left;">
        <v-list v-for="address in addresses" :key="address" @click="selectAddress(address)">{{address}}</v-list>
      </v-card>
      <v-btn color="secondary" size="small" @click="addAddress()">Add Location</v-btn>
      <v-dialog v-model="maxLocAlert">
        <v-card>
          <v-card-text class="text-center">
          Cannot enter more than 5 locations at this time.
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="maxLocAlert = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="dupAlert">
        <v-card>
          <v-card-text class="text-center">
          Location already entered.
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="dupAlert = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="emptyAlert">
        <v-card>
          <v-card-text class="text-center">
          Location entered may not be empty.
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="emptyAlert = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
      <v-row class="mx-2">
        <v-col align="end">
          <v-icon icon="mdi-calendar" />
        </v-col>
        <v-col>
          <Datepicker
            v-model="date"
            placeholder="Select Date"
            showNowButton nowButtonLabel="Now"
            hideInputIcon
            @update:modelValue="handleDate"
            :minDate= "new Date()"
            :maxDate="new Date(new Date().setDate(new Date().getDate() + 7))"
            :enableTimePicker="false"
          >
          </Datepicker>
        </v-col>
        <v-col></v-col>
      </v-row>
      <v-row class="mx-2">
        <v-col align="end">
          <v-icon icon="mdi-clock" />
        </v-col>
        <v-col>
          <Datepicker
            v-model="time"
            timePicker
            hideInputIcon
            modeHeight="120"
            placeholder="Select Time (Optional)"
          >
          </Datepicker>
        </v-col>
        <v-col></v-col>
      </v-row>
      <br>
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
    import  { useAuth0 }  from '@auth0/auth0-vue';
    import Datepicker from '@vuepic/vue-datepicker';
    import '@vuepic/vue-datepicker/dist/main.css'
    import WVBanner from './Banner.vue'

    const client = axios.create({
        baseURL: (process.env.VUE_APP_API_URI == null) ? 'https://api.weathervaneapp.com' : process.env.VUE_APP_API_URI
    });

    export default {
        name: "MySearch",
        components: {
          WVBanner,
          Datepicker
        },
        setup() {
            const { loginWithRedirect, user, isAuthenticated } = useAuth0();

            const alertFn = () => {
              alert('Menu closed');
            }

            return {
                login: () => {
                    loginWithRedirect();
                },
                user,
                isAuthenticated,
                alertFn
            };
        },
        data() {
            return {
                addresses: [],
                addressesString: '',
                selectedAddress: '',
                locations: [],
                options: ['Forecast', 'Travelcast'],
                selected: '',
                maxLocAlert: false,
                dupAlert: false,
                emptyAlert: false,
                datePassed: false,
                date: null,
                time: null
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
                if (this.addressInput == "" || this.addressInput == null) {
                    this.emptyAlert = true;
                    return;
                }
                if (this.locations.includes(this.addressInput)) {
                    this.dupAlert = true;
                    return;
                }
                if (this.locations.length < 5) {
                    this.locations.push(this.addressInput);
                    if(this.addressesString == '') {
                        this.addressesString += this.addressInput;
                    } else {
                        this.addressesString += '|' + this.addressInput;
                    }
                    this.addressInput = null;
                } else {
                    this.maxLocAlert =  true;
                }
            },
            executeForecast(){
                var date = this.getDate();
                console.log(this.datePassed);
                if (this.datePassed) {
                  this.$router.push("forecast/" + this.addressesString + '/' + date + '/true');
                } else {
                  this.$router.push("forecast/" + this.addressesString + '/' + date + '/false');
                }
            },
            executeTravelcast() {
                var date = this.getDate();
                console.log(this.datePassed);
                if(this.datePassed) {
                  this.$router.push("travelcast/" + this.addressesString + '/' + date + '/true');
                } else {
                  this.$router.push("travelcast/" + this.addressesString + '/' + date + '/false');
                }
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
                        alert("No option selected");
                }
            },
            removeLocation(index) {
                this.locations.splice(index, 1);
            },
            
            handleDate() {
                this.datePassed = true;
            },
            getDate() {
                var date = null;
                if (this.time != null) {
                  date = new Date(this.date.getFullYear(),
                                  this.date.getMonth(),
                                  this.date.getDate(),
                                  this.time.hours,
                                  this.time.minutes,
                                  this.time.seconds);
                } else {
                  date = this.date;
                }
                return date;
            },
            checkDateNotNull() {
              if (this.date == null) {
                alert("Please enter/select date before proceeding");
                return false;
              }
              return true;
            }

        },
    };
</script>

<style scoped>
    /deep/ .v-text-field {
        width: 500px;
    }
</style>
