import pyhtml
import Home
import Vaccination_summary
#import student_a_level_3
import Flowchart
import improvement
import student_b_level_2
import student_b_level_3
#In the studio project, the other team members would have their pages imported like this.
# import student_b_level_1
# import student_b_level_2
# import student_b_level_3

# import student_c_level_1
# import student_c_level_2
# import student_c_level_3

pyhtml.need_debugging_help=True

#All pages that you want on the site need to be added as below
pyhtml.MyRequestHandler.pages["/"]=Home; #Page to show when someone accesses "http://localhost/"
pyhtml.MyRequestHandler.pages["/page2"]=Vaccination_summary; #Page to show when someone accesses "http://localhost/page2"
pyhtml.MyRequestHandler.pages["/page3"]=improvement; #Page to show when someone accesses "http://localhost/page3"
pyhtml.MyRequestHandler.pages["/page4"]=Flowchart; #Page to show when someone accesses "http://localhost/page4"
pyhtml.MyRequestHandler.pages["/page5"]=student_b_level_2; #Page to show when someone accesses "http://localhost/page5"
pyhtml.MyRequestHandler.pages["/page6"]=student_b_level_3; #Page to show when someone accesses "http://localhost/page6"
#Host the site!
pyhtml.host_site()
