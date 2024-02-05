import numpy as np
load_dict=np.load('hospi.npy',allow_pickle=True).item()
for key in load_dict.keys():
    load_dict[key]=sorted(load_dict[key].items(),key=lambda x:x[1],reverse=True)
pass