# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:07:52 2014

@author: ZouLian
@Joint Lab for Medical Physics
@Oncology Department
@Sichuan People's Hospital
@Chengdu,Sichuan,China

"""

import datetime

from traits.api import HasTraits, Date, Time
from traitsui.api import View, Item, TimeEditor


class TimeEditorDemo(HasTraits):
    """ Demo class. """

    date = Date(datetime.datetime.today() )
    time1 = Time(datetime.datetime.now() )
    
    
    time = Time(datetime.time(12, 0, 0))
    view = View(Item('date'),
                Item('time1', label='Simple Editor'),
                Item('time1', label='Readonly Editor',
                     style='readonly',
                     # Show 24-hour mode instead of default 12 hour.
                     editor=TimeEditor(strftime='%H:%M:%S')
                     ),
                resizable=True)

    def _time_changed(self):
        """ Print each time the time value is changed in the editor. """
        print self.time
        print "HHAHDHD"

#-- Set Up The Demo ------------------------------------------------------------

demo = TimeEditorDemo()

if __name__ == "__main__":
    
      
        
        date = Date(datetime.datetime.today() )
        time = Time(datetime.datetime.now() )
       
        print time
        
        
        print patient_birth_date.year,patient_birth_date.month
        
        
        tim = datetime.datetime.now()
        
        print "Time:  ", tim
        
        date = tim.strftime("%Y%m%d")
        time = tim.strftime("%H%M%S")
        year = tim.year
        time_stamp_str =  tim.strftime("%Y%m%d.%H%M%S")
    
    
#    print demo.time 
#    
#    demo.configure_traits()