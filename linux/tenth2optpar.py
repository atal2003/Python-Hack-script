#! /usr/bin/python3

from optparse import OptionParser
import time
from tenthoptpar import *

parser = OptionParser()
parser.add_option("-t", "--threshold",
        dest="threshold", type="int", 
        default=90, 
        help="Set threshold (%)")
parser.add_option("-s", "--single", 
        action="store_true",
        dest="singleshot",
        default=False, 
        help="just check once, don't loop")
parser.add_option("-m", "--mailbox",
        dest="mailbox",
        help="mail report to this mailbox")

(options, partition_list) = parser.parse_args()
print("singleshot is %r" % options.singleshot)
print("mailbx is %s" % options.mailbox)
print("threshold is %d" % options.threshold)
print("partition list is %s" % str(partition_list))

while True:
    check_once(options, partition_list)
    if options.singleshot:
        exit(0)
    time.sleep(1)
