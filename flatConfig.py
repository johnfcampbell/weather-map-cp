def getConfig(configText):
    import re
    configList = {}
    with open(configText, 'r') as f:

        for line in f:
            theKey, theValue = line.split('=')
            configList[theKey] = theValue.strip()

    return configList



