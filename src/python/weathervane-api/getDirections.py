#!/usr/bin/env python3

"""
getDirections.py -
Module that encapsulates interactions with Google Maps API

Weather Vane Application
Course: CMSC495
Group 1
"""

import os
import googlemaps
import datetime
import geopy.distance


def get_autocomplete(address):
        """
        Return a dictionary that contains necessary information about the trip to
        display to the user. In addition, we compute an array of values of longitudes
        and latitudes (and the appropriate times the user is passing through them) in
        order to eventually query OpenWeatherAPI and forcast
        """
        gmaps = googlemaps.Client(key=os.getenv('GMAPS_API_KEY'))
        places = googlemaps.places.places_autocomplete(gmaps, input_text=address)
        results = []
        for i in places:
            results.append(i['description'])
        
        return results

def get_directions(locs, time):
        """
        """
        gmaps = googlemaps.Client(key=os.getenv('GMAPS_API_KEY'))

        # End returned dictionary
        results_dict = {}
        results_dict['results'] = []
        
        for x in range(len(locs)):
            if x == len(locs) - 1:
                    break
            
            directions_result = gmaps.directions(locs[x], locs[x+1], mode = 'driving', departure_time = time)
            directions_data = directions_result[0]['legs'][0]
            
            # Acquire travel directions from Google Maps API
            direction_steps = directions_data['steps']
            results = []
            updated_results = []

            # Store the steps in array form in an array 'results'
            for i in direction_steps:
                step_duration = i['duration']['text']
                step_duration = step_duration.split(' ')
                if len(step_duration) == 2:
                    step_duration = [0, int(step_duration[0])]
                else:
                    step_duration = [int(step_duration[0]), int(step_duration[2])]
                        
                time_change = datetime.timedelta(hours=step_duration[0], minutes=step_duration[1])
                time += time_change
                        
                results.append([time, i['end_location']['lat'], i['end_location']['lng']])
                
                # Some drives may be without a change in direction for several hours.
                # This part below splits up these longer sections into approx 1 hour long intervals
                # and the estimated long and lat of the driver along the path. This will allow us to
                # query the OpenWeatherAPI and forcast every hour of the drive (if possible).
        
                for i in range(len(results)):
                    updated_results.append(results[i])
                    if i != len(results) - 1:
                        time_diff = results[i+1][0] - results[i][0]
                        time_diff = time_diff.total_seconds() / 60
                        temp_lat = results[i][1]
                        temp_lng = results[i][2]
                        temp_time = results[i][0]
                        if time_diff > 60:
                            split = int(time_diff / 60) + 1
                            time_jump = datetime.timedelta(minutes = int(time_diff / split))
                            lat_jump = (results[i+1][1] - results[i][1]) / split
                            lng_jump = (results[i+1][2] - results[i][2]) / split
                            for j in range(0, split-1):
                                temp_time += time_jump
                                temp_lat += lat_jump
                                temp_lng += lng_jump
                                updated_results.append([temp_time, temp_lat, temp_lng])
                
                temp_results = updated_results
                updated_results = []
                
                temp_lat_lng = (temp_results[0][1], temp_results[0][2])
                updated_results.append(temp_results[0])
                for i in temp_results:
                        if geopy.distance.geodesic(temp_lat_lng, (i[1], i[2])).mi > 25:
                                updated_results.append(i)
                                temp_lat_lng = (i[1], i[2])
                
                results_dict['results'] += updated_results

        return results_dict
