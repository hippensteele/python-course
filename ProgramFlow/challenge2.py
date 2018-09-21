
ip = input("Please enter an IP address: ")
segmentCount = 0
lengthCount = 0
inSegment = False
for i in range(0,len(ip)):
    if ip[i] == '.':
        if not i==0:
            if lengthCount > 0:
                print("Segment length: {}".format(lengthCount))
            inSegment = False
            lengthCount = 0
    else:
        if not inSegment:
            segmentCount += 1
            inSegment = True
        lengthCount += 1
if lengthCount > 0:
    print("Segment length: {}".format(lengthCount))
print("Total segments: {}".format(segmentCount))

        