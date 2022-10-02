<template>
	<div class="MyForecast"> 
		<center>
			<div><br></div>
			<h1>Weather Vane</h1>
			<div><br></div>
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
						:key="item.date"
					>
						<td>{{ item.Location }}</td>
						<td>{{ item.Date }}</td>
						<td>{{ item.Temps }}</td>
						<td>{{ item.Forecast }}</td>
					</tr>
				</tbody>
			</v-table>
		</center>
	</div>
</template>

<script>
	import axios from 'axios';
	import moment from 'moment';

	export default {
		name: "MyForecast", 
		data() {
			return {
				forecast: [],
				address: '', 
				date: '', 
				datePassed: '',
			};
		},
		methods: {
			getForecast() {
				const path = 'http://localhost:5000/forecast?address=' + this.address + '&date=' + this.date + '&datePassed=' + this.datePassed;
				axios.get(path).then((res) => {
					this.forecast = res.data;
					console.log(this.forecast);
				}).catch((error) => {
					console.error(error);
				});
			},
		},
		created: function() {
			this.address = this.$route.params.address;
			this.date = moment(String(this.$route.params.date)).format('MM/DD/YYYY hh:mm:ss');
			this.datePassed = this.$route.params.datePassed;
			this.getForecast();
		}
	};
</script>


<style scoped>
	/deep/ .v-table{
		width: 1000px;
	}
</style>