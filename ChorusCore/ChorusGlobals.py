'''
Created on Jan 19, 2014

@author: Anduril
@target: Provide global variables
'''

def set_outputdir(path):
    '''Mark output folder as global'''
    global outputdir
    outputdir = path
    
def get_outputdir():
    '''Return output folder'''
    return outputdir
        
def set_parameters(configfile):
    '''Mark configfile as global'''
    global config
    config = configfile
    
def get_parameters():
    '''Return config file'''
    return config

def set_logserver(logserverobj):
    '''Mark logserver as global'''
    global logserver
    logserver=logserverobj
    
def get_logserver():
    '''Return logserver'''
    return logserver

def set_logger(loggerobj):
    '''Mark logger as global'''
    global logger
    logger=loggerobj
    
def get_logger():
    '''Return logger'''
    return logger

def set_configinfo(suite_info):
    '''Mark suiteinfo as global'''
    global suiteinfo
    suiteinfo = suite_info

def get_configinfo():
    '''Return suiteinfo in config file'''
    return suiteinfo

def set_suitedict(suite_dict):
    '''Mark suitedict as global'''
    global suitedict
    suitedict = suite_dict

def get_suitedict():
    '''Return suitedict generated from TestSuiteManagement'''
    return suitedict

def init_testresult():
    '''Mark testresult as global'''
    from ChorusConstants import ProjectResult
    global testresult
    testresult = ProjectResult()

def set_baseurl(url):
    '''Mark baseurl as global'''
    global baseurl
    baseurl = url

def get_baseurl():
    '''Return baseurl'''
    return baseurl
    
def get_testresult():
    '''Return testresult'''
    return testresult

def set_baselinepath(baseline_path):
    '''Mark baselinepath as global'''
    global baselinepath
    baselinepath = baseline_path

def get_baselinepath():
    '''Return global baselinepath'''
    return baselinepath

def set_knownissuelist(issue_dict):
    '''Mark known_issue_list as global'''
    global known_issue_list
    known_issue_list = issue_dict

def get_knownissuelist():
    '''Return known issue list'''
    return known_issue_list