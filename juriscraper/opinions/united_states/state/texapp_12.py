# Scraper for Texas 2nd Court of Appeals
# CourtID: texapp2
# Court Short Name: TX
# Author: Andrei Chelaru
# Reviewer: mlr
# Date: 2014-07-10


from juriscraper.opinions.united_states.state import tex


class Site(tex.Site):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.court_id = self.__module__
        self.court_name = "capp_12"
        del self.parameters["ctl00$ContentPlaceHolder1$chkListCourts$0"]
        self.parameters["ctl00$ContentPlaceHolder1$chkListCourts$13"] = "on"
