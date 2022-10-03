<template>
	<div class="MySearch"> 
		<center>
			<div><br></div>
			<h1>Weather Vane</h1>
			<div><br></div>
			<span></span>
			<v-text-field clearable type="text" outlined label="Enter Address" id="addressInput" v-model="addressInput" v-on:input="getAutoSuggest" class="shrink" ></v-text-field>
			<v-card class="mx-auto" max-width="500" v-if="addresses.length" style="text-align: left;">
				<v-list v-for="address in addresses" :key="address" @click="selectAddress(address)">{{address}}</v-list>
			</v-card>
			<v-btn color="secondary" size="small" @click="addAddress()">Submit Address</v-btn>
			<div><br></div>
			<h4 v-if="tripLegs.length"><br>Trip Legs</h4>
			<p v-for="trip in tripLegs" :key="trip">{{trip}}</p>
			<div><br></div>
			<v-btn 
				v-if="tripLegs.length"
				color="secondary"
				size="small"
				@click='executeForecast'
			>Execute Forecast</v-btn>
			<div><br></div>
			<v-btn 
				v-if="tripLegs.length"
				color="secondary"
				size="small"
				@click='executeTravelcast'
			>Execute Travelcast</v-btn>
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
				tripLegs: [],
				selection: ['Forecast', 'Travelcast'],
				selected: '',
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
				this.tripLegs.push(this.addressInput);
				if(this.addressesString == '') {
					this.addressesString += this.addressInput;
				} else {
					this.addressesString += '|' + this.addressInput;
				}
				this.addressInput = null;
			},
			executeForecast(){
				this.$router.push("forecast/" + this.tripLegs[0] + '/' + new Date() + '/false')
			},
			executeTravelcast() {
				console.log(this.addressesString);
				this.$router.push("travelcast/" + this.addressesString + '/' + new Date() + '/false')
			}
		},
	};
</script>

<style scoped>
	/deep/ .v-text-field{
		width: 500px;
	}
</style>
