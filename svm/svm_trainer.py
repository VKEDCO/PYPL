## author: vladimir kulyukin
import argparse
import os, os.path
import ntpath

from sklearn import svm, metrics

def get_path_leaf(fp):
    head, tail = npath.split(fp)
    return tail or npath.basename(head)

def read_numbers_from_file(fp):
    with open(fp) as infile:
        numbers = []
        for line in infile:
            numbers.extend([float(x) for x in line.split()])
        return numbers

def process_data_dir(dir_path, target):
    samples = []
    file_paths = []
    d = {}
    for num_fp in [os.path.join(dir_path, fp) for fp in os.listdir(dir_path)
                   if os.path.isfile(os.path.join(dir_path, fp)) and fp.endswith('.txt')]:
        #print 'Processing: ', num_fp
        data = read_numbers_from_file(num_fp)
        #print len(data)
        samples.append(data)
        file_paths.append(num_fp)
        d[num_fp] = data
    #print 'number of samples in ', dir_path + ' == ', len(samples)
    return file_paths, samples, [target for i in xrange(len(samples))], d

## ==================== TRAIN DATA ============================



grass_train_dir = ''
hive_train_dir  = ''
pad_train_dir   = ''

grass_train_data = process_data_dir(grass_train_dir, 0)
hive_train_data  = process_data_dir(hive_train_dir,  1)
pad_train_data   = process_data_dir(pad_train_dir,   2)

grass_train_fpaths = grass_train_data[0]
hive_train_fpaths  = hive_train_data[0]
pad_train_fpaths   = pad_train_data[0]

grass_train_samples = grass_train_data[1]
hive_train_samples  = hive_train_data[1]
pad_train_samples   = pad_train_data[1]

grass_train_targets = grass_train_data[2]
hive_train_targets  = hive_train_data[2]
pad_train_targets   = pad_train_data[2]

#grass_train_dict    = grass_train_data[3]
#hive_train_dict     = hive_train_data[3]
#pad_train_dict      = pad_train_data[3]

train_samples = grass_train_samples + hive_train_samples + pad_train_samples
train_targets = grass_train_targets + hive_train_targets + pad_train_targets
##train_fpaths  = grass_train_fpaths  + hive_train_fpaths  + pad_train_fpaths

### ========= END OF TRAINING =====================

#print 'Testing'

grass_test_dir = ''
hive_test_dir  = ''
pad_test_dir   = ''

grass_test_data = process_data_dir(grass_test_dir, 0)
hive_test_data  = process_data_dir(hive_test_dir,  1)
pad_test_data   = process_data_dir(pad_test_dir,   2)

grass_test_fpaths = grass_test_data[0]
hive_test_fpaths  = hive_test_data[0]
pad_test_fpaths   = pad_test_data[0]

grass_test_samples = grass_test_data[1]
hive_test_samples  = hive_test_data[1]
pad_test_samples   = pad_test_data[1]

grass_test_targets = grass_test_data[2]
hive_test_targets  = hive_test_data[2]
pad_test_targets   = pad_test_data[2]

grass_test_dict    = grass_test_data[3]
hive_test_dict     = hive_test_data[3]
pad_test_dict      = pad_test_data[3]

#print len(grass_test_targets)

test_samples = grass_test_samples + hive_test_samples + pad_test_samples
test_targets = grass_test_targets + hive_test_targets + pad_test_targets
##test_fpaths  = grass_test_fpaths  + hive_test_fpaths  + pad_test_fpaths

## ============ END OF TESTING ========================

##clf = svm.SVC()
##clf.fit(train_samples, train_targets)

lin_svc = svm.LinearSVC()
lin_svc.fit(train_samples, train_targets)

cs_lin_svc = svm.LinearSVC(multi_class='crammer_singer')
cs_lin_svc.fit(train_samples, train_targets)

ovr_lin_svc = svm.LinearSVC(multi_class='ovr')
ovr_lin_svc.fit(train_samples, train_targets)

nu_lin_svc  = svm.NuSVC(nu=0.1)
nu_lin_svc.fit(train_samples, train_targets)

nu_lin_svc_2  = svm.NuSVC(nu=0.2)
nu_lin_svc_2.fit(train_samples, train_targets)

nu_lin_svc_3  = svm.NuSVC(nu=0.1, probability=True)
nu_lin_svc_3.fit(train_samples, train_targets)

##predicted_targets         = clf.predict(test_samples)
lin_predicted_targets       = lin_svc.predict(test_samples)
cs_lin_predicted_targets    = cs_lin_svc.predict(test_samples)
ovr_lin_predicted_targets   = ovr_lin_svc.predict(test_samples)
nu_lin_predicted_targets    = nu_lin_svc.predict(test_samples)
nu_lin_predicted_targets_2  = nu_lin_svc_2.predict(test_samples)
nu_lin_predicted_targets_3  = nu_lin_svc_3.predict(test_samples)
#nu_lin_predicted_targets_4  = nu_lin_svc_3.predict_log_proba(test_samples)

##grass_predicted_targets = predicted_targets[0:len(grass_test_targets)]
##hive_predicted_targets  = predicted_targets[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
##pad_predicted_targets   = predicted_targets[len(grass_test_targets)+len(hive_test_targets):]

grass_lin_predicted_targets = lin_predicted_targets[0:len(grass_test_targets)]
hive_lin_predicted_targets  = lin_predicted_targets[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_lin_predicted_targets   = lin_predicted_targets[len(grass_test_targets)+len(hive_test_targets):]

grass_cs_lin_predicted_targets = cs_lin_predicted_targets[0:len(grass_test_targets)]
hive_cs_lin_predicted_targets  = cs_lin_predicted_targets[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_cs_lin_predicted_targets   = cs_lin_predicted_targets[len(grass_test_targets)+len(hive_test_targets):]

grass_ovr_lin_predicted_targets = ovr_lin_predicted_targets[0:len(grass_test_targets)]
hive_ovr_lin_predicted_targets  = ovr_lin_predicted_targets[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_ovr_lin_predicted_targets   = ovr_lin_predicted_targets[len(grass_test_targets)+len(hive_test_targets):]

grass_nu_lin_predicted_targets = nu_lin_predicted_targets[0:len(grass_test_targets)]
hive_nu_lin_predicted_targets  = nu_lin_predicted_targets[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_nu_lin_predicted_targets   = nu_lin_predicted_targets[len(grass_test_targets)+len(hive_test_targets):]

grass_nu_lin_predicted_targets_2 = nu_lin_predicted_targets_2[0:len(grass_test_targets)]
hive_nu_lin_predicted_targets_2  = nu_lin_predicted_targets_2[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_nu_lin_predicted_targets_2   = nu_lin_predicted_targets_2[len(grass_test_targets)+len(hive_test_targets):]

grass_nu_lin_predicted_targets_2 = nu_lin_predicted_targets_2[0:len(grass_test_targets)]
hive_nu_lin_predicted_targets_2  = nu_lin_predicted_targets_2[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_nu_lin_predicted_targets_2   = nu_lin_predicted_targets_2[len(grass_test_targets)+len(hive_test_targets):]

grass_nu_lin_predicted_targets_3 = nu_lin_predicted_targets_3[0:len(grass_test_targets)]
hive_nu_lin_predicted_targets_3  = nu_lin_predicted_targets_3[len(grass_test_targets):len(grass_test_targets)+len(hive_test_targets)]
pad_nu_lin_predicted_targets_3   = nu_lin_predicted_targets_3[len(grass_test_targets)+len(hive_test_targets):]

def display_targets(target_file_paths, real_targets, predicted_targets):
    for target_fp, real_target, pred_target in zip(target_file_paths, real_targets, predicted_targets):
        print 'Target file:' + target_fp
        print 'Real target:' + str(real_target)
        print 'Pred target:' + str(pred_target)
        print

def display_target_misses(target_file_paths, real_targets, predicted_targets):
    for target_fp, real_target, pred_target in zip(target_file_paths, real_targets, predicted_targets):
        if real_target != pred_target:
            print 'Target file:' + target_fp
            print 'Real target:' + str(real_target)
            print 'Pred target:' + str(pred_target)
            if target_fp in grass_test_dict:
                print nu_lin_svc_3.predict_proba([grass_test_dict[target_fp]])
            elif target_fp in hive_test_dict:
                print nu_lin_svc_3.predict_proba([hive_test_dict[target_fp]])
            elif target_fp in pad_test_dict:
                print nu_lin_svc_3.predict([pad_test_dict[target_fp]])
            else:
                print 'No dict'
            print

def display_texture_stats(texture_name, model_name, real_targets, predicted_targets):
    hit, miss = 0, 0
    for rt, pt in zip(real_targets, predicted_targets):
        if rt == pt:
            hit = hit + 1
        else:
            miss = miss + 1
    print 'Num real targets: ' + str(len(real_targets))
    print 'Num pred targets: ' + str(len(predicted_targets))
    print 'Texture: ' + texture_name
    print 'Model:   ' + model_name
    print 'Hits:    ' + str(hit)
    print 'Miss:    ' + str(miss)
    print 'Total:   ' + str(len(real_targets))
    print '% Hit:   ' + str(float(hit)/len(real_targets))
    print '% Miss:  ' + str(float(miss)/len(real_targets))
    print
    
#display_texture_stats('Grass', 'LinSVM',   grass_test_targets, grass_lin_predicted_targets)
#display_texture_stats('Hive',  'LinSVM',   hive_test_targets,  hive_lin_predicted_targets)
#display_texture_stats('Pad',   'LinSVM',   pad_test_targets,   pad_lin_predicted_targets)

#display_texture_stats('Grass', 'CSLinSVM',  grass_test_targets, grass_cs_lin_predicted_targets)
#display_texture_stats('Hive',  'CSLinSVM',  hive_test_targets,  hive_cs_lin_predicted_targets)
#display_texture_stats('Pad',   'CSLinSVM',  pad_test_targets,   pad_cs_lin_predicted_targets)

#display_texture_stats('Grass', 'OVRLinSVM', grass_test_targets, grass_cs_lin_predicted_targets)
#display_texture_stats('Hive',  'OVRLinSVM', hive_test_targets,  hive_cs_lin_predicted_targets)
#display_texture_stats('Pad',   'OVRLinSVM', pad_test_targets,   pad_cs_lin_predicted_targets)

#display_texture_stats('Grass', 'NuSVM', grass_test_targets, grass_nu_lin_predicted_targets)
#display_texture_stats('Hive',  'NuSVM', hive_test_targets,  hive_nu_lin_predicted_targets)
#display_texture_stats('Pad',   'NuSVM', pad_test_targets,   pad_nu_lin_predicted_targets)

#display_texture_stats('Grass', 'NuSVM2', grass_test_targets, grass_nu_lin_predicted_targets)
#display_texture_stats('Hive',  'NuSVM2', hive_test_targets,  hive_nu_lin_predicted_targets)
#display_texture_stats('Pad',   'NuSVM2', pad_test_targets,   pad_nu_lin_predicted_targets)

display_texture_stats('Grass', 'NuSVM3', grass_test_targets, grass_nu_lin_predicted_targets)
display_texture_stats('Hive',  'NuSVM3', hive_test_targets,  hive_nu_lin_predicted_targets)
display_texture_stats('Pad',   'NuSVM3', pad_test_targets,   pad_nu_lin_predicted_targets)

#display_target_misses(grass_test_fpaths, grass_test_targets, grass_lin_predicted_targets)
#display_target_misses(hive_test_fpaths,  hive_test_targets,  hive_lin_predicted_targets)
#display_target_misses(pad_test_fpaths,   pad_test_targets,   pad_lin_predicted_targets)

#display_target_misses(grass_test_fpaths, grass_test_targets, grass_cs_lin_predicted_targets)
#display_target_misses(hive_test_fpaths,  hive_test_targets,  hive_cs_lin_predicted_targets)
#display_target_misses(pad_test_fpaths,   pad_test_targets,   pad_cs_lin_predicted_targets)

#display_target_misses(grass_test_fpaths, grass_test_targets, grass_ovr_lin_predicted_targets)
#display_target_misses(hive_test_fpaths,  hive_test_targets,  hive_ovr_lin_predicted_targets)
#display_target_misses(pad_test_fpaths,   pad_test_targets,   pad_ovr_lin_predicted_targets)

#display_target_misses(grass_test_fpaths, grass_test_targets, grass_nu_lin_predicted_targets)
#display_target_misses(hive_test_fpaths,  hive_test_targets,  hive_nu_lin_predicted_targets)
#display_target_misses(pad_test_fpaths,   pad_test_targets,   pad_nu_lin_predicted_targets)

#display_target_misses(grass_test_fpaths, grass_test_targets, grass_nu_lin_predicted_targets_2)
#display_target_misses(hive_test_fpaths,  hive_test_targets,  hive_nu_lin_predicted_targets_2)
#display_target_misses(pad_test_fpaths,   pad_test_targets,   pad_nu_lin_predicted_targets_2)

display_target_misses(grass_test_fpaths, grass_test_targets, grass_nu_lin_predicted_targets_3)
display_target_misses(hive_test_fpaths,  hive_test_targets,  hive_nu_lin_predicted_targets_3)
display_target_misses(pad_test_fpaths,   pad_test_targets,   pad_nu_lin_predicted_targets_3)

#display_targets(grass_test_fpaths, grass_test_targets, predicted_targets)
#display_targets(hive_test_fpaths,  hive_test_targets,  predicted_targets)
#display_targets(pad_test_fpaths,   pad_test_targets,   predicted_targets)

#display_texture_stats('Grass', 'SVM', grass_test_targets, grass_predicted_targets)
#display_texture_stats('Hive','SVM',   hive_test_targets,  hive_predicted_targets)
#display_texture_stats('Pad', 'SVM',   pad_test_targets,   pad_predicted_targets)









    


