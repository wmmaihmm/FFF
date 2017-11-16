a='''Hello I am     a short passage, I dont know myself at all Would you like to tell me     something about myself I would appreciate
any         information you could give me'''
a.split()
import collections
print(collections.Counter(a.split()))
