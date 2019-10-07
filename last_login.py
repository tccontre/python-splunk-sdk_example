__author__ = "tccontre"
"""
description:
    this script is a simple splunk search query using the splunk python SDK for automating mass query and day to day task
"""
import sys
import xml.etree.ElementTree as ET
import splunklib.results as results
import splunklib.client as client


class QuickSearch:
    def __init__(self):
        self.service = self.check_connection()
        self.query_results = self.splunk_search(self.service)
        self.out_raw_list = self.parse_xml(self.query_results)
        self.display_output(self.out_raw_list)
        return
                        

    def check_connection(self):
        """
        # initialize your splunk service connection with your password and username
        """
        try:
            service = client.connect(username="admin",
                                 password="yourpassword",
                                 host = "localhost", # change this to ip address of machine where the splunk monitoring instance is located (remote splunk instance)
                                 port = 8089
                                     )
        except:
            print("[+] splunk login authentication failure encounter\n\n")
        return service

    def splunk_search(self, service):
        """
        # initialized the one shot splunk search
        """
        search_query = 'search source="wineventlog:security" EventCode IN (4625,4624) | table _time Account_Name Keywords Source_Network_Address'
        kwargs_oneshot = {"earliest_time": "-7d","latest_time": "now"}
        query_results = service.jobs.oneshot(search_query, **kwargs_oneshot)
        return query_results

    
    def parse_xml(self, res):
        """
        # parse the XML raw output of the splunk query to one liner output
        """
        out_raw_list =[]
        tree = ET.parse(res)
        root = tree.getroot()
        
        for node in root.iter('field'):    
            # the field name of splunk need to parse
            #print(node.attrib)
            holder = ""
            children = node.getchildren()
            for c in children:
                for i in c.iter('text'):
                    if len(children) >1:
                        holder = holder + i.text
                    else:
                        holder = i.text
            out_raw_list.append(holder)
        return out_raw_list

    def display_output(self, raw_list):
        for i in range (0,len(raw_list),4):
            if raw_list[i] != None or raw_list[i] != "":
                print("timestamp: {0} user: {1} status: {2} src: {3}".format(raw_list[i],raw_list[i+1],raw_list[i+2],raw_list[i+3],))
            else:
                continue
        return



def main():
    qs = QuickSearch()
    return

if __name__ == "__main__":
    main()





