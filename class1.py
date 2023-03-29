class class1(object):
    """description of class"""
    # creating and viewing the html files in python
 
    import webbrowser
    import os
    # 1st method how to open html files in chrome using
    filename = 'file:///'+os.getcwd()+'/' + 'WebPage1.html'
    webbrowser.open_new_tab(filename)

