'''
Title: Bus Buddy

Description: A little app that pulls RTD data and so always knows your bus arrival time

Author: Ryan Wright
'''
from google.transit import gtfs_realtime_pb2
import requests
from mylogins import *
import time

class Tripsdata:
    def __init__(self):
         self.count = 0
         self.datastore = self.pull
    def pull(self):
        '''Pull rtd-denver GTFS data and the assign bindings using gtfs_realtime_pb2'''
        while True:
            tufeed = gtfs_realtime_pb2.FeedMessage()
            response = requests.get('http://www.rtd-denver.com/google_sync/TripUpdate.pb', auth=(username, passwords))
            #Use response.content to load the binary into the feed object using gtfs_realtime_pb2 here.
            tufeed.ParseFromString(response.content)
            # print "tufeed loaded"

            # make sure we loaded data from denver RTD API
            if tufeed == False:
                # print "nothing loaded from Denver RTD retrying in 10 seconds"
                time.sleep(10)


            else:
                print "Feed is loaded now"
                self.count += 1
                # print self.count
                return tufeed
                # print "Pulled the feed %s time and stored in data.datastore" %count
                # time.sleep(60)
                # time.sleep(60)
                # pass
data = Tripsdata()


class Feedstore:
    def get_packaged_data(self, tufeed):
        '''Parse through RTD data and start loading it into database'''
        model.newtable()

        for entity in tufeed.entity:
            for mystop in entity.trip_update.stop_time_update:

                print entity.trip_update.trip.route_id
                bus = entity.trip_update.trip.route_id

                print mystop.stop_id
                stop = mystop.stop_id

                print mystop.arrival
                times = mystop.arrival

        return self.times
feed = Feedstore()

if __name__ == '__main__':
    ourdata = data.pull()
    db_data = feed.get_packaged_data(ourdata)
