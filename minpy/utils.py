import minpy.numpy as np
import pickle
import os
import flags

def get_accuracy(output, label):
    return 1 - np.count_nonzero(output - label).val / float(label.shape[0])

def get_sparsity(activation):
    return 1 - np.count_nonzero(activation).val / get_size(activation)

def get_deactivated_scale(deactivation, num_epoch):
    return [deactivation[deactivation == t].shape[0] / get_size(deactivation)
            for t in range(num_epoch + 1)]

def get_size(array):
    size = 1.0
    for d in array.shape:
        size *= d 
    return size

def get_mean(array):
    means = array.mean(axis=0)
    return (means.min(), means.max(), array.mean())

def get_std_deviation(array):
    deviations = array.std(axis=0)
    return (deviations.min(), deviations.max(), array.std())

def record_model(model):
    if not os.path.exists('Log'):
        os.system('mkdir Log/')
    if not os.path.exists('Log/' + flags.NAME):
        os.system('mkdir Log/%s/' % flags.NAME)
    pickle.dump(model, open('Log/%s/Model.pkl' % flags.NAME, 'wb'))

def record_settings(model_name, model_setting, solver_setting):
    if not os.path.exists('Log'):
        os.system('mkdir Log/')
    if not os.path.exists('Log/' + flags.NAME):
        os.system('mkdir Log/%s/' % flags.NAME)
    pickle.dump([flags.NAME, model_setting, solver_setting], open('Log/%s_setting.pkl' % (model_name), 'wb'))

def record_activation(records):
    if not os.path.exists('Log'):
        os.system('mkdir Log/')
    if not os.path.exists('Log/' + flags.NAME):
        os.system('mkdir Log/%s/' % flags.NAME)
    pickle.dump(records, open('Log/%s/%s-epoch-%d_activation.pkl' % (flags.NAME, flags.NAME, flags.EPOCH),'wb'))

def record_parameter(records):
    if not os.path.exists('Log'):
        os.system('mkdir Log/')
    if not os.path.exists('Log/' + flags.NAME):
        os.system('mkdir Log/%s/' % flags.NAME)
    pickle.dump(records, open('Log/%s/%s-epoch-%d_parameter.pkl' % (flags.NAME, flags.NAME, flags.EPOCH),'wb'))

def record_gradient(records):
    if not os.path.exists('Log'):
        os.system('mkdir Log/')
    if not os.path.exists('Log/' + flags.NAME):
        os.system('mkdir Log/%s/' % flags.NAME)
    pickle.dump(records, open('Log/%s/%s-epoch-%d_gradient.pkl' % (flags.NAME, flags.NAME, flags.EPOCH),'wb'))

def record_loss(records):
    if not os.path.exists('Log'):
        os.system('mkdir Log/')
    if not os.path.exists('Log/' + flags.NAME):
        os.system('mkdir Log/%s/' % flags.NAME)
    pickle.dump(records, open('Log/%s/%s_loss.pkl' % (flags.NAME, flags.NAME),'wb'))
